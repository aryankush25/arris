import reflex as rx
from arris.protected import require_login
from arris.utils import ClientStorageState
from arris.schemas.shopify_store import get_stores
from typing import List
from arris.services.shopify import ShopifyService


class HomeState(ClientStorageState):
    data: List[dict] = []

    def get_data(self):
        email = self.get_email()

        self.data = get_stores(email)

    def handle_submit(self, form_data: dict):
        return ShopifyService.install_app(form_data["store_name"])


@rx.page(on_load=HomeState.get_data)
@require_login
def home() -> rx.Component:

    return rx.box(
        rx.button(
            "Logout",
            color_scheme="ruby",
            on_click=ClientStorageState.logout,
        ),
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Store Name"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Store Name",
                            type="name",
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a valid store name",
                        match="typeMismatch",
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="store_name",
            ),
            rx.form.submit(
                rx.button("Connect Shopify"),
                as_child=True,
            ),
            on_submit=HomeState.handle_submit,
        ),
        rx.box(
            rx.text("Stores"),
            padding_left="250px",
            padding_top="100px",
        ),
        rx.foreach(
            HomeState.data,
            lambda store, index: rx.box(
                rx.text(index + 1),
                rx.text(store["name"]),
                rx.chakra.link(
                    "Go to builder ->",
                    href=f"/builder/{store['name']}",
                ),
                padding_left="250px",
                class_name="border border-gray",
            ),
        ),
    )
