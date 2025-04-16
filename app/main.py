from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.router import router as api_router
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

app.include_router(api_router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("base.html", {"request": request, "title": "Главная страница"})

@app.get("/about/", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("base.html", {
        "request": request,
        "title": "This Site",
        "content": "Демонстрационный сайт для ДЗ по веб-приложению."
                   "Разработчик: Mikhail G."
    })