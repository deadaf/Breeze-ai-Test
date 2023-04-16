from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/reverse")
async def string_reverse(input:str):
    return input[::-1]

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0',port=8001)