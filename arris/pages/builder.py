import reflex as rx
from arris.services.shopify import get_store


class BuilderState(rx.State):
    store_name: str = ""
    data: dict = {}

    @rx.var
    def store_name(self) -> str:
        self.store_name = self.router.page.params.get("store_name")
        return self.store_name

    def get_data(self):

        self.data = get_store(self.store_name)

        print(self.data)


# @rx.page(on_load=BuilderState.get_data)
def builder():
    return rx.heading(BuilderState.store_name)
