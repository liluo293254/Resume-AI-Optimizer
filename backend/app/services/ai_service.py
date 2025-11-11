"""
AI服务：集成Ollama和OpenAI
"""
import httpx
from typing import Optional
from app.config import settings

class AIService:
    """AI优化服务"""
    
    def __init__(self):
        self.ollama_url = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL
        self.use_openai = settings.USE_OPENAI
        self.openai_key = settings.OPENAI_API_KEY
    
    async def optimize_resume(
        self,
        resume_content: str,
        job_description: Optional[str] = None
    ) -> dict:
        """
        优化简历内容
        
        Args:
            resume_content: 原始简历内容
            job_description: 职位描述（可选）
        
        Returns:
            包含优化后内容和建议的字典
        """
        if self.use_openai and self.openai_key:
            return await self._optimize_with_openai(resume_content, job_description)
        else:
            return await self._optimize_with_ollama(resume_content, job_description)
    
    async def _optimize_with_ollama(
        self,
        resume_content: str,
        job_description: Optional[str] = None
    ) -> dict:
        """使用Ollama优化简历"""
        prompt = self._build_prompt(resume_content, job_description)
        
        try:
            async with httpx.AsyncClient(timeout=120.0) as client:
                response = await client.post(
                    f"{self.ollama_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "stream": False
                    }
                )
                response.raise_for_status()
                result = response.json()
                
                optimized_text = result.get("response", "")
                
                # 解析优化后的内容（简单实现，可根据实际需求改进）
                return {
                    "optimized_content": optimized_text,
                    "notes": "简历已通过AI优化，建议根据实际情况进一步调整。"
                }
        except httpx.RequestError as e:
            raise Exception(f"Ollama服务连接失败: {str(e)}")
        except Exception as e:
            raise Exception(f"AI优化失败: {str(e)}")
    
    async def _optimize_with_openai(
        self,
        resume_content: str,
        job_description: Optional[str] = None
    ) -> dict:
        """使用OpenAI优化简历（可选）"""
        # 实现OpenAI API调用
        # 这里提供基本框架，实际使用时需要安装openai包
        raise NotImplementedError("OpenAI集成待实现")
    
    def _build_prompt(
        self,
        resume_content: str,
        job_description: Optional[str] = None
    ) -> str:
        """构建优化提示词"""
        base_prompt = f"""你是一位专业的简历优化专家。请优化以下简历内容，使其更加专业、清晰、有吸引力。

原始简历内容：
{resume_content}
"""
        
        if job_description:
            base_prompt += f"""

目标职位描述：
{job_description}

请根据职位描述，有针对性地优化简历，突出相关技能和经验。
"""
        
        base_prompt += """

请提供优化后的简历内容，并简要说明主要改进点。直接输出优化后的简历内容，不要添加额外的说明文字。"""
        
        return base_prompt

# 全局AI服务实例
ai_service = AIService()

