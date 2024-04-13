"""The main index page."""

import reflex as rx
from arris.utils import ClientStorageState


def index() -> rx.Component:

    return rx.box(
        rx.button(
            "Logout",
            color_scheme="ruby",
            on_click=ClientStorageState.logout,
        ),
        rx.button(
            "Decrement",
            color_scheme="ruby",
        ),
        rx.box(
            margin_top="calc(50px + 2em)",
            padding="2em",
        ),
        padding_left="250px",
        padding_top="100px",
    )
