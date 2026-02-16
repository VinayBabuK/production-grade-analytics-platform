from fastapi import FastAPI

app = FastAPI(
    title="Production-Grade Analytics Platform",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "Backend is running"}
