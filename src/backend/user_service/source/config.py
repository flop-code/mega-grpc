from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

    GRPC_HOST: str
    GRPC_PORT: str

    REDIS_HOST: str
    REDIS_PORT: int

    FRONTEND_URL: str
    COOKIE_AGE: int
    COOKIE_PARAMS: dict = {"secure": False, "samesite": "none", "httponly": True}

    def gen_postgres_dsn(self, driver: str):
        return "postgresql+{}://{}:{}@{}:{}/{}".format(
            driver,
            self.POSTGRES_USER, self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST, self.POSTGRES_PORT,
            self.POSTGRES_DB
        )

    @property
    def dsn(self):
        return self.gen_postgres_dsn("asyncpg")

    @property
    def alembic_dsn(self):
        return self.gen_postgres_dsn("psycopg2")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
