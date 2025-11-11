"""
Resume AI Optimizer - FastAPI Main Application
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
import uvicorn

from app.database import init_db, get_db
from app.routers import resume, health
from app.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """生命周期管理：启动时初始化数据库"""
    init_db()
    yield
    # 关闭时清理资源（如需要）

app = FastAPI(
    title="Resume AI Optimizer API",
    description="AI-powered resume optimization service",
    version="1.0.0",
    lifespan=lifespan
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(resume.router, prefix="/api/resume", tags=["Resume"])

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """全局异常处理"""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "message": str(exc)}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

