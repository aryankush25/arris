import reflex as rx

def herosection() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    "Creating",
                    class_name="font-bold text-[rgba(21, 23, 26, 1)] text-5xl"
                ),
                rx.box(
                    "Websites",
                    class_name="font-bold text-[rgba(21, 23, 26, 1)] text-5xl"
                ),
                rx.box(
                    "without Code",
                    rx.image(
                        src="/line.png",
                        alt="Descriptive text about the image",
                        box_size="400px",
                        max_width="50%"
                    ),
                    class_name="flex flex-col gap-1 font-bold text-[rgba(21, 23, 26, 1)] text-5xl"
                ),
                rx.box(
                    "Hassle",
                    class_name="font-bold text-[rgba(21, 23, 26, 1)] text-5xl"
                ),
                rx.box(
                    rx.box(
                    "Explore a new AI-powered approach to",
                    class_name="font-medium text-[rgba(21, 23, 26, 1)] text-base"
                ),
                rx.box(
                    "website and UI element design.",
                    class_name="font-medium text-[rgba(21, 23, 26, 1)] text-base"
                ),
                class_name="flex flex-col"
                ),
                rx.box(
                    rx.box(
                        "Get Started",
                        class_name="border border-black rounded-lg text-base items-center justify-center text-white bg-black p-1.5"
                    ),
                    rx.box(
                        rx.image(
                             src="/play.png",
                             alt="Descriptive text about the image",
                             box_size="14px",
                             max_width="50%",
                             class_name="w-[20px] h-[20px]"
                             ),
                             rx.box(
                                  "View Demo",
                                  class_name="text-base text-[rgba(21, 23, 26, 1)]"
                                  ),
                     
                        class_name="flex gap-1 items-center"
                    ),
                    class_name="flex gap-4 mt-6"
                ),
                class_name="flex flex-col gap-2"
            ),
            rx.box(
                rx.image(
                    src="/cuate.png",
                    alt="Descriptive text about the image",
                    box_size="500px",
                    max_width="50%"
                ),
                class_name="flex w-[50%] mt-4 justify-end h-[370px]"
            ),
            class_name="flex justify-between w-full mt-14"
        ),
        class_name="h-screen w-full flex flex-col mx-auto max-w-7xl"
    )
