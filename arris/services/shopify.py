import random
import reflex as rx
from rxconfig import shopify_api_key, be_domain
from arris.schemas.shopify_store import get_store, add_store


class ShopifyService(rx.State):
    def install_app(self):
        try:
            shop = "xg-dev"
            email = "ravi@gmail.com"
            scopes = "read_products,read_orders,read_analytics,read_orders,read_product_feeds,read_product_listings,read_products"

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

            redirectUri = f"{be_domain}/shopify/oauth/callback"
            authUrl = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api_key}&scope={scopes}&redirect_uri={redirectUri}&state={nonce}"

            print("Redirecting to: ", authUrl)

            return rx.redirect(authUrl)
        except Exception as error:
            print("Store Error", error)
