from pydantic_settings import SettingsConfigDict, BaseSettings

from models import Post


class Settings(BaseSettings):
    TEST_POSTGRES_USER: str
    TEST_POSTGRES_PASSWORD: int
    TEST_POSTGRES_HOST: str
    TEST_POSTGRES_PORT: int
    TEST_POSTGRES_DB: str

    def gen_postgres_dsn(self, driver: str):
        return "postgresql+{}://{}:{}@{}:{}/{}".format(
            driver,
            self.TEST_POSTGRES_USER, self.TEST_POSTGRES_PASSWORD,
            self.TEST_POSTGRES_HOST, self.TEST_POSTGRES_PORT,
            self.TEST_POSTGRES_DB
        )

    @property
    def dsn(self):
        return self.gen_postgres_dsn("asyncpg")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


test_settings = Settings()

DUMMIES = [
    {"title": "Hello world!", "author_id": 69},
    {"title": "Hello again.", "author_id": 69},
    {"title": "Another author!", "author_id": 70}
]
