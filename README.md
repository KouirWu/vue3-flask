# 🤖 智能对话助手

<div align="center">

![Vue](https://img.shields.io/badge/Vue-3.0-4FC08D?style=flat-square&logo=vue.js&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-16+-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

一个基于Vue 3和Flask的智能对话应用，集成了SiliconFlow API，提供流畅的对话体验。

[功能特点](#功能特点) • [技术栈](#技术栈) • [快速开始](#快速开始) • [使用说明](#使用说明) • [常见问题](#常见问题)

</div>

## ✨ 功能特点

- 🎨 现代化的用户界面
- ⚡ 实时流式响应
- 💬 支持多轮对话
- 📱 响应式设计，适配各种设备

## 🛠️ 技术栈

### 前端
- Vue 3 - 渐进式JavaScript框架
- Element Plus - 基于Vue 3的组件库
- Vite - 下一代前端构建工具

### 后端
- Flask - Python Web框架
- OpenAI SDK - AI接口集成
- Flask-CORS - 跨域资源共享支持

## 📋 环境要求

- Node.js 16.0 或更高版本
- Python 3.8 或更高版本
- npm 或 yarn 包管理器

## 🚀 快速开始

### 1️⃣ 克隆项目

```bash
git clone https://github.com/KouirWu/vue3-flask.git
cd vue3-flask
```

### 2️⃣ 安装前端依赖

```bash
# 进入前端目录
cd src

# 安装依赖
npm install
# 或者使用 yarn
yarn install
```

### 3️⃣ 安装后端依赖

```bash
# 进入后端目录
cd backend

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 4️⃣ 配置环境变量

在 `backend` 目录下创建 `.env` 文件，添加以下内容：

```env
OPENAI_API_KEY=你的API密钥
```

## 🏃‍♂️ 运行项目

### 1️⃣ 启动后端服务

```bash
# 确保在backend目录下
cd backend

# 激活虚拟环境（如果还没激活）
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 启动Flask服务
python app.py
```

后端服务将在 http://localhost:5000 运行

### 2️⃣ 启动前端服务

```bash
# 在项目根目录下
cd src

# 启动开发服务器
npm run dev
# 或者使用 yarn
yarn dev
```

前端服务将在 http://localhost:5173 运行

## 📖 使用说明

1. 打开浏览器访问 http://localhost:5173
2. 在输入框中输入您的问题
3. 点击发送按钮或按回车键发送消息
4. 等待AI助手的回复

## ❓ 常见问题

### 🔄 跨域问题
确保后端服务正在运行，并且CORS配置正确。

### 🔑 API密钥错误
检查 `.env` 文件中的 API 密钥是否正确配置。

### 🔌 连接问题
确保后端服务在 http://localhost:5000 运行，并且没有其他程序占用该端口。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

<div align="center">
  <sub>Built with ❤️ by 季禾</sub>
</div> 