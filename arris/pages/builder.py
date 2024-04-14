import reflex as rx
from arris.services.shopify import get_store


class BuilderState(rx.State):
    data: dict = {}

    @rx.var
    def store_name(self) -> str:
        return self.router.page.params.get("store_name")

    def get_data(self):

        self.data = get_store(self.store_name)

        print(self.data)


# @rx.page(on_load=BuilderState.get_data)
def builder():
    return rx.heading(BuilderState.store_name)
