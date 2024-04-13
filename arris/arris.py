"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from arris.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from arris.pages.index import index
from arris.pages.register import register
from arris.services.shopify import shopifyOAuthCallback
from arris.schemas.shopify_store import update_store

# from arris.pages.tools import tools
# from arris.pages.team import team

def health():
    # update_store(name="xg-dev", access_token="access_token")
    # return "Healthy"
    yield [rx.redirect(f"https://google.com")]


# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(register, route="/register")
app.api.add_api_route("/oauth/callback/", shopifyOAuthCallback)
app.api.add_api_route("/health", health, methods=["GET"])
# app.api.add_api_route("/install-shopify", install_app("xg-dev", "ravi149185@gmail.com"))
# app.add_page(tools, route="/tools")
# app.add_page(team, route="/team")
