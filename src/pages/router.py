from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Pages"])

templates = Jinja2Templates(directory="src/templates")


@router.get("/base")
def get_base_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/search")
def get_search_page(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@router.get("/chat")
def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})
