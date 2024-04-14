import reflex as rx # type: ignore

def benefitssection() -> rx.Component:
    return rx.box(
        rx.box(
            "What Benefit Will You Get",
            class_name="font-bold text-[32px]"
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.image(
                        src="/checkbox.svg",
                    ),
                    rx.box(
                        rx.text(
                            "TIME-SAVING",
                            class_name="font-semibold text-xl"
                        ),
                        rx.text(
                            "Offer pre-designed templates and intuitive tools for creating a website quickly, eliminating the need for coding and designing from scratch.",
                            class_name="text-[#6C6C72]"
                        ),
                        class_name="flex flex-col gap-2"
                    ),
                    class_name="flex p-5 gap-4 items-start rounded-xl bg-white shadow-md max-w-[568px]"
                ),
                rx.box(
                    rx.image(
                        src="/checkbox.svg",
                    ),
                    rx.box(
                        rx.text(
                            "CUSTOMIZATION OPTIONS",
                            class_name="font-semibold text-xl"
                        ),
                        rx.text(
                            "Easy setup and customization options for a unique website. Personalize colors, fonts, layouts, and more to match your brand identity and specific needs.",
                            class_name="text-[#6C6C72]"
                        ),
                        class_name="flex flex-col gap-2"
                    ),
                    class_name="flex p-5 gap-4 items-start rounded-xl bg-white shadow-md max-w-[568px]"
                ),
                rx.box(
                    rx.image(
                        src="/checkbox.svg",
                    ),
                    rx.box(
                        rx.text(
                            "EASE OF USE",
                            class_name="font-semibold text-xl"
                        ),
                        rx.text(
                            "User-friendly interfaces and drag-and-drop functionality, allowing even those with limited technical expertise to create professional websites easily.",
                            class_name="text-[#6C6C72]"
                        ),
                        class_name="flex flex-col gap-2"
                    ),
                    class_name="flex p-5 gap-4 items-start rounded-xl bg-white shadow-md max-w-[568px]"
                ),
                class_name="flex flex-col gap-7"
            ),
            rx.image(
                src="/benefits.svg"
            ),
            class_name="flex items-center justify-between"
        ),
        class_name="max-w-7xl mt-28 w-full mx-auto flex flex-col gap-8"
    )