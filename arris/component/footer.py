import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
            rx.box(
                rx.box(
                rx.image(
                   src="/play.png",
                   alt="Descriptive text about the image",
                   box_size="14px",
                   max_width="40%",
                   class_name="w-[20px] h-[20px]" 
                ),
                rx.box(
                    "ARRIS",
                    class_name="font-bold text-black text-lg"
                ),
                class_name="flex gap-2 items-center justify-center"
            ),
            rx.box(
                "Arris uses AI to generate working",
                class_name="font-normal text-black text-sm mt-4"
            ),
            rx.box(
                "Webpages without the hassle to code.",
                class_name="font-normal text-black text-sm"
            ),
            ),
            rx.box(
                rx.box(
                "©2024 ARRIS, Inc.",
                class_name="font-normal text-black text-sm"
            ),
            rx.box(
                rx.image(
                   src="/Facebook.png",
                   alt="Descriptive text about the image",
                   box_size="14px",
                   class_name="w-[20px] h-[20px]" 
                ),
                rx.image(
                   src="/Instagram.png",
                   alt="Descriptive text about the image",
                   box_size="14px",
                   class_name="w-[20px] h-[20px]" 
                ),
                rx.image(
                   src="/Linkedin.png",
                   alt="Descriptive text about the image",
                   box_size="14px",
                   class_name="w-[20px] h-[20px]" 
                ),
                rx.image(
                   src="/Twitter.png",
                   alt="Descriptive text about the image",
                   box_size="14px",
                   class_name="w-[20px] h-[20px]" 
                ),
                class_name="flex gap-3 items-center mt-4"
            ),
            ),
            class_name="flex flex-col justify-between md:h-[315px] w-full items-center md:w-[40%]"

        ),
        rx.box(
            rx.box(
            rx.box(
                rx.box(
                    "Product",
                    class_name="font-bold text-black text-lg"
                    ),
            ),
            rx.box(
                rx.box(
                    "AI Assistant",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "CRM",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Invoicing",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Pricing",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Website builder",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Blog builder",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            class_name="flex flex-col gap-4 h-[315px]",
        ),
            rx.box(
            rx.box(
                rx.box(
                    "Resources",
                    class_name="font-bold text-black text-lg"
                    ),
            ),
            rx.box(
                rx.box(
                    "Blog",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Perks",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "State guides",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Industries",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Starter guides",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Website templates",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "AI tools",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            class_name="flex flex-col gap-4 h-[315px]",
        ),
            rx.box(
            rx.box(
                rx.box(
                    "Company",
                    class_name="font-bold text-black text-lg"
                    ),
            ),
            rx.box(
                rx.box(
                    "About",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Affiliate program",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Careers",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Newsletter",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Privacy policy",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Support",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            rx.box(
                rx.box(
                    "Terms of service",
                    class_name="font-normal text-black text-sm"
                    ),
            ),
            class_name="flex flex-col gap-4 md:h-[315px]",
        ),
        class_name="flex gap-5 md:justify-between md:w-[60%]"
        ),
        class_name="max-w-7xl flex-col md:flex-row flex w-full mx-auto items-center gap-10"
        ),
        class_name="w-full flex bg-blue-100 bg-opactiy-70 mt-12 md:mt-6 py-16 px-4"
    )
