from typing import List, Optional
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker Backend")

# Allow your React dev server to talk to this API.
# Tighten this list when you deploy.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/applications", response_model=List[schemas.ApplicationOut])
def list_applications(
    status: Optional[models.StatusEnum] = None,
    sort_by: str = "date_applied",
    order: str = "desc",
    db: Session = Depends(get_db),
):
    query = db.query(models.Application)
    if status:
        query = query.filter(models.Application.status == status)

    sort_column = getattr(models.Application, sort_by, models.Application.date_applied)
    query = query.order_by(desc(sort_column) if order == "desc" else asc(sort_column))

    return query.all()


@app.post("/applications", response_model=schemas.ApplicationOut, status_code=201)
def create_application(payload: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    application = models.Application(**payload.model_dump())
    db.add(application)
    db.commit()
    db.refresh(application)
    return application


@app.get("/applications/{application_id}", response_model=schemas.ApplicationOut)
def get_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.Application).get(application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application


@app.put("/applications/{application_id}", response_model=schemas.ApplicationOut)
def update_application(
    application_id: int, payload: schemas.ApplicationUpdate, db: Session = Depends(get_db)
):
    application = db.query(models.Application).get(application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(application, field, value)

    db.commit()
    db.refresh(application)
    return application


@app.delete("/applications/{application_id}", status_code=204)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    application = db.query(models.Application).get(application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(application)
    db.commit()
