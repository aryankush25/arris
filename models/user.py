import reflex as rx
from sqlmodel import Field


class User(rx.Model, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, primary_key=True)
    username: str
    full_name: str
    email: str = Field(unique=True)
    password: str
