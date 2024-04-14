import reflex as rx
from typing import Optional

from sqlmodel import Field

class ShopifyThemes(rx.Model, table=True):
    __tablename__ = "shopify_themes"
    id: int = Field(default=None, primary_key=True)
    theme_id: int
    name: str
    role: str
    theme_store_id: Optional[str] = None
    previewable: bool = False
    processing: bool = False
    admin_graphql_api_id: str
    email: str
    store_id: int
