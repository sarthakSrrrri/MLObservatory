from fastapi import FastAPI

app = FastAPI(title="MLObservatory")


@app.get("/")
def root():
    return {"message": "MLObservatory API is running"}