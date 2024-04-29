from fastapi import FastAPI
from generator import traffic
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)
  
@app.get("/")

def trafficStatus():
    i = 10
    trafficList = []
    while i >= 0: 
        trafficList.append(traffic())
        i -= 1
    return trafficList
    
async def root():
  attempt = trafficStatus()
  
  return attempt
  