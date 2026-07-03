import os
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
from fastapi.responses import FileResponse
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import SessionLocal, engine, Base
from models import ContactMessage as ContactMessageModel 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# Initialize Database
Base.metadata.create_all(bind=engine)
app = FastAPI()

# CORS Config
origins = [
    "https://manojkc1.com.np",
    "https://www.manojkc1.com.np",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schema
class ContactMessageSchema(BaseModel):
    name: str
    email: EmailStr
    message: str

load_dotenv()
MY_EMAIL = os.getenv("EMAIL_USER")
# Use environment variables for Relay Service (e.g., Brevo/SendGrid) instead of Gmail
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("EMAIL_USER")
SMTP_PASS = os.getenv("EMAIL_PASSWORD")

def send_email_notification(sender_name, sender_email, sender_message):
    msg = EmailMessage()
    msg.set_content(f"New message from: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{sender_message}")
    msg['Subject'] = "New Portfolio Contact"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    try:
        # Using a generic relay setup
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"ERROR: Email failed: {e}")
        return False

@app.post("/api/contact")
async def contact_route(
    contact_data: ContactMessageSchema, 
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db) # Added database dependency
):
    # Save to Database
    new_message = ContactMessageModel(
        name=contact_data.name,
        email=contact_data.email,
        message=contact_data.message
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    
    # Queue Email
    background_tasks.add_task(
        send_email_notification, 
        contact_data.name, 
        contact_data.email, 
        contact_data.message
    )
    
    return {"status": "success", "message": "Message saved and notification queued."}

@app.get("/")
def read_root():
    return FileResponse("index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")