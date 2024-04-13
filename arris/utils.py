import reflex as rx


class ClientStorageState(rx.State):
    custom_cookie: str = rx.Cookie(
        max_age=86400,
        path="/",
        name="access_token",
    )

    def logout(self):
        return rx.remove_cookie("access_token")
