from fastapi import FastAPI
from tasks import router

app = FastAPI(title="To-Do List API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
