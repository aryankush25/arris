import reflex as rx
from arris.services.shopify import get_store
from arris.protected import require_login
from arris.services.shopify_page import ShopifyPageService
from arris.utils import ClientStorageState
from arris.schemas.shopify_page import get_store_page_by_id


class BuilderPageState(ClientStorageState):
    data: dict = {}
    is_fetching: bool = False
    html: str = "<div></div>"

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    @rx.var
    def page_id(self) -> str:
        return self.router.page.params.get("page_id")

    def get_data(self):
        self.is_fetching = True
        print("self.store_name", self.store_name)
        print("self.page_id", self.page_id)

        store_data = get_store(self.store_name)
        print("store_data", store_data)

        data = get_store_page_by_id(self.page_id)

        self.html = data.body_html
        self.is_fetching = False
        self.data = data

        print("self.data", self.data)

    def handle_change(self, html: str):
        self.html = html


@rx.page(on_load=BuilderPageState.get_data, route="/builder/[store_name]/[page_id]")
@require_login
def builder_page() -> rx.Component:

    return rx.cond(
        BuilderPageState.is_fetching,
        rx.chakra.center(
            rx.chakra.spinner(),
        ),
        rx.box(
            rx.heading("Builder Page"),
            rx.heading(BuilderPageState.data["title"]),
            rx.flex(
                rx.text_area(
                    placeholder="Type here...",
                    value=BuilderPageState.html,
                    on_change=BuilderPageState.handle_change,
                    border="1px dashed #ccc",
                    border_radius="4px",
                    width="100%",
                    height="600px",
                ),
                rx.box(
                    rx.html(BuilderPageState.html),
                    border="1px dashed #ccc",
                    border_radius="4px",
                    width="100%",
                    height="600px",
                ),
            ),
        ),
    )
