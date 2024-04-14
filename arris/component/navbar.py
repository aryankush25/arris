import reflex as rx # type: ignore
from arris.utils import ClientStorageState

def navbar() -> rx.Component:
    def redirect_to_signup():
        return rx.redirect("/register")
    def redirect_to_signin():
        return rx.redirect("/login")
    def redirect_to_home():
        return rx.redirect("/home")
    display_login: str = rx.Cookie("access-token")
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
        rx.cond(
                ClientStorageState.custom_cookie,
                rx.box(
            "Go to Home",
            class_name="text-white cursor-pointer md:text-lg py-1.5 flex items-center px-4 bg-black rounded-md",
            on_click=redirect_to_home
        ),
                rx.box(
            rx.box(
                "Login",
                class_name="text-gray-500 md:text-lg font-medium cursor-pointer",
                on_click=redirect_to_signin
            ),
            rx.box(
                "Sign Up",
                class_name="text-white cursor-pointer md:text-lg py-2 px-[14px] bg-black rounded-md",
                on_click=redirect_to_signup
            ),
            class_name="flex gap-5 items-center"
        ),
            ),
        class_name="flex justify-between w-full md:mt-14 mt-8 px-4 max-w-7xl mx-auto"
    )
