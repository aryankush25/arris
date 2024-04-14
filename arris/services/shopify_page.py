import reflex as rx
from arris.utils import ClientStorageState
import shopify

api_version = "2024-01"


class ShopifyService(ClientStorageState):
  def publish_page_and_update_theme(self, shop: str, page_title: str, page_body: str):
      print("Publishing Page and Updating Theme", shop)
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

      return rx.window_alert("Page created")
