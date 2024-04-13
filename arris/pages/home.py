import reflex as rx
from arris.services.shopify import ShopifyService
from arris.protected import require_login
from arris.utils import ClientStorageState


# @rx.page(on_load=IndexLoadState.get_data)
@require_login
def home() -> rx.Component:

    return rx.box(
        rx.button(
            "Logout",
            color_scheme="ruby",
            on_click=ClientStorageState.logout,
        ),
        rx.button(
            "Connect Shopify Store",
            color_scheme="ruby",
            on_click=ShopifyService.install_app("xg-dev"),
        ),
    )
