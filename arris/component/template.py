import reflex as rx

def templates() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                "Some of our Templates",
                class_name="font-semibold text-[32px] text-[#4193F3]"
            ),
            rx.box(
            rx.box(
                rx.image(
                    src="/template.png",
                    alt="Descriptive text about the image",
                    box_size="400px",
                ),
                class_name="h-[725px] object-contain"
            ),
            rx.box(
                rx.image(
                    src="/template2.png",
                    alt="Descriptive text about the image",
                    box_size="400px",
                ),
                class_name="h-[960px] object-contain"
            ),
            rx.box(
                rx.image(
                    src="/template3.png",
                    alt="Descriptive text about the image",
                    box_size="400px",  
                ),
                class_name="h-[740px] object-contain"
            ),
            class_name="flex justify-between gap-2"
        ),
        class_name="flex flex-col gap-16 justify-center items-center"
        ),
        class_name="flex justify-between w-full mt-20 max-w-7xl mx-auto"
    )
