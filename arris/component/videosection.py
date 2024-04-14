import reflex as rx # type: ignore

def videosection() -> rx.Component:
    return rx.box(
        rx.box(
            "Want to see our AI website builder in action?",
            class_name="font-semibold text-2xl md:text-[32px] max-w-[630px]"
        ),
        rx.box(
            rx.video(
            url="https://www.youtube.com/watch?v=crDWEskuPII",
            width="100%",
            height="690px",
            class_name="rounded-3xl",
            playing=True,
            loop=True
        ),
            class_name="p-11 bg-[#6FB2FF] rounded-lg w-full"
        ),
        class_name="max-w-7xl justify-center items-center text-center px-4 mt-16 md:mt-28 mx-auto w-full flex flex-col gap-5"
    )