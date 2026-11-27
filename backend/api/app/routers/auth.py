from fastapi import APIRouter,Depends
from database import User,get_session
from sqlalchemy import select,insert
from sqlalchemy.orm import Session
from pydantic import *

router = APIRouter(prefix="/auth",tags=["auth"])

class UserReg(BaseModel):
    username: str
    passwd: str

@router.post("/register")
async def register(user: UserReg, ses: Session = Depends(get_session)):
    #Fa la query e vede se trova un utente con lo stesso nome
    a = select(User).where(User.nome==user.username)
    #Ritorna una entry del db se l' utente esiste oppure None se non esiste
    user_ipotetico = ses.scalars(a).one_or_none()
    #Se esiste già ritorna questo messaggio
    if(user_ipotetico != None):
        return {"message":"Utente già esistente"}
    #Mappa l' utente sul modello del db
    nuovo_user = User(nome=user.username,password=user.passwd)
    #Aggiunge l' user al db
    ses.add(nuovo_user)
    ses.commit()
      

@router.post("/login")
async def login(user: UserReg, ses: Session = Depends(get_session)):

    a = select(User).where(User.nome==user.username)
    #Ritorna una entry del db se l' utente esiste oppure None se non esiste
    user_ipotetico = ses.scalars(a).one_or_none()
    # Se non esiste ritorna    
    if(user_ipotetico==None):
        return {"message":"Utente inesistente"}
    # Se esiste e la password è corretta ritorna 
    if(user_ipotetico.nome == user.username and user_ipotetico.password==user.passwd):
        return {"message":"Utente loggato con successo"}
