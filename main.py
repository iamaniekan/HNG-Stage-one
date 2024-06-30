from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
    
@app.get("/api/hello")
async def visitor_info(request: Request, visitor_name: str):
    client_ip = "127.0.0.1"
    temperature = 11
    location = "New York"
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}"
    
    return {
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
