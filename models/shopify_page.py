import reflex as rx
from typing import Optional

from sqlmodel import Field


class ShopifyPage(rx.Model, table=True):
    __tablename__ = "shopify_pages"

    id: int = Field(default=None, primary_key=True)
    page_id: str
    shopify_store_id: str
    title: str
    handle: str
    body_html: str
    author: str
    template_suffix: Optional[str] = None
    admin_graphql_api_id: str
    created_at: str
    updated_at: str
    published_at: Optional[str] = None
    store_id: int
