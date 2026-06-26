import os
from dotenv import load_dotenv

import smtplib
from email.message import EmailMessage
from fastapi.responses import FileResponse

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import SessionLocal, engine, Base
from models import ContactMessage as ContactMessageModel 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "https://manojkc1.com.np",
    "https://www.manojkc1.com.np",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class ContactMessageSchema(BaseModel):
    name: str
    email: EmailStr
    message: str



load_dotenv()
MY_EMAIL = os.getenv("EMAIL_USER")
MY_APP_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email_notification(sender_name, sender_email, sender_message):
    # 1. Setup the message
    msg = EmailMessage()
    msg.set_content(f"New message from: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{sender_message}")
    msg['Subject'] = "New Portfolio Contact"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    # 2. Use Port 587 with STARTTLS (Most reliable for Gmail)
    try:
        print("Attempting to connect to Gmail SMTP...")
        # Use port 587 for TLS
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Upgrade to secure connection
            
            # REMOVE ALL SPACES FROM YOUR APP PASSWORD
            # Example: "abcd efgh ijkl mnop" -> "abcdefghijklmnop"
            server.login(MY_EMAIL, MY_APP_PASSWORD) 
            
            server.send_message(msg)
        
        print("SUCCESS: Email sent successfully!")
        return True
        
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed. Check your email and 16-character App Password (no spaces).")
    except Exception as e:
        print(f"ERROR: A connection or server error occurred: {e}")
    
    return False



@app.post("/api/contact")
async def create_contact_message(data: ContactMessageSchema, db: Session = Depends(get_db)):
    try:
        new_message = ContactMessageModel(name=data.name, email=data.email, message=data.message)
        db.add(new_message)
        db.commit()
        db.refresh(new_message)
        
        send_email_notification(data.name, data.email, data.message)
        return {"status": "success", "message": "Message Sent Successfully!"}
    
    except Exception as e:
        # THIS PRINTS THE REAL ERROR TO YOUR VS CODE TERMINAL
        print(f"--- DEBUG ERROR: {str(e)} ---")
        # THIS SENDS THE REAL ERROR TO THE BROWSER
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/")
def read_root():
    return FileResponse("index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")