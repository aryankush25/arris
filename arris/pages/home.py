import reflex as rx
from arris.services.shopify import ShopifyService
from arris.protected import require_login
from arris.utils import ClientStorageState


class ShopifyRadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):
        return ShopifyService.install_app(form_data["store_name"])


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
            on_submit=ShopifyRadixFormSubmissionState.handle_submit,
        ),
    )
