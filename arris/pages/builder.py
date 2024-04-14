import reflex as rx
from arris.services.shopify import get_store
from arris.protected import require_login
from arris.utils import ClientStorageState
from arris.services.shopify_page import ShopifyPageService
from arris.schemas.shopify_page import get_store_pages
from arris.services.shopify import get_shopify_products
from arris.services.openai import get_completion


class BuilderState(ClientStorageState):
    data: dict = {}
    pages: list[dict] = []

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    def get_data(self):
        self.data = get_store(self.store_name)
        self.pages = get_store_pages(self.data.id)

    def createPage(self, form_data: dict):

        page_title = form_data["page_title"]
        html = "<h1>ARRIS</h1>"

        if page_title == "":
            return rx.window_alert("Please enter a valid page title")

        return ShopifyPageService.create_page(
            self.store_name,
            page_title,
            html,
        )
        
    def get_products(self):
        return get_shopify_products(self.store_name)

    def open_ai_chat(self):
        return get_completion("Hello, how are you?")

@rx.page(on_load=BuilderState.get_data, route="/builder/[store_name]")
@require_login
def builder() -> rx.Component:
    return rx.box(
        rx.heading("Builder Page"),
        rx.heading(BuilderState.data["name"]),
        rx.button(
            "Products",
            color_scheme="ruby",
            on_click=BuilderState.open_ai_chat,
        ),
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Page Title"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Page Title",
                            type="name",
                        ),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="page_title",
            ),
            rx.form.submit(
                rx.button("Create Page"),
                as_child=True,
            ),
            on_submit=BuilderState.createPage,
        ),
        rx.foreach(
            BuilderState.pages,
            lambda page, index: rx.box(
                rx.text(index + 1),
                rx.text(page["title"]),
                rx.html(page["body_html"]),
                rx.chakra.link(
                    "Go to builder page ->",
                    href=f"/builder/{BuilderState.store_name}/{page['id']}",
                ),
                padding_left="250px",
                class_name="border border-gray",
            ),
        ),
    )
