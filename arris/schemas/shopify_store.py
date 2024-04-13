import reflex as rx
from models import ShopifyStores


def get_stores():
    with rx.session() as session:
        stores = session.exec(ShopifyStores.select.all())
        return stores


def get_store(name: str, is_app_installed: bool):
    print("Store Request Body", name)
    print("Store Request Body", is_app_installed)
    with rx.session() as session:
        store = session.exec(
            ShopifyStores.select(ShopifyStores.name.contains(name)).all()
        )

        # users = session.exec(
        #     User.select.where(User.email.contains()).all()
        # )

        return store


def add_store(store: dict):
    with rx.session() as session:
        session.add(
            ShopifyStores(
                name=store.name,
                state=store.state,
                email=store.email,
                access_token=store.access_token,
                is_app_installed=store.is_app_installed,
            )
        )
    session.commit()
