from argon2 import PasswordHasher
from pydantic_settings import SettingsConfigDict, BaseSettings

from models import User


class Settings(BaseSettings):
    TEST_POSTGRES_USER: str
    TEST_POSTGRES_PASSWORD: int
    TEST_POSTGRES_HOST: str
    TEST_POSTGRES_PORT: int
    TEST_POSTGRES_DB: str

    TEST_REDIS_HOST: str
    TEST_REDIS_PORT: int

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

PASSWORD = "helloWORLD123"
PASS_HASH = PasswordHasher().hash(PASSWORD)
DUMMIES = [
    {"username": "dummy1", "phone_number": "380123456789",
     "address": "Ukraine, Kyiv, Khreschatyk st., 57, 02000"},
    {"username": "dummy2", "phone_number": "380123456879",
     "address": "Ukraine, Kyiv, Khreschatyk st., 58, 02000"},
    {"username": "dummy3", "phone_number": "380123456897",
     "address": "Ukraine, Kyiv, Khreschatyk st., 59, 02000"},
]
