"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from arris.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from arris.pages.tools import tools
from arris.pages.team import team
from arris.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
