import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_jwt_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///database.db")  # Change to PostgreSQL in prod
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret_key")

config = Config()
