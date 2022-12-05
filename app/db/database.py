"""
Database
"""
import pymongo
from pymongo.server_api import ServerApi

from app.config.database import get_db_settings

db_settings = get_db_settings()

client = pymongo.MongoClient(
    db_settings.database_url, server_api=ServerApi("1")
)

db = client[db_settings.mongo_db]
User = db.users
User.create_index([("email", pymongo.ASCENDING)], unique=True)
