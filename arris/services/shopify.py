import random
import requests
import reflex as rx
import rxconfig as config
from arris.schemas.shopify_store import ShopifyStoreRepo

class ShopifyService(rx.State):
    def install_app():
        try:
            shop = "xg-dev"
            email = "ravi@gmail.com"
            shopify_api = config.shopify_api_key
            scopes = "read_products,read_orders,read_analytics,read_orders,read_product_feeds,read_product_listings,read_products"
            be_domain = config.be_domain
            
            if not shop:
                return "Shop parameter is missing"

            print("Store Request Body", shop, email, shopify_api)
            
            get_store_instance = ShopifyStoreRepo()

            storeData = get_store_instance.get_store({
                "name": shop,
                "isAppInstall": "true"
            })

            if not storeData:
                get_store_instance.add_store({"shop": shop, "email": email})

            if storeData and storeData.get("isAppInstall"):
                return "App already installed"

            nonce = random.getrandbits(64)
            redirectUri = f"{be_domain}/shopify/oauth/callback"
            authUrl = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api}&scope={scopes}&redirect_uri={redirectUri}&state={nonce}"

            response = {"authUrl": authUrl}
            return response
        except Exception as error:
            print("Store Error", error)
