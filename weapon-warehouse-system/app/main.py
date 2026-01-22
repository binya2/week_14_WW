import io
import os

import pandas as pd
from fastapi import FastAPI, UploadFile
import uvicorn

app = FastAPI(title="weapon-warehouse-system")


@app.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    csv_string = content.decode('utf-8')
    df = pd.read_csv(io.StringIO(csv_string))
    print(df)
    return {"filename": file.filename,
            "data:": df.to_dict()}


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=os.getenv("DB_PORT", 8000),
        reload=True,
    )
