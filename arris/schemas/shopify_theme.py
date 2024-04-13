import reflex as rx
from models import ShopifyThemes
from sqlmodel import select


def get_store_themes(storeId: int):
    with rx.session() as session:
        storeThemes = session.exec(
            select(ShopifyThemes).where(
                ShopifyThemes.store_id == storeId
            )
        ).all()
        return storeThemes


def get_store_theme_by_id(id: int):
    with rx.session() as session:
        storeTheme = session.exec(
            select(ShopifyThemes).where(
                ShopifyThemes.id == id
            )
        ).first()

        return storeTheme

def update_store_theme(id: int, role: str, name: str):
    with rx.session() as session:
        storeTheme = session.exec(
            select(ShopifyThemes).where(ShopifyThemes.id == id)
        ).first()

        if role:
            storeTheme.role = role
        if name:
            storeTheme.name = name
        session.add(storeTheme)
        session.commit()

def delete_store_theme(id: int):
    with rx.session() as session:
        storeTheme = session.exec(
            select(ShopifyThemes).where(ShopifyThemes.id == id)
        ).first()

        session.delete(storeTheme)
        session.commit()

def create_store_theme(
    theme_id: int,
    name: str,
    role: str,
    email: str,
    store_id: int,
    admin_graphql_api_id: str,
    theme_store_id: str = None,
    previewable: bool = False,
    processing: bool = False,
):
    with rx.session() as session:
        session.add(
            ShopifyThemes(
              theme_id=theme_id,
              name=name,
              role=role,
              email=email,
              store_id=store_id,
              admin_graphql_api_id=admin_graphql_api_id,
              theme_store_id=theme_store_id,
              previewable=previewable,
              processing=processing
            )
        )
        session.commit()
