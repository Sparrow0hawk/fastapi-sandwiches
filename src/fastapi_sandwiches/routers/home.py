from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

PROJECT_ROOT = Path(__file__).parent.parent

templates = Jinja2Templates(directory=PROJECT_ROOT.joinpath("templates"))


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", context={"request": request})
