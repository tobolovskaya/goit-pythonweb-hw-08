from fastapi import FastAPI

from src.api import utils, contacts

app = FastAPI(
    title="Contacts API",
    description="goit-pythonweb-hw-08",
    version="1.0.0",
)

app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

