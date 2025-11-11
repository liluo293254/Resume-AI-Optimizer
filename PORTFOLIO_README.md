# GitHub 作品集使用指南

## 📋 概述

已为您创建了一个现代化的 GitHub 作品集网站，并将 **AI 智能简历优化器** 项目添加到了作品集中。

## 📁 作品集位置

作品集文件位于 `portfolio/` 目录下：

```
portfolio/
├── index.html          # 主页面
├── styles.css          # 样式文件
├── script.js           # JavaScript 逻辑（包含项目数据）
├── README.md           # 作品集说明文档
├── DEPLOYMENT.md       # 部署指南
├── CUSTOMIZE.md        # 自定义指南
└── PORTFOLIO_SETUP.md  # 设置清单
```

## 🚀 快速开始

### 1. 本地预览

直接在浏览器中打开 `portfolio/index.html`，或使用本地服务器：

```bash
cd portfolio
python -m http.server 8000
# 然后访问 http://localhost:8000
```

### 2. 部署到 GitHub Pages

#### 方法 A: 使用 GitHub Actions (推荐)

1. 将代码推送到 GitHub 仓库
2. 在仓库设置中启用 GitHub Pages，选择 "GitHub Actions" 作为源
3. 工作流文件已配置在 `.github/workflows/deploy-portfolio.yml`
4. 每次推送代码到 `main` 分支时会自动部署

#### 方法 B: 手动部署

1. 在 GitHub 仓库设置中：
   - Settings → Pages
   - Source: 选择分支（如 `main`）
   - Folder: 选择 `/portfolio`
   - 保存

2. 访问: `https://yourusername.github.io/repository-name/`

## ✏️ 自定义内容

### 必须修改的内容

1. **更新项目链接** (`portfolio/script.js`):
   ```javascript
   demoUrl: "https://github.com/yourusername/resume-ai-optimizer",
   codeUrl: "https://github.com/yourusername/resume-ai-optimizer",
   ```
   将 `yourusername` 替换为您的 GitHub 用户名

2. **更新联系方式** (`portfolio/index.html`):
   - GitHub 链接 (约第 165 行)
   - Email 地址 (约第 170 行)
   - LinkedIn 链接 (约第 175 行)

3. **更新个人信息**:
   - 导航栏品牌名称
   - 首页标题和描述
   - "关于我"部分内容

### 可选自定义

- 修改颜色主题 (`styles.css`)
- 添加更多项目 (`script.js`)
- 更新技能标签 (`index.html`)
- 添加个人照片或 Logo

详细说明请查看 `portfolio/CUSTOMIZE.md`

## 📦 当前包含的项目

作品集已包含以下项目：

1. **AI 智能简历优化器** ⭐ (已添加)
   - 技术栈: Python, FastAPI, React, TypeScript, Ollama, SQLite
   - 描述: 基于 AI 技术的智能简历优化工具

2. **项目示例 2** (占位符，可删除或替换)
3. **项目示例 3** (占位符，可删除或替换)

## 🎨 作品集特性

- ✅ 现代化响应式设计
- ✅ 平滑滚动和动画效果
- ✅ 项目卡片展示
- ✅ 技能标签分类
- ✅ 联系方式集成
- ✅ 移动端友好
- ✅ 快速加载

## 📚 相关文档

- **README.md**: 作品集基本说明
- **DEPLOYMENT.md**: 详细的部署指南
- **CUSTOMIZE.md**: 完整的自定义指南
- **PORTFOLIO_SETUP.md**: 部署前检查清单

## 🔗 下一步

1. ✅ 查看 `portfolio/PORTFOLIO_SETUP.md` 完成检查清单
2. ✅ 自定义个人信息和项目链接
3. ✅ 本地测试作品集
4. ✅ 推送到 GitHub 并部署

## 💡 提示

- 作品集使用纯 HTML/CSS/JavaScript，无需构建步骤
- 所有资源都是静态的，可以轻松部署到任何静态网站托管服务
- 支持 GitHub Pages、Netlify、Vercel 等平台

---

**开始展示您的作品吧！** 🎉

如有问题，请查看 `portfolio/` 目录下的详细文档。

