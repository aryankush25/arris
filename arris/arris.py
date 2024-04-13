"""The main Dashboard App."""

import reflex as rx

from arris.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from arris.pages.index import index
from arris.pages.register import register
from arris.services.shopify import shopifyOAuthCallback
from arris.pages.login import login
from arris.pages.home import home


# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")
app.add_page(home, route="/home")
app.api.add_api_route("/oauth/callback/", shopifyOAuthCallback)
