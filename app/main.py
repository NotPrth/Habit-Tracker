from fastapi import FastAPI

app=FastAPI(
    title="Habit Tracker API",
    description="We track them and we make them",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}