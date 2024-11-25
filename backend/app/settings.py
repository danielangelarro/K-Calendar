import os
import inject
from pydantic import BaseSettings


def configure(binder):
    from app.infrastructure.repositories.user_repository import UserRepository
    from app.infrastructure.services.user_service import UserService
    from app.infrastructure.services.auth_service import AuthService
    from app.application.repositories.user_repository import IUserRepository
    from app.application.services.user_service import IUserService
    from app.application.services.auth_service import IAuthService

    binder.bind(IUserRepository, UserRepository())
    binder.bind(IUserService, UserService())
    binder.bind(IAuthService, AuthService())


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.sqlite")
    SECRET_KEY = os.getenv("SECRET_KEY", "tu_clave_secreta")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    class Config:
        env_file = ".env"


settings = Settings()
