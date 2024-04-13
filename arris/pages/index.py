"""The main index page."""

import reflex as rx
from arris.navigation import navbar
from arris.services.shopify import ShopifyService
from arris.protected import require_login


# @rx.page(on_load=IndexLoadState.get_data)
@require_login
def index() -> rx.Component:

    return rx.box(
        navbar(heading="Dashboard"),
        rx.button(
            "Decrement",
            color_scheme="ruby",
            on_click=ShopifyService.install_app,
            # on_click=AddUser.add_user,
        ),
        rx.box(
            margin_top="calc(50px + 2em)",
            padding="2em",
        ),
        padding_left="250px",
        padding_top="100px",
    )
