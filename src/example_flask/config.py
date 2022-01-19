from pydantic import BaseSettings


class LogSettings(BaseSettings):
    DATEFMT: str = "%Y-%m-%d %H:%M:%S %z"
    FORMAT: str = "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
    LEVEL: str = "WARNING"

    class Config:
        env_prefix = "LOG_"


class Settings(BaseSettings):
    logging: LogSettings = LogSettings()
