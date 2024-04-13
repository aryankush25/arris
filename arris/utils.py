import reflex as rx
import jwt
from rxconfig import config


class ClientStorageState(rx.State):
    custom_cookie: str = rx.Cookie(
        max_age=86400,
        path="/",
        name="access_token",
    )

    def get_email(self):
        if not self.custom_cookie:
            return None

        payload = jwt.decode(
            self.custom_cookie,
            config.jwt_secret,
            algorithms=["HS256"],
        )

        return payload["email"]

    def generate_token(self, email: str):
        return jwt.encode(
            {"email": email},
            config.jwt_secret,
            algorithm="HS256",
        )

    def logout(self):
        yield [rx.remove_cookie("access_token"), rx.redirect("/login")]
