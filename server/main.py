from fastapi import FastAPI
from app.routes import summary
from app.services.summary_service import running_tasks
from app.config import settings

app = FastAPI()

# 라우터 등록
app.include_router(summary.router, prefix="/test", tags=["test"])


