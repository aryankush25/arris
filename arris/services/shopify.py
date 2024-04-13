import random
import reflex as rx
from rxconfig import config
import httpx
import requests
import axios
from arris.schemas.shopify_store import get_store, add_store, update_store, get_store_by_name


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

            be_domain = config.be_domain
            shopify_api_key = config.shopify_api_key

            redirectUri = f"{be_domain}/oauth/callback"
            authUrl = f"https://{shop}.myshopify.com/admin/oauth/authorize?client_id={shopify_api_key}&scope={scopes}&redirect_uri={redirectUri}&state={nonce}"

            print("Redirecting to: ", authUrl)

            return rx.redirect(authUrl)
        except Exception as error:
            print("Store Error", error)

def shopifyOAuthCallback(code: str, shop: str, state: str):
    shopify_api_key = config.shopify_api_key
    shopify_api_secret = config.shopify_api_secret_key
    
    # if code is None | shop is None | state is None:
    #     return "Missing code or shop or state parameter"
    
    accessTokenUrl = f"https://{shop}/admin/oauth/access_token"
    accessParams = {
        "client_id": shopify_api_key,
        "client_secret": shopify_api_secret,
        "code": code,
    }

    try:
        # response = requests.post(accessTokenUrl, data=accessParams)
        print("Access Token URL: ", accessTokenUrl, "Access Params: ", accessParams, "Shop: ", shop)
        # response = await client.post(accessTokenUrl, data=accessParams)
        # response = httpx.post(accessTokenUrl, data=accessParams)
        response = requests.post(accessTokenUrl, data=accessParams, headers={ 'Accept': 'application/json', 'Content-Type': 'application/json' })
        # response.raise_for_status()
        print(response.json(),"response")
        access_token = response.json().get("access_token")
        store_name = shop.split(".")[0]
        
        storeData = get_store_by_name(name=store_name)
        if not storeData:
            return "Store not found"
        
        print("FOUND STORE: ", storeData)
        update_store(name=store_name, access_token=access_token)
        print("UPDATED ")
        print("DONE ASYNC")
        # return "DONE"
        yield [rx.redirect(f"https://google.com")]
    except Exception as error:
        print("OAuth Error", error)
    # async with httpx.AsyncClient() as client: