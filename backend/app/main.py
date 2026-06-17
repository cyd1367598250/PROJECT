from fastapi import FastAPI
from app.api.router import api_router

app=FastAPI(            #创建一个FastAPI应用实例
    title="AI Interview Coach API",
    description="AI 面试助手后端服务",
    version="0.1.0"
)           

app.include_router(api_router,prefix="/api")

@app.get("/health")
def health_check():
    return {"status":"ok"}
