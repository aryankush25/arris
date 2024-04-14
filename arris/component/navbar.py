import reflex as rx # type: ignore

def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            "ARRIS",
            class_name="font-semibold text-[#5B9BF3] text-[32px] md:text-5xl"
        ),
        rx.box(
            rx.box(
                "Home",
                class_name="font-medium text-lg text-gray-500"
            ),
            rx.box(
                "Product",
                class_name="font-medium text-lg text-gray-500"
            ),
            rx.box(
                "About Us",
                class_name="font-medium text-lg text-gray-500"
            ),
            class_name="md:flex items-center hidden gap-16"
        ),
        rx.box(
            rx.box(
                "Login",
                class_name="text-gray-500 md:text-lg font-medium"
            ),
            rx.box(
                "Sign Up",
                class_name="text-white md:text-lg py-2 px-[14px] bg-black rounded-md"
            ),
            class_name="flex gap-3 items-center"
        ),
        class_name="flex justify-between w-full md:mt-14 mt-8 px-4 max-w-7xl mx-auto"
    )
