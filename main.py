from fastapi import FastAPI, Form,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI()

# mount static file
app.mount("/static", StaticFiles(directory="static"), name="static")

# load templates
templates = Jinja2Templates(directory="templates")

# home page
@app.get("/",response_class=HTMLResponse,name="home")
async def root(request:Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/weather",name="get_weather")
async def getWeather(req:Request,location:str=Form(...)):
    key=os.getenv("WEATHER_API")
    endpoint=os.getenv("WEATHER_ENDPOINT")
    fullEndpoint=endpoint+"current.json?key="+key+"&q="+location+"&aqi=yes"
    data=requests.get(fullEndpoint) 
    status_code = data.status_code
    if(status_code==200):
        data=data.json()
        # data page
        return templates.TemplateResponse("data.html",{"request": req,"weather":data})
    else:
        # error page
        return templates.TemplateResponse("error.html",{"request": req,"location":location})

 
