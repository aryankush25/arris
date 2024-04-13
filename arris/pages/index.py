"""The main index page."""

import reflex as rx


def index() -> rx.Component:

    return rx.box(
        rx.text("Welcome to Arris"),
        padding_left="250px",
        padding_top="100px",
    )
