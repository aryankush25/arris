import reflex as rx
from arris.component.landing import herosection

def index() -> rx.Component:
    return rx.box(
        herosection()
    )
