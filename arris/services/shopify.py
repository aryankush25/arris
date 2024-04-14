import random
import reflex as rx
from rxconfig import config
import requests
from fastapi.responses import RedirectResponse
from arris.utils import ClientStorageState, scopes

from arris.schemas.shopify_store import (
    get_store,
    add_store,
    update_store,
    get_store_by_name,
)


class ShopifyService(ClientStorageState):
    def install_app(self, shop: str):
        try:
            email = self.get_email()

            if not email:
                return rx.redirect("/login")

            if not shop:
                return "Shop parameter is missing"

            storeData = get_store(name=shop, is_app_installed=True)

            nonce = random.getrandbits(64)

            if storeData is None:
                add_store(
                    name=shop,
                    email=email,
                    state=nonce,
                    access_token=None,
                    is_app_installed=False,
                )

            if storeData != None and storeData.is_app_installed:
                return "App already installed"

            be_domain = config.be_domain
            shopify_api_key = config.shopify_api_key

            scopeString = ",".join(scopes)
            redirectUri = f"{be_domain}/oauth/callback"
            authUrl = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api_key}&scope={scopeString}&redirect_uri={redirectUri}&state={nonce}"

            print("Redirecting to: ", authUrl)

            return rx.redirect(authUrl)
        except Exception as error:
            print("Store Error", error)


def shopifyOAuthCallback(code: str, shop: str, state: str):
    # if code is None | shop is None | state is None:
    #     return "Missing code or shop or state parameter"

    accessTokenUrl = f"https://{shop}/admin/oauth/access_token"
    accessParams = {
        "client_id": config.shopify_api_key,
        "client_secret": config.shopify_api_secret_key,
        "code": code,
    }

    try:
        response = requests.post(accessTokenUrl, data=accessParams)

        access_token = response.json().get("access_token")
        store_name = shop.split(".")[0]

        storeData = get_store_by_name(name=store_name)
        if not storeData:
            return "Store not found"

        update_store(name=store_name, access_token=access_token)

        return RedirectResponse(config.fe_domain, status_code=303)

    except Exception as error:
        print("OAuth Error", error)
