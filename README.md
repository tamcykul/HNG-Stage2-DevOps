# 🚀 HNG Stage 2 DevOps – Microservices Job Processing System

## 📌 Project Overview

This project is a containerized microservices system that simulates a real-world **job processing pipeline**.

It demonstrates how modern backend systems work using:
- API service (FastAPI)
- Background worker service (Python)
- Redis queue (message broker)
- Docker + Docker Compose (container orchestration)

---

## 🧠 System Architecture

The system follows this flow:
Client → API → Redis Queue → Worker → Redis → API → Response


### Components:

### 1. API Service (FastAPI)
- Accepts job requests
- Stores job in Redis queue
- Returns job ID
- Provides job status endpoint

### 2. Redis (Message Broker)
- Stores job queue
- Acts as communication layer between API and worker

### 3. Worker Service (Python)
- Continuously listens to Redis queue
- Picks up jobs
- Processes them
- Updates job status to "completed"

---

## ⚙️ Technologies Used

- Python 3.11
- FastAPI
- Redis
- Docker
- Docker Compose
- Uvicorn
- Linux (WSL2 environment)

---

## 📦 Project Structure
hng14-stage2-devops/
│
├── api/
│ ├── main.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── worker/
│ ├── worker.py
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/ (optional service)
│
├── docker-compose.yml
├── README.md
├── FIXES.md


---

## 🚀 How to Run the Project

### Step 1: Clone Repository
git clone https://github.com/tamcykul/hng14-stage2-devops.git
cd hng14-stage2-devops
---

### Step 2: Start System with Docker Compose

This will start:
- API service on port 8000
- Redis container
- Worker service

---

## 🌐 Accessing the Application

### API Documentation (Swagger UI)
http://127.0.0.1:8000/docs


---

## 🧪 How to Test the System

### 1. Create a Job

Send a POST request:
POST /jobs

Response:
```json
{
  "job_id": "unique-id"
}

2. Check Job Status
GET /jobs/{job_id}
Response:
{
  "job_id": "unique-id",
  "status": "completed"
}

🔄 How the System Works Internally
User creates a job via API
API pushes job ID to Redis queue
Worker listens to Redis
Worker processes job
Worker updates job status
API returns updated status

🐳 Docker Setup
Build Services
docker compose build

Run Services
docker compose up

Stop Services
docker compose down

🧩 Key DevOps Concepts Demonstrated
Containerization (Docker)
Microservices architecture
Service communication via Redis
Background job processing
Non-root container security
Multi-service orchestration (Docker Compose)
Environment-based configuration
Health-based service startup (conceptual requirement)
