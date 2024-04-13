import reflex as rx
from models import ShopifyStores

class ShopifyStoreRepo(rx.State):
  store: ShopifyStores
  stores: list[ShopifyStores]

  def get_stores(self):
    with rx.session() as session:
        self.stores = session.exec(ShopifyStores.select.all())

  def get_store(self):
    with rx.session() as session:
      self.store = session.exec(ShopifyStores.select.where(
        (ShopifyStores.name == self.name) &
        (ShopifyStores.is_app_installed == self.isAppInstall)
    ))

  def add_store(self):
    with rx.session() as session:
      session.add(
          ShopifyStores(
            name=self.name,
            state=self.state,
            email=self.email,
            access_token=self.access_token,
            is_app_installed=self.is_app_installed,
          )
      )
    session.commit()
