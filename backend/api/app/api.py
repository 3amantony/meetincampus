from fastapi import FastAPI,routing
import uvicorn
from pydantic import BaseModel
from routers.auth import register,login
from routers.auth import router as api_router
#Modello da usare per il JSON della richiesta di register 
# Da aggiungere id per il db, e adattarlo all' uso per db




app = FastAPI(title="Test API di MeetInCampus",version="0.1")
app.include_router(api_router)

# @app.get("/test")
# async def test():
#     return {"message": "API OK MeetInCampus"}
# #Endpoint di registrazione (test)
# @app.post("/register")
# async def user_register(user: UserReg):
#     return await register(user)
# #Endpoint di login (test)
# @app.post("/login")
# async def user_login(user: UserReg):
#     return await login(user)



if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)