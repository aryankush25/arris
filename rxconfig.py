import reflex as rx
from dotenv import dotenv_values

envConfig = dotenv_values()


config = rx.Config(
    app_name="arris",
    db_url=envConfig["DATABASE_URL"],
    shopify_api_key=envConfig["SHOPIFY_API_KEY"],
    shopify_api_secret_key=envConfig["SHOPIFY_API_SECRET_KEY"],
    be_domain=envConfig["BE_DOMAIN"],
    fe_domain=envConfig["FE_DOMAIN"],
    jwt_secret=envConfig["JWT_SECRET"],
    openai_key=envConfig["OPENAI_KEY"],
)
