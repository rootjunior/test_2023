from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = "8000"
    debug: bool = True
    worcers_count: int = 1
    use_timezone: bool = True
    redis_port: int = 6379
    redis_host: str = "redis"


settings = Settings()
