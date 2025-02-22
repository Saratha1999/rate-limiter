import time
import redis
from fastapi import FastAPI, HTTPException, Depends


app = FastAPI()

@app.get("/")
def home():
    return {"Welcome to Rate limiter"}

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

# Define Rate Limit Parameters
rate_limit = 5
time_limit =10

token_bucket_capcity = 5
token_bucket_refill_rate = 1

def token_bucket_limiter():
    key = "token_bucket" #redis key which store the avalibale number of tokens
    tokens= int(redis_client.get(key) or token_bucket_capcity )

    last_refill = float (redis_client.get(f"{key}:last_refill") or time.time())

    #refill token based on time passed
    now = time.time()
    refill = int (( now - last_refill) * token_bucket_refill_rate)
    tokens = min(token_bucket_capcity, tokens+refill)

    redis_client.set(key, tokens)
    redis_client.set(f"{key}:last_refill", now)

    if tokens > 0:
        redis_client.decr(key)
    else:
        raise HTTPException(status_code=429, detail="Rate limit exceeded (Token Bucket)")

@app.get("/token-bucket")
def token_based_request(tocken_bucket: str = Depends(token_bucket_limiter) ):
    return {"message" : "Request accepted (Token Bucket)"}

def fixed_window_limiter():

    key = f"Fixed window: {(int(time.time()//time_limit))}" #divides time into fixed 10-second windows and converts it to an integer.

    count = int(redis_client.get(key) or 0)

    if count >= rate_limit:
        raise HTTPException(status_code =429, detail = " Rate limit exceeded (Fixed window)")
    
    redis_client.incr(key)
    redis_client.expire(key, time_limit)

@app.get("/fixed-window")
def fixed_window_request(fixed_window: str = Depends (fixed_window_limiter)):
    return{"message": "Request accepted(Fixed window)"}


def sliding_window():
    key= "Sliding window"
    current_time = time.time()

    redis_client.zremrangebyscore(key, 0, current_time - time_limit)  #Deletes old requests that exceed the time window

    count = redis_client.zcard(key)  #how many valid requests still exist after old ones are removed.

    if count >= rate_limit:
        raise HTTPException(status_code = 429, detail = " Rate limit exceeded (sliding window)")
    

    redis_client.zadd(key, {current_time:current_time}) #request timestamp is added to Redis.


@app.get("/sliding-window")
def sliding_window_request(sliding_window: str = Depends(sliding_window)):
    return {"message": "Request accepted (Sliding window)" }




