import os
import reflex as rx
from dotenv import dotenv_values  # type: ignore

envConfig = dotenv_values()


config = rx.Config(
    app_name="arris",
    db_url=envConfig["DATABASE_URL"],
    shopify_api_key=envConfig["SHOPIFY_API_KEY"],
    shopify_api_secret_key=envConfig["SHOPIFY_API_SECRET_KEY"],
    be_domain=envConfig["BE_DOMAIN"],
)
