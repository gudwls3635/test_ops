from fastapi import FastAPI
from app.routes import summary
from contextlib import asynccontextmanager
from app.services.summary_service import running_tasks
from app.config import settings
import asyncio 

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작
    yield
    # 종료 
    for task in running_tasks:
        task.cancel()
    # 모든 태스크가 완료될 때까지 대기
    if running_tasks:
        await asyncio.gather(*running_tasks, return_exceptions=True)
    # 태스크 세트 비우기
    running_tasks.clear()

app = FastAPI()

# 라우터 등록
app.include_router(summary.router, prefix="/text", tags=["Summary"])

if settings.IS_DEV:
    from app.dev.ui.components import GradioUIBuilder
    from app.dev.ui.dev_components import DevUIBuilder
    from gradio import mount_gradio_app
    # gradio
    interface = GradioUIBuilder().create_ui()
    interface.queue()
    app = mount_gradio_app(app, interface, path="/gradio")
    #
    #dev
    dev_interface = DevUIBuilder().create_ui()
    dev_interface.queue()
    app = mount_gradio_app(app, dev_interface, path="/dev")
    #

# FastAPI에 MCP SSE 서버를 '/mcp' 마운트
if settings.ENABLE_MCP:
    from app.services.mcp_service import mcp
    app.mount("/", mcp.sse_app())


