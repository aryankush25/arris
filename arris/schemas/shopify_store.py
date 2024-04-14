import reflex as rx
from models import ShopifyStores
from sqlmodel import select

def get_stores():
    with rx.session() as session:
        stores = session.exec(ShopifyStores.select.all())
        return stores


def get_store(
    name: str,
):
    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name.contains(name))
        ).first()

        return store


def get_store_by_name(name: str):
    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        return store


def update_store(name: str):

    with rx.session() as session:
        store = session.exec(
            select(ShopifyStores).where(ShopifyStores.name == name)
        ).first()

        session.add(store)
        session.commit()


def add_store(
    name: str,
    email: str,
    access_token: str,
):

    with rx.session() as session:
        session.add(
            ShopifyStores(
                name=name,
                email=email,
                access_token=access_token,
            )
        )
        session.commit()
