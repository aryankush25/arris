import reflex as rx  # type: ignore


def no_access() -> rx.Component:

    return rx.box(
        rx.image(src="/noaccess.svg"),
        rx.box(
            "You don't have access to this page.",
            class_name="mt-6 font-semibold text text-2xl max-w-[460px] text-center",
        ),
        rx.box("Please Log In", class_name="mt-1 text-[#4F4F4F]"),
        rx.box(
            "Login",
            class_name="py-3 px-6 bg-black font-semibold text-white rounded cursor-pointer mt-6",
            on_click=lambda: rx.redirect("/login"),
        ),
        class_name="h-screen w-full flex flex-col justify-center items-center from-blue-100 via-white to-blue-100 bg-gradient-to-r",
    )
