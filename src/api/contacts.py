from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.schemas import ContactSchema, ContactUpdateSchema
from src.services.contacts import create_contact, get_contacts

router = APIRouter()

@router.post("/", response_model=ContactSchema)
def create_new_contact(contact: ContactSchema, db: Session = Depends(get_db)):
    return create_contact(db, contact)

@router.get("/", response_model=list[ContactSchema])
def get_all_contacts(db: Session = Depends(get_db)):
    return get_contacts(db)
