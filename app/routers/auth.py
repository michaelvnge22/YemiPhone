from fastapi import APIRouter, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.auth import ServiceAuth

auth = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@auth.get('/login', response_class=HTMLResponse)
async def connexion(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth.get('/register', response_class=HTMLResponse)
async def inscription(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@auth.post("/login")
async def connexion_post(request: Request, email: str = Form(...),password: str = Form(...)):
    pass

@auth.post("/register")
async def inscription_post(
    name: str = Form(...),
    firsname: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    conf_password: str = Form(...)
    ):
    my_auth = await ServiceAuth.inscription(name, firsname, email, password, conf_password)
    if not my_auth:
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="echec d'inscription")
    return {"reponse": "inscription reussi"}
