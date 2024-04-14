import reflex as rx

from arris.styles import THEME, STYLESHEETS

from arris.pages.index import index
from arris.pages.register import register
from arris.services.shopify import shopifyOAuthCallback
from arris.pages.login import login
from arris.pages.home import home
from arris.pages.builder import builder
from arris.pages.builder_page import builder_page
from arris.pages.page_not_found import page_not_found
from arris.pages.no_access import no_access


# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(login, route="/login")
app.add_page(register, route="/register")
app.add_page(page_not_found, route="/page_not_found")
app.add_page(home, route="/home")
app.add_page(no_access, route="/no_access")
app.add_page(builder, route="/builder/[store_name]")
app.add_page(builder_page, route="/builder/[store_name]/[page_id]")
app.api.add_api_route("/oauth/callback/", shopifyOAuthCallback)
