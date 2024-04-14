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

    return rx.fragment(
        rx.cond(
            ClientStorageState.is_hydrated,
            rx.cond(
                ClientStorageState.custom_cookie,
                rx.fragment(
                    rx.chakra.link("Home", href="/home"),
                    rx.button(
                        "Logout",
                        color_scheme="ruby",
                        on_click=ClientStorageState.logout,
                    ),
                ),
                rx.chakra.link("Login", href="/login"),
            ),
            rx.chakra.center(
                rx.chakra.spinner(),
            ),
        )
    )
