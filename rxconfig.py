import os
import reflex as rx
from dotenv import dotenv_values  # type: ignore

config = dotenv_values()

database_url = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/arris"
)

config = rx.Config(
    app_name="arris",
    db_url=config["DATABASE_URL"],
    shopify_api_key = config["SHOPIFY_API_KEY"],
    shopify_api_secret_key = config["SHOPIFY_API_SECRET_KEY"],
    be_domain = "https://ed9e-112-196-47-10.ngrok-free.app",
)
