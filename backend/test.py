from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Test API di MeetInCampus")

@app.get("/test")
async def test():
    return {"message": "API OK MeetInCampus"}


if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0", port=8000)