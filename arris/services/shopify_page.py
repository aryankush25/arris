import shopify
import reflex as rx
from arris.utils import ClientStorageState
from arris.schemas.shopify_page import create_store_page, update_store_page, get_store_page_by_id
from arris.schemas.shopify_store import get_store
from arris.schemas.shopify_page import get_store_page_by_page_id

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

            print("shop_url", shop_url)

            session = shopify.Session(shop_url, api_version, store_data.access_token)
            shopify.ShopifyResource.activate_session(session)

            page = shopify.Page()
            page.title = page_title
            page.body_html = page_body
            page.save()

            page_info = page.to_dict()

            shopify.ShopifyResource.clear_session()

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

            page_id = get_store_page_by_page_id(str(page_info["id"])).id

            return rx.redirect(f"/builder/{store_name}/{page_id}")

        except Exception as error:
            print("Create Page Error", error)
            return rx.window_alert("Error creating page")
            
def update_page(store_name: str, page_id: str, page_body: str):
    try:
        page_data = get_store_page_by_id(id=page_id)
        store_data = get_store(name=store_name)

        if store_data == None:
            return rx.window_alert("Store not found")

        shop_url = f"{store_name}.myshopify.com"

        session = shopify.Session(shop_url, api_version, store_data.access_token)
        shopify.ShopifyResource.activate_session(session)

        page = shopify.Page.find(page_data.page_id)
        page.body_html = page_body
        page.save()

        page_info = page.to_dict()

        shopify.ShopifyResource.clear_session()

        update_store_page(
            id=page_data.id,
            body_html=page_info["body_html"],
        )

        return rx.window_alert("Page updated")
    except Exception as error:
        print("Update Page Error", error)
    finally:
        shopify.ShopifyResource.clear_session()

def delete_page(store_name: str, page_id: str):
    try:
        page_data = get_store_page_by_id(id=page_id)
        store_data = get_store(name=store_name)

        if store_data == None:
            return rx.window_alert("Store not found")

        shop_url = f"{store_name}.myshopify.com"

        session = shopify.Session(shop_url, api_version, store_data.access_token)
        shopify.ShopifyResource.activate_session(session)

        page = shopify.Page.find(page_data.page_id)
        page.destroy()

        shopify.ShopifyResource.clear_session()

        return rx.window_alert("Page removed")
    except Exception as error:
        print("Remove Page Error", error)
    finally:
        shopify.ShopifyResource.clear_session()