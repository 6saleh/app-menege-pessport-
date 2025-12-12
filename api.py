
from fastapi import FastAPI, HTTPException, Request, Form

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.passport_service import (
    add_passport,
    view_all_passports,
    search_passport,
    update_passport,
    delete_passport
)
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend"), name="static")
templates = Jinja2Templates(directory="frontend")

class Passport(BaseModel):
    national_id: str
    passport_number: str
    full_name: str
    date_of_birth: str
    nationality: str
    issue_date: str
    expiry_date: str
    authority: str

class PassportUpdate(BaseModel):
    full_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    nationality: Optional[str] = None
    issue_date: Optional[str] = None
    expiry_date: Optional[str] = None
    authority: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/passports", response_class=HTMLResponse)
def get_all_passports(request: Request):
    passports = view_all_passports()
    return templates.TemplateResponse("partials/passport_list.html", {"request": request, "passports": passports})

@app.get("/passports/{passport_number}")
def get_passport(passport_number: str):
    passport = search_passport(passport_number)
    if not passport:
        raise HTTPException(status_code=404, detail="Passport not found")
    return passport[0]

@app.post("/passports", response_class=HTMLResponse)
async def create_passport(request: Request, 
                        national_id: str = Form(...),
                        passport_number: str = Form(...),
                        full_name: str = Form(...),
                        date_of_birth: str = Form(...),
                        nationality: str = Form(...),
                        issue_date: str = Form(...),
                        expiry_date: str = Form(...),
                        authority: str = Form(...)                        
                        ):
    try:
        add_passport(national_id, passport_number, full_name, date_of_birth, nationality, issue_date, expiry_date, authority)
        passports = view_all_passports()
        return templates.TemplateResponse("partials/passport_list.html", {"request": request, "passports": passports})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/passports/{passport_number}", response_class=HTMLResponse)
def update_passport_api(request: Request, passport_number: str, 
                        full_name: Optional[str] = Form(None),
                        date_of_birth: Optional[str] = Form(None),
                        nationality: Optional[str] = Form(None),
                        issue_date: Optional[str] = Form(None),
                        expiry_date: Optional[str] = Form(None),
                        authority: Optional[str] = Form(None)
                        ):
    updates = {}
    if full_name: updates['full_name'] = full_name
    if date_of_birth: updates['date_of_birth'] = date_of_birth
    if nationality: updates['nationality'] = nationality
    if issue_date: updates['issue_date'] = issue_date
    if expiry_date: updates['expiry_date'] = expiry_date
    if authority: updates['authority'] = authority

    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")
    update_passport(passport_number, **updates)
    passports = view_all_passports()
    return templates.TemplateResponse("partials/passport_list.html", {"request": request, "passports": passports})

@app.delete("/passports/{passport_number}", response_class=HTMLResponse)
def delete_passport_api(request: Request, passport_number: str):
    delete_passport(passport_number)
    passports = view_all_passports()
    return templates.TemplateResponse("partials/passport_list.html", {"request": request, "passports": passports})

@app.get("/search/passports")
def search_passports_api(search_term: str):
    return search_passport(search_term)
