import reflex as rx # type: ignore

def featuresection() -> rx.Component:
    return rx.box(
        rx.box(
            border_radius="50% 50% 50% 50% / 0% 0% 100% 100%"
        ),
        rx.box(
        rx.box(
            rx.text(
                "Features",
                class_name="text-white font-bold text-5xl"
            ),
            rx.text(
                "Strategic services drive digital success with tailored, comprehensive approaches.",
                class_name="text-white text-xl backdrop-opacity-80"
            ),
            class_name="flex flex-col items-center gap-3"
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
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-[360px] w-full"
            ),
            rx.box(
                rx.box(
                    rx.text(
                    "Smart Prototyping using AI",
                    class_name="text-black font-bold text-3xl"
                ),
                rx.text(
                    "Quickly transition from a simple idea to a fully functional prototype using AI for web development, which lets you go from an idea to a fully functioning prototype in minutes rather than hours.",
                    class_name="text-[#33373A99]"
                ),
                class_name="flex flex-col gap-1.5"
                ),
                rx.image(
                        src="/phone.png",
                        class_name="mx-auto w-64 h-40"
                    ),
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-[360px] w-full"
            ),
            rx.box(
                rx.box(
                    rx.text(
                    "Drag and drop editing",
                    class_name="text-black font-bold text-3xl"
                ),
                rx.text(
                    "Drag and Drop to create responsive pages and sections. Add text, buttons and pull product images straight from Shopify.",
                    class_name="text-[#33373A99]"
                ),
                class_name="flex flex-col gap-1.5"
                ),
                rx.image(
                        src="/dragdrop.png",
                        class_name="mx-auto w-64 h-40"
                    ),
                class_name="p-6 flex gap-4 flex-col rounded-lg bg-white max-w-[360px] w-full"
            ),
            class_name="flex flex-col md:flex-row w-full gap-3 md:gap-7 mx-auto justify-center items-center"
        ),
        class_name="flex flex-col mx-auto max-w-7xl w-full gap-12 text-center px-3"
    ),
    class_name="bg-[#5B9BF3] w-full mx-auto mt-28 py-16 md:py-32",
)
