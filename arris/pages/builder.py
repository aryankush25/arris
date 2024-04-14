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
    raw_products: list = []

    # page_title: str = ""
    selected_product: dict = {}
    is_product_selected: bool = False

    is_generating_page: bool = False

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    def get_data(self):
        self.data = get_store(self.store_name)
        self.pages = get_store_pages(self.data.id)
        self.get_products()

    def createPage(self):

        # page_title = self.page_title
        selected_product = self.selected_product

        # print("Creating Page", page_title, selected_product)

        # if page_title == "":
        #     return rx.window_alert("Please enter a valid page title")

        if self.is_product_selected == False:
            return rx.window_alert("Please select a product")

        self.clear_selected()

        self.is_generating_page = True

        selected_raw_product = next(
            (
                product
                for product in self.raw_products
                if product["id"] == selected_product["id"]
            ),
            None,
        )

        print("Selected Raw Product", selected_raw_product)

        html = generate_html_for_products(
            selected_product["title"],
            selected_product["image"],
            selected_product["desc"],
            selected_product["price"],
            self.store_name,
            selected_raw_product,
        )

        self.is_generating_page = False

        return ShopifyPageService.create_page(
            self.store_name,
            selected_product["title"],
            html,
        )

    def get_products(self):
        products = get_shopify_products(self.store_name)

        for product in products:
            self.raw_products.append(
                {
                    "id": product.id,
                    "title": product.title,
                    "body_html": product.body_html,
                    "vendor": product.vendor,
                    "product_type": product.product_type,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at,
                    "tags": product.tags,
                    "variants": [
                        {
                            "id": variant.id,
                            "title": variant.title,
                            "price": variant.price,
                            "sku": variant.sku,
                            "inventory_management": variant.inventory_management,
                        }
                        for variant in product.variants
                    ],
                    "images": [
                        {
                            "id": image.id,
                            "src": image.src,
                            "alt": image.alt,
                        }
                        for image in product.images
                    ],
                }
            )

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

        # print("Products", self.products)

    def set_selected_product(self, product):
        self.selected_product = product
        self.is_product_selected = True
        print("Selected Product", self.selected_product)

    def clear_selected_product(self):
        self.selected_product = {}
        self.is_product_selected = False

    # def on_change(self, value):
    #     self.page_title = value

    def clear_selected(self):
        self.selected_product = {}
        self.is_product_selected = False
        # self.page_title = ""


@rx.page(on_load=BuilderState.get_data, route="/builder/[store_name]")
@require_login
def builder() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.image(
                        src="/company_logo.png",
                        alt="Descriptive text about the image",
                        height="45px",
                        width="45px",
                    ),
                    rx.text("ARRIS", class_name="text-2xl font-bold text-black"),
                    class_name="w-full flex gap-2 items-center",
                ),
                class_name="flex flex-col gap-1",
            ),
            rx.cond(
                BuilderState.is_generating_page,
                rx.text("Generating page..."),
                rx.dialog.root(
                    rx.dialog.trigger(
                        rx.button(
                            "Generate new page",
                            height="40px",
                            background_color="black",
                            color="white",
                            cursor="pointer",
                        )
                    ),
                    rx.dialog.content(
                        rx.dialog.title("Generate new page using AI"),
                        rx.dialog.description(
                            "Select a product to generate a new page using AI",
                            size="2",
                            margin_bottom="16px",
                        ),
                        # rx.dialog.description(
                        #     "Enter the page title and select a product to generate a new page using AI",
                        #     size="2",
                        #     margin_bottom="16px",
                        # ),
                        # rx.flex(
                        #     rx.text(
                        #         "Title",
                        #         as_="div",
                        #         size="2",
                        #         margin_bottom="4px",
                        #         weight="bold",
                        #     ),
                        #     rx.input(
                        #         value=BuilderState.page_title,
                        #         on_change=BuilderState.on_change,
                        #         placeholder="Enter the page title",
                        #     ),
                        #     direction="column",
                        #     spacing="3",
                        #     margin_bottom="12px",
                        # ),
                        rx.cond(
                            BuilderState.is_product_selected,
                            rx.flex(
                                rx.box(
                                    rx.text(
                                        "Selected product",
                                        as_="div",
                                        size="2",
                                        weight="bold",
                                    ),
                                    rx.text(
                                        "Reset",
                                        as_="span",
                                        size="2",
                                        color_scheme="blue",
                                        class_name="cursor-pointer text-blue",
                                        on_click=BuilderState.clear_selected_product(),
                                    ),
                                    class_name="flex gap-2 items-center justify-between w-full",
                                ),
                                rx.box(
                                    rx.image(
                                        src=BuilderState.selected_product["image"],
                                        width="100px",
                                        height="auto",
                                    ),
                                    rx.text(
                                        BuilderState.selected_product["title"],
                                        align="center",
                                    ),
                                    class_name=f"border border-blue cursor-pointer flex flex-col justify-center items-center gap-2 rounded p-2",
                                ),
                                direction="column",
                                spacing="3",
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
                                            on_click=BuilderState.set_selected_product(
                                                product
                                            ),
                                            class_name=f"border border-blue cursor-pointer flex flex-col justify-center items-center gap-2 rounded p-2",
                                        ),
                                    ),
                                    columns="3",
                                    spacing="4",
                                    width="100%",
                                ),
                                direction="column",
                                spacing="3",
                            ),
                        ),
                        rx.flex(
                            rx.dialog.close(
                                rx.button(
                                    "Cancel",
                                    color_scheme="gray",
                                    variant="soft",
                                    on_click=BuilderState.clear_selected,
                                ),
                            ),
                            rx.button(
                                "Create",
                                on_click=BuilderState.createPage,
                                background_color="black",
                                color="white",
                                cursor="pointer",
                            ),
                            spacing="3",
                            margin_top="16px",
                            justify="end",
                        ),
                    ),
                ),
            ),
            class_name="flex w-full mt-12 justify-between items-center",
        ),
        rx.box(
            rx.image(
                src="/back_arrow.svg",
                alt="Descriptive text about the image",
                height="25px",
                width="25px",
            ),
            rx.text(
                BuilderState.data["name"],
                class_name="text-xl font-bold text-black",
            ),
            class_name="flex gap-4 items-center cursor-pointer",
            on_click=lambda: rx.redirect(f"/home"),
        ),
        rx.cond(
            BuilderState.pages,
            rx.box(
                rx.foreach(
                    BuilderState.pages,
                    lambda page: rx.box(
                        rx.box(
                            rx.text(
                                page["title"],
                                class_name="text-lg font-bold flex-1",
                            ),
                            rx.chakra.link(
                                "View pages",
                                href=f"/builder/{BuilderState.store_name}/{page['id']}",
                                color="#4193F3",
                                display="flex",
                            ),
                            class_name="flex justify-between items-center gap-4",
                        ),
                        rx.html(page["body_html"]),
                        class_name="border border-gray w-[400px] p-4 h-[400px] overflow-y-auto flex flex-col gap-4",
                    ),
                ),
                class_name="flex gap-6 px-4 md:px-0 flex-col mx-auto md:flex-row items-center flex-wrap justify-start pb-16",
            ),
            rx.box(
                rx.image(src="/empty.avif", class_name="w-[400px] h-[300px]"),
                rx.box(
                    "No pages found. Generate a new page using AI.",
                    class_name="mt-6 font-semibold text text-xl text-center mx-auto",
                ),
                class_name="flex flex-col justify-center items-center",
            ),
        ),
        class_name="max-w-7xl flex-col flex gap-6 mx-auto h-screen w-full px-4",
    )
