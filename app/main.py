from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Production Ready", "devops_level": "Expert"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
