import io
import os
from contextlib import asynccontextmanager

import pandas as pd
import uvicorn
from fastapi import FastAPI
from fastapi import UploadFile


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Executing database initialization...")
    try:
        pass # init_db()
    except Exception as e:
        print(f"Startup failed: {e}")
    yield
    print("Server shutting down...")


app = FastAPI(title="weapon-warehouse-system", lifespan=lifespan)


@app.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    csv_string = content.decode('utf-8')
    df = pd.read_csv(io.StringIO(csv_string))
    print(df)
    return {"filename": file.filename, "rows": len(df)}


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
