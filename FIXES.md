# FIXES.md – DevOps Stage 2

## 1. Redis Connection Issue (Critical Fix)
- File: worker/worker.py
- Problem: Redis host was set to "localhost"
- Why it failed: Containers cannot use localhost to reach other services
- Fix: Changed host to "redis" to enable Docker service discovery

---

## 2. Docker Build Context Error
- Problem: Incorrect build path used during image creation
- Fix: Used correct context (".") inside each service directory

---

## 3. Worker Failure Due to Network Isolation
- Problem: Worker could not resolve Redis hostname
- Cause: Running containers separately using docker run
- Fix: Migrated system to docker-compose for shared networking

---

## 4. WSL Docker Integration Issue
- Problem: docker-compose not recognized in WSL terminal
- Fix: Enabled Docker Desktop WSL integration and restarted Docker

---

## 5. Microservices Communication Fix
- Problem: API, Worker, and Redis were not on same network
- Fix: Implemented docker-compose.yml to unify services
