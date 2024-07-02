from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

app = FastAPI()

WEATHER_API_KEY = os.getenv("API_KEY")


def get_location_by_ip():
    url = f"http://api.weatherapi.com/v1/ip.json?key={WEATHER_API_KEY}&q=auto:ip"
    response = requests.get(url)
    data = response.json()
    ip = data["ip"]
    city = data["city"]
    return ip, city

def get_weather(location: str):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}"
    response = requests.get(url)
    data = response.json()
    temperature = data["current"]["temp_c"]
    city = data["location"]["name"]
    return temperature, city

@app.get("/api/hello")
async def visitor_info(request: Request, visitor_name: str):
    client_ip, location = get_location_by_ip()
    temperature, city = get_weather(client_ip)
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    
    return {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
