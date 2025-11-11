"""
简历优化API路由
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from app.database import get_db, Resume
from app.services.ai_service import ai_service

router = APIRouter()

# 请求模型
class ResumeOptimizeRequest(BaseModel):
    """简历优化请求"""
    content: str
    job_description: Optional[str] = None

class ResumeCreateRequest(BaseModel):
    """创建简历请求"""
    original_content: str
    job_description: Optional[str] = None

# 响应模型
class ResumeResponse(BaseModel):
    """简历响应"""
    id: int
    original_content: str
    optimized_content: Optional[str]
    job_description: Optional[str]
    status: str
    created_at: datetime
    updated_at: datetime
    optimization_notes: Optional[str]
    
    class Config:
        from_attributes = True

@router.post("/optimize", response_model=dict)
async def optimize_resume(
    request: ResumeOptimizeRequest,
    db: Session = Depends(get_db)
):
    """
    直接优化简历内容（不保存到数据库）
    """
    try:
        result = await ai_service.optimize_resume(
            request.content,
            request.job_description
        )
        return {
            "success": True,
            "optimized_content": result["optimized_content"],
            "notes": result.get("notes", "")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=ResumeResponse)
async def create_resume(
    request: ResumeCreateRequest,
    db: Session = Depends(get_db)
):
    """
    创建简历记录
    """
    try:
        resume = Resume(
            original_content=request.original_content,
            job_description=request.job_description,
            status="pending"
        )
        db.add(resume)
        db.commit()
        db.refresh(resume)
        return resume
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{resume_id}/optimize", response_model=ResumeResponse)
async def optimize_resume_by_id(
    resume_id: int,
    db: Session = Depends(get_db)
):
    """
    优化指定ID的简历
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    
    if resume.status == "processing":
        raise HTTPException(status_code=400, detail="简历正在处理中")
    
    try:
        resume.status = "processing"
        db.commit()
        
        result = await ai_service.optimize_resume(
            resume.original_content,
            resume.job_description
        )
        
        resume.optimized_content = result["optimized_content"]
        resume.optimization_notes = result.get("notes", "")
        resume.status = "completed"
        resume.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(resume)
        
        return resume
    except Exception as e:
        resume.status = "failed"
        db.commit()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{resume_id}", response_model=ResumeResponse)
async def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    """
    获取简历详情
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    return resume

@router.get("/", response_model=list[ResumeResponse])
async def list_resumes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    获取简历列表
    """
    resumes = db.query(Resume).offset(skip).limit(limit).all()
    return resumes

@router.delete("/{resume_id}")
async def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    """
    删除简历
    """
    resume = db.query(Resume).filter(Resume.id == resume_id).first()
    if not resume:
        raise HTTPException(status_code=404, detail="简历不存在")
    
    db.delete(resume)
    db.commit()
    return {"message": "简历已删除"}

