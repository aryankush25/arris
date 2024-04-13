import reflex as rx

def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            "ARRIS",
            class_name="font-semibold text-[#5B9BF3] text-5xl"
        ),
        rx.box(
            rx.box(
                "Home",
                class_name="font-medium text-gray-500"
            ),
            rx.box(
                "Product",
                class_name="font-medium text-gray-500"
            ),
            rx.box(
                "About Us",
                class_name="font-medium text-gray-500"
            ),
            class_name="flex items-center gap-20"
        ),
        rx.box(
            rx.box(
                "Login",
                class_name="text-gray-500 font-medium"
            ),
            rx.box(
                "Sign Up",
                class_name="text-white py-2 px-[14px] bg-black rounded-md"
            ),
            class_name="flex gap-3 items-center"
        ),
        class_name="flex justify-between w-full mt-14 max-w-7xl mx-auto"
    )
