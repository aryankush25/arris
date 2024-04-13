import reflex as rx
from models import ShopifyStores
from sqlmodel import select

def get_stores():
    with rx.session() as session:
        stores = session.exec(ShopifyStores.select.all())
        return stores


def get_store(name: str, is_app_installed: bool):
    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(
                ShopifyStores.name.contains(name) & ShopifyStores.is_app_installed
                == is_app_installed
            )
        ).first()

        return store


def get_store_by_name(name: str):
    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        return store


def update_store(name: str, access_token: str):

    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        store.access_token = access_token
        store.is_app_installed = True
        session.add(store)
        session.commit()


def add_store(
    name: str,
    email: str,
    state: str,
    access_token: str,
    is_app_installed: bool,
):

    with rx.session() as session:
        session.add(
            ShopifyStores(
                name=name,
                state=state,
                email=email,
                access_token=access_token,
                is_app_installed=is_app_installed,
            )
        )
        session.commit()
