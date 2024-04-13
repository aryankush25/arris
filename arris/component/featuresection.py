import reflex as rx

def featuresection() -> rx.Component:
    return rx.box(
    rx.box(
        rx.box(
            rx.text(
                "Features",
                class_name="text-white font-bold text-[32px]"
            ),
            rx.text(
                "Strategic services drive digital success with tailored, comprehensive approaches.",
                class_name="text-white font-medium text-xl backdrop-opacity-80"
            ),
            class_name="flex flex-col items-center gap-5"
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.text(
                    "AI Generated Webpages",
                    class_name="text-black font-bold text-3xl"
                ),
                rx.text(
                    "Using AI to create websites offers speed and flexibility to any new design project. Build an AI generated website in real-time by writing a detailed prompt for the content you want to center the site on.",
                    class_name="text-[#33373A99]"
                ),
                class_name="flex flex-col gap-1.5"
                ),
                rx.image(
                        src="/screen.png",
                        class_name="mx-auto w-64 h-40"
                    ),
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-sm w-full"
            ),
            rx.box(
                rx.box(
                    rx.text(
                    "AI Generated Webpages",
                    class_name="text-black font-bold text-3xl"
                ),
                rx.text(
                    "Using AI to create websites offers speed and flexibility to any new design project. Build an AI generated website in real-time by writing a detailed prompt for the content you want to center the site on.",
                    class_name="text-[#33373A99]"
                ),
                class_name="flex flex-col gap-1.5"
                ),
                rx.image(
                        src="/screen.png",
                        class_name="mx-auto w-64 h-40"
                    ),
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-sm w-full"
            ),
            rx.box(
                rx.box(
                    rx.text(
                    "AI Generated Webpages",
                    class_name="text-black font-bold text-3xl"
                ),
                rx.text(
                    "Using AI to create websites offers speed and flexibility to any new design project. Build an AI generated website in real-time by writing a detailed prompt for the content you want to center the site on.",
                    class_name="text-[#33373A99]"
                ),
                class_name="flex flex-col gap-1.5"
                ),
                rx.image(
                        src="/screen.png",
                        class_name="mx-auto w-64 h-40"
                    ),
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-sm w-full"
            ),
            class_name="flex w-full justify-between"
        ),
        class_name="flex flex-col items-center mx-auto max-w-7xl w-full gap-12"
    ),
    class_name="bg-[#5B9BF3] w-full mx-auto"
)
