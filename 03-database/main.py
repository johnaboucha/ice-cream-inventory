from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name="static")
templates = Jinja2Templates(directory="templates")

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.get("/", response_class=HTMLResponse)
def root(request: Request, db: Session = Depends(get_db)):
	return templates.TemplateResponse("index.html", {"request": request, "title":" - Home"})