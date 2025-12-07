# 🚀 IntegrationRetellAI

A full-stack platform integrating **Retell AI** with a **Python + PostgreSQL** backend and a **React** frontend.  
The system consists of two independent backend services — **AdminPage** and **UserManager** — plus a modern frontend interface.

---

## 🌟 Features

- 🔗 **Retell AI Integration**
- 🧩 **Modular Multi-Service Architecture**
- 🔒 **Role-Based Admin Authorization**
- 👤 **User & Tenant Management**
- ⚡ **Webhook-Driven AI Call Processing**
- 🐳 **Docker Orchestration**
- 🗄️ **PostgreSQL Database**
- 🎨 **React Frontend**

---

## 🧰 Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![RetellAI](https://img.shields.io/badge/RetellAI-Integrated-purple)

## 🔧 Back-End Setup

### 1. Create and Run PostgreSQL via Docker

``` bash
docker run --name postgres   -e POSTGRES_PASSWORD=password123   -p 5432:5432   -d postgres
```

### 2. Start ngrok for Port 4000

``` bash
ngrok http 4000
```

### 3. Set Webhook URL in UserManager

    WEBHOOK_URL=<your-ngrok-url>

### 4. Create Retell AI Account and API Key

Add your key to `UserManager/.env`:

    RETELL_API_KEY=<your-retell-api-key>

### 5. Install, Build & Run AdminPage
in AdminPage folder
``` bash
bin/poetry install
docker compose build
docker compose up
```

### 6. Install, Build & Run UserManager
in UserManager folder
``` bash
bin/poetry install
docker compose build
docker compose up
```

### 7. Create First Admin User Manually

Connect to `admin_page` DB and create: - first admin role\
- permissions\
- admin user

## 💻 Front-End Setup

``` bash
npm install
npm run dev
```

## 📁 Project Structure

    root/
     ├─ admin_page/
     ├─ user_manager/
     ├─ frontend/
     ├─ docker-compose.yml
     └─ README.md

## 🧩 Summary of All Steps

-   Create PostgreSQL Docker instance
-   Start ngrok on port 4000
-   Set webhook URL in UserManager
-   Create Retell AI account and API key
-   Store API key in environment
-   Install + build + run AdminPage
-   Install + build + run UserManager
-   Connect to DB and create admin role & user
-   Run frontend with npm
