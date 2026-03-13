from fastapi import FastAPI, Request
from app.api.v1 import barang_route, auth_route
from app.core.exceptions import InventoryException
from fastapi.responses import JSONResponse
from app.core.middleware import log_requests
from app.core.config_log import setup_logging

setup_logging()

app = FastAPI(title="Inventory API")

app.middleware("http")(log_requests)
# GLOBAL ERROR HANDLER
@app.exception_handler(InventoryException)
async def inventory_exception_handler(request: Request, exc: InventoryException):
    # Di sini kita tentukan status code berdasarkan kodenya
    status_map = {"ITEM_NOT_FOUND": 404, "UNAUTHORIZED": 401, "INVALID_PRICE": 400}
    return JSONResponse(
        status_code=status_map.get(exc.code, 400),
        content={"error_code": exc.code, "message": exc.message}
    )
# Mendaftarkan Router
app.include_router(barang_route.router, prefix="/barang", tags=["Barang"])
app.include_router(auth_route.router, prefix="/auth", tags=["Auth"])