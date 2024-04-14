import reflex as rx
from models import User
from sqlmodel import select


def get_user(email: str):
    with rx.session() as session:
        user = session.exec(select(User).where(User.email == email)).first()

        return user


def add_user(
    email: str,
    full_name: str,
    password: str,
):
    with rx.session() as session:
        session.add(
            User(
                email=email,
                full_name=full_name,
                password=password,
            )
        )
        session.commit()
