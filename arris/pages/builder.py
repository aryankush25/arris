import reflex as rx
from arris.services.shopify import get_store
from arris.protected import require_login
from arris.utils import ClientStorageState
from arris.services.shopify_page import ShopifyPageService
from arris.schemas.shopify_page import get_store_pages
from arris.services.shopify import get_shopify_products
from arris.services.openai import generate_html_for_products


class BuilderState(ClientStorageState):
    data: dict = {}
    pages: list[dict] = []
    products: list[dict] = []

    page_title: str = ""
    selected_product: dict = {}

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    def get_data(self):
        self.data = get_store(self.store_name)
        self.pages = get_store_pages(self.data.id)
        self.get_products()

    def createPage(self):

        page_title = self.page_title
        selected_product = self.selected_product

        if page_title == "":
            return rx.window_alert("Please enter a valid page title")

        self.page_title = ""
        self.selected_product = {}

        html = generate_html_for_products(
            selected_product["title"],
            selected_product["image"],
            selected_product["desc"],
            selected_product["price"],
        )

        return ShopifyPageService.create_page(
            self.store_name,
            page_title,
            html,
        )

    def get_products(self):
        products = get_shopify_products(self.store_name)

        for product in products:
            # print(f"Product ID: {product.id}")
            # print(f"Title: {product.title}")
            # if len(product.images) > 0:
            #     print(f"Images: {product.images[0].src}")
            # print(f"Desc: {product.body_html}")
            # print(f"Price: {product.variants[0].price}")

            self.products.append(
                {
                    "id": product.id,
                    "title": product.title,
                    "image": product.images[0].src if len(product.images) > 0 else "",
                    "desc": product.body_html if product.body_html else "",
                    "price": (
                        product.variants[0].price if len(product.variants) > 0 else ""
                    ),
                }
            )

        print("Products", self.products)

        return products

    def set_selected_product(self, product):
        self.selected_product = product
        print("Selected Product", self.selected_product)

    def is_selected_product(self, product):
        return "" if self.selected_product != product else "border-2"


@rx.page(on_load=BuilderState.get_data, route="/builder/[store_name]")
@require_login
def builder() -> rx.Component:
    return rx.box(
        rx.heading("Builder Page"),
        rx.heading(BuilderState.data["name"]),
        rx.dialog.root(
            rx.dialog.trigger(rx.button("Generate new page")),
            rx.dialog.content(
                rx.dialog.title("Generate new page using AI"),
                rx.dialog.description(
                    "Enter the page title and select a product to generate a new page using AI",
                    size="2",
                    margin_bottom="16px",
                ),
                rx.flex(
                    rx.text(
                        "Title",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.input(
                        bind=BuilderState.page_title,
                        placeholder="Enter the page title",
                    ),
                    direction="column",
                    spacing="3",
                    margin_bottom="12px",
                ),
                rx.flex(
                    rx.text(
                        "Choose a product",
                        as_="div",
                        size="2",
                        margin_bottom="4px",
                        weight="bold",
                    ),
                    rx.grid(
                        rx.foreach(
                            BuilderState.products,
                            lambda product: rx.box(
                                rx.image(
                                    src=product["image"],
                                    width="100px",
                                    height="auto",
                                ),
                                rx.text(
                                    product["title"],
                                    align="center",
                                ),
                                on_click=BuilderState.set_selected_product(product),
                                class_name=f"border border-blue cursor-pointer flex flex-col justify-center items-center gap-2 rounded p-2 {BuilderState.is_selected_product(product)}",
                                # border=BuilderState.is_selected_product(product),
                            ),
                        ),
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    direction="column",
                    spacing="3",
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancel",
                            color_scheme="gray",
                            variant="soft",
                        ),
                    ),
                    rx.dialog.close(
                        rx.button("Create", on_click=BuilderState.createPage),
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
            ),
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
