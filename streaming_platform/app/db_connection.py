from motor.motor_asyncio import AsyncIOMotorClient
import logging

logger = logging.getLogger("uvicorn.error")
mongo_client = AsyncIOMotorClient("mongodb://admin:adminpassword@localhost:27017/")

async def ping_mongo_db_server():
  try:
    await mongo_client.admin.command("ping")
    logger.info("Connected to MongoDB server")
  except Exception as e:
    logger.error(f"Failed to connect to MongoDB server: {e}")
    raise e