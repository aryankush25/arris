# """The main index page."""

import reflex as rx
from arris.component.herosection import herosection
from arris.component.navbar import navbar
from arris.component.featuresection import featuresection
from arris.component.footer import footer
from arris.component.reviewsection import reviewsection
from arris.component.template import templates

def index() -> rx.Component:
    return rx.box(
        navbar(),
        herosection(),
        featuresection(),
        reviewsection(),
        footer(),
        templates(),
        class_name="min-h-screen w-full flex flex-col from-blue-100 bg-opacity-30 via-white to-blue-100 bg-gradient-to-r"
    )
