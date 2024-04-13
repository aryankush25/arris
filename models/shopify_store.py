import reflex as rx

from sqlmodel import Field

class ShopifyStores(rx.Model, table=True):
    __tablename__ = "shopify_stores"
    id: int = Field(default=None, primary_key=True)
    name: str
    state: str
    email: str
    access_token: str
    is_app_installed: bool
    created_at: str
    updated_at: str
    deleted_at: str
