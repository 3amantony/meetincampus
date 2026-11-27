from sqlalchemy import *
from sqlalchemy.orm import *
from collections.abc import Iterator
import os


URL = os.environ.get("DATABASE_URL","sqlite:///../db/database.db")
engine_db = create_engine(URL)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__="User"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

Base.metadata.create_all(engine_db)

def get_session() -> Iterator[Session]:
    with Session(engine_db) as ses:
        yield ses




# #Testing con file di testo di register e login, poi aggiungo il db
# async def register(user):
#     with open(file="./db/file.txt",mode="a+") as file:
#         file.seek(0)
#         for riga in file:
#             if riga.split(":")[0] == user.username:
#                 return {"message": "utente già esistnete"}
#         file.write(user.username+":"+user.passwd+"\n")
#         return {"message": "utente registrato con successo"}


# async def login(user):
#     with open(file="./db/file.txt") as file:
#         file.seek(0)
#         for riga in file:
#             if riga.split(":")[0] == user.username and riga.split(":")[1].strip() == user.passwd:
#                 return {"message": "utente loggato con successo"}
#         return {"message": "password errata e/o utente inesistente"}







