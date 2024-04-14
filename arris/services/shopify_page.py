import shopify
import reflex as rx
from arris.utils import ClientStorageState
from arris.schemas.shopify_page import create_store_page
from arris.schemas.shopify_store import get_store

api_version = "2024-01"


class ShopifyPageService(ClientStorageState):
    def create_page(self, store_name: str, page_title: str, page_body: str):
        try:
            print("Creating Page", store_name)

            store_data = get_store(name=store_name)

            if store_data == None:
                return rx.window_alert("Store not found")

            shop_url = f"{store_name}.myshopify.com"

            if store_name.startswith("https://") or store_name.startswith("http://"):
                shop_url = store_name.split("/")[2]
            elif shop_url.endswith(".myshopify.com"):
                shop_url = store_name

            session = shopify.Session(shop_url, api_version, store_data.access_token)
            shopify.ShopifyResource.activate_session(session)

            page = shopify.Page()
            page.title = page_title
            page.body_html = page_body
            page.save()

            page_info = page.to_dict()

            print("Page Info", page_info)

            create_store_page(
                page_id=page_info["id"],
                shopify_store_id=page_info["shop_id"],
                title=page_info["title"],
                handle=page_info["handle"],
                body_html=page_info["body_html"],
                author=page_info["author"],
                template_suffix=page_info["template_suffix"],
                admin_graphql_api_id=page_info["admin_graphql_api_id"],
                created_at=page_info["created_at"],
                updated_at=page_info["updated_at"],
                published_at=page_info["published_at"],
                store_id=store_data.id,
            )

            return rx.window_alert("Page created")
        except Exception as error:
            print("Create Page Error", error)
        finally:
            shopify.ShopifyResource.clear_session()
