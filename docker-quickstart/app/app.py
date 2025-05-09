from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "OK"}

if __name__ == '__main__':
    uvicorn.run("app:app",host='0.0.0.0',port=80)