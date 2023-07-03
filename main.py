from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
import uvicorn
import joblib

app = FastAPI()

class StartupData(BaseModel):
    rd: float =150
    admin: float =35
    marketing: float =28


@app.on_event("startup")
def loadmodel():
    global model 
    model = joblib.load("startup.pkl")
    print(" MODELLO CARICATO")
    return model

@app.get("/predict")
async def predictget(data:StartupData=Depends()):
    try:
        X = [[data.rd, data.admin, data.marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")
    
@app.post("/predict")
async def predictpost(data:StartupData):
    try:
        X = [[data.rd, data.admin, data.marketing]]
        y_pred = model.predict(X)[0]
        res = round(y_pred,2)
        return {'prediction':res}
    except:
        raise HTTPException(status_code=404, detail="error")



if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)
