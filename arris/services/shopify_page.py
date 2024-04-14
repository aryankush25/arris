import shopify
import reflex as rx
from arris.utils import ClientStorageState
from arris.schemas.shopify_page import create_store_page
from arris.schemas.shopify_store import get_store

api_version = "2024-01"


class ShopifyPageService(ClientStorageState):
  def craete_page(self, shop: str, page_title: str, page_body: str):
    try:
      print("Creating Page", shop)
      
      store_data = get_store(name=shop)

      if store_data == None:
          return rx.window_alert("Store not found")

      shop_url = f"{shop}.myshopify.com"

      if shop.startswith("https://") or shop.startswith("http://"):
          shop_url = shop.split("/")[2]
      elif shop_url.endswith(".myshopify.com"):
          shop_url = shop

      session = shopify.Session(shop_url, api_version, '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')
      shopify.ShopifyResource.activate_session(session)

      page = shopify.Page()
      page.title = page_title
      page.body_html = page_body
      page.save()

      page_info = page.to_dict()
      
      email=self.get_email()
      print("Page Info", page_info)
      create_store_page(
        page_id= page_info["id"],
        title= page_info["title"],
        handle= page_info.handle,
        body_html= page_info.body_html,
        author=page_info.author,
        template_suffix=page_info.template_suffix,
        admin_graphql_api_id=page_info.admin_graphql_api_id,  
        created_at=page_info.created_at,
        updated_at=page_info.updated_at,
        published_at=page_info.published_at,
        email=email,
        store_id=store_data.id
      )

      return rx.window_alert("Page created")
    except Exception as error:
      print("Craete Page Error", error)
    finally:
      shopify.ShopifyResource.clear_session()
