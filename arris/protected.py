import reflex as rx
from arris.utils import ClientStorageState


def require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:

    def protected_page():
        return rx.cond(
            ClientStorageState.custom_cookie,
            page(),
            protected(),
        )

    protected_page.__name__ = page.__name__

    return protected_page


def not_require_login(page: rx.app.ComponentCallable) -> rx.app.ComponentCallable:

    def protected_page():
        return rx.cond(
            ClientStorageState.custom_cookie,
            protected(),
            page(),
        )

    protected_page.__name__ = page.__name__

    return protected_page


def protected() -> rx.Component:

    return rx.fragment(
        rx.cond(
            ClientStorageState.is_hydrated,
            rx.cond(
                ClientStorageState.custom_cookie,
                rx.box(
                    rx.image(src="/fallback.svg"),
                    rx.box(
                        "Oops! The page you are looking for doesn't exist",
                        class_name="mt-6 font-semibold text text-2xl max-w-[460px] text-center",
                    ),
                    rx.box(
                        "Sorry we couldn't find any page for your search.",
                        class_name="mt-1 text-[#4F4F4F]",
                    ),
                    rx.box(
                        "Go back to home",
                        class_name="text-white bg-black rounded py-3 px-6 cursor-pointer mt-6",
                        on_click=lambda: rx.redirect("/home"),
                    ),
                    class_name="h-screen w-full flex flex-col justify-center items-center from-blue-100 via-white to-blue-100 bg-gradient-to-r",
                ),
                rx.box(
                    rx.image(src="/noaccess.svg"),
                    rx.box(
                        "You don't have access to this page.",
                        class_name="mt-6 font-semibold text text-2xl max-w-[460px] text-center",
                    ),
                    rx.box("Please log in", class_name="mt-1 text-[#4F4F4F]"),
                    rx.box(
                        "Login",
                        class_name="py-3 px-6 bg-black font-semibold text-white rounded cursor-pointer mt-6",
                        on_click=lambda: rx.redirect("/login"),
                    ),
                    class_name="h-screen w-full flex flex-col justify-center items-center from-blue-100 via-white to-blue-100 bg-gradient-to-r",
                ),
            ),
            rx.chakra.center(
                rx.chakra.spinner(),
            ),
        )
    )
