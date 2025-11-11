<!--
Sync Impact Report:
Version change: N/A → 1.0.0
Modified principles: N/A (initial creation)
Added sections: Core Principles (5), Technology Stack, Development Workflow, Governance
Removed sections: N/A
Templates requiring updates: ✅ N/A (initial creation)
Follow-up TODOs: None
-->

# Resume AI Optimizer Constitution

## Core Principles

### I. Local-First Architecture
所有核心功能必须支持本地部署和运行；依赖外部服务必须可配置且提供本地替代方案（如Ollama替代OpenAI）；数据存储在本地SQLite数据库，确保隐私和数据主权。

### II. One-Click Startup
项目必须提供一键启动脚本，支持开发和生产环境；所有依赖必须通过标准包管理器（pip/npm）安装；Docker Compose可选但推荐用于完整环境隔离。

### III. API-First Design
后端使用FastAPI构建RESTful API，提供OpenAPI文档；前端通过标准HTTP请求与后端通信；所有API端点必须包含输入验证和错误处理。

### IV. Test-First Development (NON-NEGOTIABLE)
关键功能必须包含单元测试和集成测试；测试覆盖率目标：核心业务逻辑≥80%；所有PR必须通过测试套件验证。

### V. Live Demo Ready
项目必须包含演示模式和示例数据；前端界面必须直观易用，支持实时预览；提供清晰的用户指南和API文档。

## Technology Stack

- **Backend**: Python 3.11+, FastAPI, SQLAlchemy, Pydantic
- **Frontend**: React 18+, TypeScript, Vite
- **Database**: SQLite (开发) / PostgreSQL (生产可选)
- **AI Engine**: Ollama (本地LLM) / OpenAI API (可选)
- **Deployment**: Docker Compose, 支持本地开发和生产部署

## Development Workflow

1. **环境设置**: 使用虚拟环境（venv/conda）隔离Python依赖；Node.js依赖通过npm/yarn管理
2. **代码规范**: 遵循PEP 8 (Python) 和ESLint (TypeScript/React) 规范
3. **版本控制**: 使用语义化版本控制；主分支保护，通过PR合并
4. **文档要求**: README必须包含安装、配置、启动说明；API文档自动生成（FastAPI Swagger）

## Governance

本宪章是项目的最高指导原则，所有开发决策必须符合这些原则。修改宪章需要：
1. 提出修改提案并说明理由
2. 获得项目维护者批准
3. 更新版本号（语义化版本）
4. 更新相关文档和模板

所有代码审查必须验证是否符合宪章原则。复杂性必须得到充分论证。

**Version**: 1.0.0 | **Ratified**: 2025-01-27 | **Last Amended**: 2025-01-27
