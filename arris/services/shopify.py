import reflex as rx
from rxconfig import config
from fastapi.responses import RedirectResponse
from arris.utils import ClientStorageState, scopes, get_email_from_token
import shopify

from arris.schemas.shopify_store import (
    get_store,
    add_store,
    get_store_by_name,
)

api_version = "2024-01"


class ShopifyService(ClientStorageState):
    def install_app(self, shop: str):
        try:
            email = self.get_email()

            if not email:
                return rx.redirect("/login")

            if not shop:
                return rx.window_alert("Shop parameter is missing")

            storeData = get_store(name=shop)

            if storeData != None:
                return rx.window_alert("App already installed")

            shopify.Session.setup(
                api_key=config.shopify_api_key, secret=config.shopify_api_secret_key
            )

            shop_url = f"{shop}.myshopify.com"

            if shop.startswith("https://") or shop.startswith("http://"):
                shop_url = shop.split("/")[2]
            elif shop_url.endswith(".myshopify.com"):
                shop_url = shop

            state = self.generate_token(email)
            redirect_uri = f"{config.be_domain}/oauth/callback"

            newSession = shopify.Session(shop_url, api_version)
            auth_url = newSession.create_permission_url(scopes, redirect_uri, state)

            print("Redirecting to: ", auth_url)

            return rx.redirect(auth_url)
        except Exception as error:
            print("Store Error", error)
            return rx.window_alert(f"Store Error {error}")


def shopifyOAuthCallback(
    code: str,
    shop: str,
    state: str,
    hmac: str,
    host: str,
    timestamp: str,
):
    if code is None or shop is None or state is None:
        return RedirectResponse(
            f"{config.fe_domain}/home?error=missing_code_or_shop_or_state_parameter",
            status_code=303,
        )

    store_name = shop.split(".")[0]
    storeData = get_store_by_name(name=store_name)

    if storeData != None:
        return RedirectResponse(
            f"{config.fe_domain}/home?error=app_already_installed",
            status_code=303,
        )

    access_params = {
        "code": code,
        "shop": shop,
        "state": state,
        "hmac": hmac,
        "host": host,
        "timestamp": timestamp,
    }

    try:
        shopify.Session.setup(
            api_key=config.shopify_api_key, secret=config.shopify_api_secret_key
        )
        session = shopify.Session(shop, api_version)
        access_token = session.request_token(access_params)

        email = get_email_from_token(state)

        add_store(
            name=store_name,
            access_token=access_token,
            email=email,
        )

        return RedirectResponse(config.fe_domain, status_code=303)

    except Exception as error:
        print("OAuth Error", error)

        return RedirectResponse(
            f"{config.fe_domain}/home?error=oauth_error?error={error}",
            status_code=303,
        )
