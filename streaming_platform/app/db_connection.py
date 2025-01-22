from motor.motor_asyncio import AsyncIOMotorClient
import logging
from elasticsearch import (
  AsyncElasticsearch,
  TransportError
)
from redis import asyncio as aioredis

logger = logging.getLogger("uvicorn.error")
mongo_client = AsyncIOMotorClient("mongodb://admin:adminpassword@localhost:27017/")
#es_client = AsyncElasticsearch("http://localhost:9200")

es_client = AsyncElasticsearch(
    hosts=["https://localhost:9200"],
    http_auth=("elastic", "RYK3ay2AUYsWNCM+eJ8f"),
    verify_certs=False  # if using self-signed certs in dev
)

redis_client = aioredis.Redis(
  host="localhost",
  port=6379,
)

async def ping_mongo_db_server():
  try:
    await mongo_client.admin.command("ping")
    logger.info("Connected to MongoDB server")
  except Exception as e:
    logger.error(f"Failed to connect to MongoDB server: {e}")
    raise e
  
async def ping_elasticsearch_server():
  try:
    await es_client.info()
    logger.info("Connected to Elasticsearch server")
  except TransportError as e:
    logger.error(f"Failed to connect to Elasticsearch server: {e}")
    raise e
  
async def ping_redis_server():
  try:
    await redis_client.ping()
    logger.info("Connected to Redis")
  except Exception as e:
    logger.error(f"Error connecting to Redis: {e}")
    raise e