from fastapi import Request
from fastapi.responses import JSONResponse
from core.errors import CSVFormatError, DBError

def register_handlers(app):
    @app.exception_handler(CSVFormatError)
    async def csv_handler(request: Request, exc: CSVFormatError):
        return JSONResponse(status_code=400, content={"error": "Invalid CSV", "detail": exc.message})

    @app.exception_handler(DBError)
    async def db_handler(request: Request, exc: DBError):
        return JSONResponse(status_code=500, content={"error": "Database Error", "detail": exc.message})
