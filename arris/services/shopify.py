import random
import requests
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

            print("Store Request Body", shop, email, shopify_api_key)

            storeData = get_store(name=shop, is_app_installed=True)

            print("Store Data", storeData)

            if not storeData:
                add_store({"shop": shop, "email": email})

            if storeData != None and storeData.is_app_install:
                return "App already installed"

            nonce = random.getrandbits(64)
            redirectUri = f"{be_domain}/shopify/oauth/callback"
            authUrl = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api_key}&scope={scopes}&redirect_uri={redirectUri}&state={nonce}"

            response = {"authUrl": authUrl}
            return response
        except Exception as error:
            print("Store Error", error)
