import reflex as rx


def page_not_found() -> rx.Component:

    return rx.box(
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
            "Go Back to ARRIS",
            class_name="text-white bg-black rounded py-3 px-6 cursor-pointer mt-6",
            on_click=lambda: rx.redirect("/home"),
        ),
        class_name="h-screen w-full flex flex-col justify-center items-center from-blue-100 via-white to-blue-100 bg-gradient-to-r",
    )
