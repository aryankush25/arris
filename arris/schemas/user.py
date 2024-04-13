import reflex as rx
from models import User


class QueryUser(rx.State):
    name: str
    users: list[User]

    def get_users(self):
        with rx.session() as session:
            self.users = session.exec(
                User.select.where(User.username.contains(self.name)).all()
            )


class AddUser(rx.State):
    def add_user(self):
        with rx.session() as session:
            session.add(
                User(
                    username="aryan",
                    email="aryan@gluelabs.com",
                    full_name="Aryan",
                    password="1234",
                )
            )
            session.commit()
