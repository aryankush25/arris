# """The main index page."""

import reflex as rx
# from arris.data import (
#     line_chart_data,
#     lines,
#     pie_chart_data,
#     area_chart_data,
#     areas,
#     stat_card_data,
#     tabular_data,
# )
# from arris.graphs import (
#     area_chart,
#     line_chart,
#     pie_chart,
#     stat_card,
#     table,
# )
# from arris.navigation import navbar
# from arris.template import template

# from arris.schemas.user import AddUser


# # Content in a grid layout.


# def content_grid():

#     return rx.chakra.grid(
#         *[
#             rx.chakra.grid_item(stat_card(*c), col_span=1, row_span=1)
#             for c in stat_card_data
#         ],
#         rx.chakra.grid_item(
#             line_chart(data=line_chart_data, data_key="name", lines=lines),
#             col_span=3,
#             row_span=2,
#         ),
#         rx.chakra.grid_item(
#             pie_chart(data=pie_chart_data, data_key="value", name_key="name"),
#             row_span=2,
#             col_span=1,
#         ),
#         rx.chakra.grid_item(table(tabular_data=tabular_data), col_span=4, row_span=2),
#         rx.chakra.grid_item(
#             area_chart(data=area_chart_data, data_key="name", areas=areas),
#             col_span=3,
#             row_span=2,
#         ),
#         template_columns="repeat(4, 1fr)",
#         width="100%",
#         gap=4,
#         row_gap=8,
#     )


# @template


def index() -> rx.Component:
    return rx.box(
        #navbar
            rx.box(
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
        ),
        #features
        rx.box(
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
            #three box
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
                rx.box(
                    
                ),
                rx.box(

                ),
                class_name="flex w-full justify-between"
            ),
                class_name="flex flex-col items-center mx-auto max-w-7xl w-full gap-12"
            ),
            class_name="bg-[#5B9BF3] w-full mx-auto"
        ),
        class_name="min-h-screen w-full flex flex-col from-blue-100 bg-opacity-30 via-white to-blue-100 bg-gradient-to-r"
    )

#     return rx.box(
        # navbar(heading="Dashboard"),
#         rx.button(
#             "Decrement",
#             color_scheme="ruby",
#             on_click=AddUser.add_user,
#         ),
#         rx.box(
#             content_grid(),
#             margin_top="calc(50px + 2em)",
#             padding="2em",
#         ),
#         padding_left="250px",
#         padding_top="100px",
#     )


