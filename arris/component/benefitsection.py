import reflex as rx

def benefitssection() -> rx.Component:
    return rx.box(
        rx.box(
            "What Benefit Will You Get",
            class_name="font-bold text-[32px]"
        ),
        rx.box(),
        class_name="max-w-7xl w-full flex flex-col gap-8"
    )