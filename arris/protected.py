import reflex as rx
from arris.utils import ClientStorageState


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:

    def protected_page():
        return rx.cond(
            ClientStorageState.custom_cookie,
            page(),
            protected(),
        )

    protected_page.__name__ = page.__name__

    return protected_page


def not_require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:

    def protected_page():
        return rx.cond(
            ClientStorageState.custom_cookie,
            protected(),
            page(),
        )

    protected_page.__name__ = page.__name__

    return protected_page


def protected() -> rx.Component:

    return rx.chakra.vstack(
        rx.chakra.heading("Protected Page", font_size="2em"),
        rx.cond(
            ClientStorageState.custom_cookie,
            rx.fragment(
                rx.chakra.link("Home", href="/"),
                rx.chakra.link("Logout", href="/", on_click=ClientStorageState.logout),
            ),
            rx.chakra.link("Login", href="/login"),
        ),
    )
