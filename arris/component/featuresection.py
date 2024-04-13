import reflex as rx

def featuresection() -> rx.Component:
    return rx.box(
    rx.box(
        rx.box(
            rx.text(
                "Features",
                class_name="text-white"
            ),
            rx.box(
                "Strategic services drive digital success with tailored, comprehensive approaches.",
                class_name="text-white"
            ),
            class_name="flex flex-col border items-center gap-5"
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
                rx.box(),
                class_name="p-6 flex flex-col rounded-lg bg-white max-w-sm w-full"
            ),
            rx.box(),
            rx.box(),
            class_name="flex w-full justify-between"
        ),
        class_name="flex flex-col items-center mx-auto max-w-7xl w-full gap-12"
    ),
    class_name="bg-[#5B9BF3] w-full mx-auto"
)
