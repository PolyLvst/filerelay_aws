from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    app_name: str = "File Relay AWS"
    version: str = "1.0.0"

    AWS_BUCKET: str

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'