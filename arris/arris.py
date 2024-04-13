"""The main Dashboard App."""

import reflex as rx

from arris.styles import THEME, STYLESHEETS

from arris.pages.index import index
from arris.pages.register import register
from arris.services.shopify import shopifyOAuthCallback
from arris.services.shopify_theme import createStoreTheme, updateStoreTheme, getStoreThemes, getStoreThemeById
from arris.pages.login import login


# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")
app.api.add_api_route("/oauth/callback/", shopifyOAuthCallback)
app.api.add_api_route("shopify/theme/create", createStoreTheme, methods=["POST"])
app.api.add_api_route("shopify/theme/update/{id}", updateStoreTheme, methods=["PUT"])
app.api.add_api_route("shopify/theme/get", getStoreThemes, methods=["GET"])
app.api.add_api_route("shopify/theme/get/{id}", getStoreThemeById, methods=["GET"])
app.api.add_api_route("shopify/theme/delete/{id}", getStoreThemeById, methods=["DELETE"])