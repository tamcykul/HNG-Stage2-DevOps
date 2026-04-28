from fastapi import FastAPI
import redis
import os
import uuid

app = FastAPI()

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    decode_responses=True
)

# -------------------------
# CREATE JOB
# -------------------------
@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())

    # store as simple hash
    r.hset(f"job:{job_id}", mapping={
        "status": "queued"
    })

    return {
        "job_id": job_id,
        "status": "queued"
    }


# -------------------------
# GET JOB
# -------------------------
@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    job = r.hgetall(f"job:{job_id}")

    if not job:
        return {"error": "not found"}

    return {
        "job_id": job_id,
        "status": job.get("status", "unknown")
    }