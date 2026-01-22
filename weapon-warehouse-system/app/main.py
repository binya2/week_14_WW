from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi import UploadFile

from db.repository import init_tables
from service import data_processing, save_to_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Executing database initialization...")
    try:
        init_tables()
    except Exception as e:
        print(f"Startup failed: {e}")
    yield
    print("Server shutting down...")


app = FastAPI(title="weapon-warehouse-system", lifespan=lifespan)


@app.post("/upload")
async def upload_file(file: UploadFile):
    data = await data_processing(file)
    response = await save_to_db(data)
    return {
        "filename": file.filename,
        "status": "processed",
        "db_response": response
    }


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
