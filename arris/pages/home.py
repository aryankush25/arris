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
            rx.box(
                rx.box(
                rx.image(
                    src="/company_logo.png",
                    alt="Descriptive text about the image",
                    height="45px",
                    width="45px",
                ),
                rx.text("ARRIS",font_family="Integral CF",class_name="text-2xl font-bold text-black"),
                class_name="w-full flex gap-2 items-center",
                ),
                rx.box(
                    rx.button(
                        "Logout",
                        on_click=ClientStorageState.logout,
                        height="44px",
                        background_color="#FF5C5C", 
                        color="white",
                        cursor="pointer"
                    ),
                    class_name="items-center"

                ),
            class_name="flex justify-between items-center w-full md:mt-14 mt-8 px-4 max-w-7xl mx-auto"
            ),
            rx.box(
                rx.box(
                    rx.image(
                    src="/shopify.png",
                    alt="Descriptive text about the image",
                    height="60px",
                    width="60px",
                    ),
                    rx.text("Connect your Shopify Store",class_name="text-lg font-bold text-black"),
                    class_name="w-full flex gap-2 justify-center items-center",
                ),
                rx.form.root(
                    rx.form.field(
                        rx.flex(
                            rx.form.control(
                                rx.input.input(
                                    placeholder="Store Name",
                                    type="name",
                                    height="44px",
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
                        width="100%",
                    ),
                    rx.form.submit(
                        rx.button("Connect", height="44px", background_color="black", color="white", cursor="pointer"),
                        as_child=True,
                    ),
                    on_submit=HomeState.handle_submit,
                    width="430px",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    gap="8px",
                    box_shadow="4px Grey/Light 3"
                ),
                class_name="flex flex-col gap-6 justify-center items-center w-full md:mt-14 mt-8 px-4 max-w-7xl mx-auto"
            ),
            rx.box(
                rx.text("Store List",class_name="text-2xl font-bold text-black"),
                rx.box(
                    rx.foreach(
                        HomeState.data,
                        lambda store, index: rx.box(
                        rx.text(store["name"], class_name="text-lg font-bold"),
                        rx.image(
                            src="/store.png",
                            alt="Descriptive text about the image",
                            height="100%",
                            max_height="180px",
                            width="100%",
                        ),
                        rx.chakra.link(
                            "View Pages",
                            href=f"/builder/{store['name']}",
                            color="#4193F3",
                            display="flex",
                            flex_direction="row-reverse",
                            
                        ),
                        class_name="border rounded-lg p-2 flex flex-col gap-4 w-full max-w-[250px] h-[250px] border-gray",
                        # on_click=lambda store=store: rx.redirect(f"/builder/{store['name']}"),
                        ),
                    ),
                    class_name="flex flex-wrap max-w-7xl mb-16 mt-4 gap-10 justify-center items-center"
                ),
                class_name="flex flex-col gap-4 justify-center items-center w-full md:mt-14 mt-8 px-4 max-w-7xl mx-auto"
            ),
        class_name="min-h-screen w-full flex gap-4 flex-col bg-[#F4FAFF]"
    )
