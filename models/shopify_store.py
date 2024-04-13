import reflex as rx
from typing import Optional

from sqlmodel import Field


class ShopifyStores(rx.Model, table=True):
    __tablename__ = "shopify_stores"
    id: int = Field(default=None, primary_key=True)
    name: str
    state: str
    email: str
    access_token: Optional[str] = None
    is_app_installed: bool = False
