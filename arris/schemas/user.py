import reflex as rx
from models import User


def get_users(self):
    with rx.session() as session:
        self.users = session.exec(
            User.select.where(User.username.contains(self.name)).all()
        )


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
