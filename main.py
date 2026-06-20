import smtplib
from email.message import EmailMessage

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import SessionLocal, engine, Base
from models import ContactMessage as ContactMessageModel 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


# 1. INITIALIZE DATABASE TABLES
Base.metadata.create_all(bind=engine)

# 2. INITIALIZE FASTAPI APP
app = FastAPI()

# 3. CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://manojkc1.com.np"], #LIVE DOMAIN
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. DATABASE SESSION DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. PYDANTIC VALIDATION SCHEMA
class ContactMessageSchema(BaseModel):
    name: str
    email: EmailStr
    message: str



# --- EMAIL CONFIGURATION ---
MY_EMAIL = "khatrimanoj2135@gmail.com"
# PASTE YOUR 16-CHARACTER APP PASSWORD HERE (No spaces)
MY_APP_PASSWORD = "bmkk mpuy vvme uobk" 

def send_email_notification(sender_name, sender_email, sender_message):
    try:
        msg = EmailMessage()
        msg.set_content(f"You got a new message from your portfolio!\n\nName: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{sender_message}")
        
        # Make sure you only have EXACTLY ONE of each of these lines!
        msg['Subject'] = f"Portfolio Contact: {sender_name}"
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        msg['Reply-To'] = sender_email

        # Connect to Gmail securely
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(MY_EMAIL, MY_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("SUCCESS: Email notification sent to your inbox!")
    except Exception as e:
        print(f"ERROR: Failed to send email: {e}")

# --- Email Configuration END ---        

# 6. POST ENDPOINT FOR CONTACT FORM
@app.post("/contact")
async def create_contact_message(data: ContactMessageSchema, db: Session = Depends(get_db)):
    new_message = ContactMessageModel(
        name=data.name,
        email=data.email,
        message=data.message
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    send_email_notification(data.name, data.email, data.message)
    return {"status": "success", "message": "Message Sent Successfully!"}

# 7. GET ENDPOINT FOR PROJECTS
@app.get("/projects")
async def get_projects():
    return {"projects": [
        {"title": "AcadFlow SMS", "description": "Student system"},
        {"title": "Shabdhabhandar", "description": "Dictionary app"}
    ]}

# 8. MOUNT STATIC FILES (MUST BE AT THE VERY BOTTOM)
# This serves index.html at the root ("/") automatically without conflicting routes.
app.mount("/", StaticFiles(directory=".", html=True), name="static")

@app.get("/health")
def health_check():
    return {"status": "healthy"}