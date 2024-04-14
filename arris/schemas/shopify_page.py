import reflex as rx
from models import ShopifyPage
from sqlmodel import select

def get_store_pages(storeId: int):
    with rx.session() as session:
        shopifyPages = session.exec(
            select(ShopifyPage).where(
                ShopifyPage.store_id == storeId
            )
        ).all()
        return shopifyPages


def get_store_page_by_id(id: int):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(
                ShopifyPage.id == id
            )
        ).first()

        return shopifyPage

def update_store_page(id: int, role: str, name: str):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.id == id)
        ).first()

        session.add(shopifyPage)
        session.commit()

def delete_store_page(id: int):
    with rx.session() as session:
        shopifyPage = session.exec(
            select(ShopifyPage).where(ShopifyPage.id == id)
        ).first()

        session.delete(shopifyPage)
        session.commit()

def create_store_page(
  page_id: int,
  title: str,
  handle: str,
  body_html: str,
  author: str,
  template_suffix: str,
  admin_graphql_api_id: str,
  created_at: str,
  updated_at: str,
  published_at: str,
  email: str,
  store_id: int
):
    with rx.session() as session:
        session.add(
            ShopifyPage(
              email=email,
              store_id=store_id,
              admin_graphql_api_id=admin_graphql_api_id,
              title=title,
              handle=handle,
              body_html=body_html,
              author=author,
              template_suffix=template_suffix,
              created_at=created_at,
              updated_at=updated_at,
              published_at=published_at,
              page_id=page_id
            )
        )
        session.commit()
