from dataclasses import dataclass
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

PROJECT_ROOT = Path(__file__).parent.parent

templates = Jinja2Templates(directory=PROJECT_ROOT.joinpath("templates"))


@router.get("/")
def home(request: Request):
    data = [Sandwiches(name="Marmite and Cheese", count=10)]
    return templates.TemplateResponse("home.html", context={"request": request, "sandwiches": data})


@dataclass
class Sandwiches:
    name: str
    count: int
