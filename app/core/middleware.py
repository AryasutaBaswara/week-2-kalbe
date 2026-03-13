import time
import logging
from fastapi import Request

logger = logging.getLogger("inventory_api")

async def log_requests(request: Request, call_next):
    # 1. Catat waktu sebelum request diproses
    start_time = time.time()
    
    # 2. Lanjut ke proses berikutnya (Route/Service/Repo)
    response = await call_next(request)
    
    # 3. Hitung selisih waktu (dalam milidetik)
    process_time = (time.time() - start_time) * 1000
    
    # 4. Catat hasil ke terminal
    logger.info(
        f"Method: {request.method} | "
        f"Path: {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Time: {process_time:.2f}ms"
    )
    
    return response