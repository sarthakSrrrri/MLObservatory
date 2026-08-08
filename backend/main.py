from fastapi import FastAPI

app = FastAPI(title="MLObservatory")


@app.get("/")
def root():
    return {"message": "MLObservatory is running"}