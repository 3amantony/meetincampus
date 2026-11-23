

#Testing con file di testo di register e login, poi aggiungo il db
async def register(user):
    with open(file="./db/file.txt",mode="a+") as file:
        file.seek(0)
        for riga in file:
            if riga.split(":")[0] == user.username:
                return {"message": "utente già esistnete"}
        file.write(user.username+":"+user.passwd+"\n")
        return {"message": "utente registrato con successo"}


async def login(user):
    with open(file="./db/file.txt") as file:
        file.seek(0)
        for riga in file:
            if riga.split(":")[0] == user.username and riga.split(":")[1].strip() == user.passwd:
                return {"message": "utente loggato con successo"}
        return {"message": "password errata e/o utente inesistente"}







