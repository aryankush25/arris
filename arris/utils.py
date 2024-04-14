import reflex as rx
import jwt
from rxconfig import config

scopes = [
    "read_products",
    "read_orders",
    "read_analytics",
    "read_orders",
    "read_product_feeds",
    "read_product_listings",
    "read_products",
    "read_script_tags",
    "read_shipping",
    "read_shopify_payments_payouts",
    "read_themes",
    "write_checkouts",
    "write_customers",
    "write_draft_orders",
    "write_inventory",
    "write_marketing_events",
    "write_orders",
    "write_price_rules",
    "write_products",
    "write_script_tags",
    "write_shipping",
    "write_themes",
]


class ClientStorageState(rx.State):
    custom_cookie: str = rx.Cookie(
        max_age=86400,
        path="/",
        name="access_token",
    )

    def get_email(self):
        if not self.custom_cookie:
            return None

        payload = jwt.decode(
            self.custom_cookie,
            config.jwt_secret,
            algorithms=["HS256"],
        )

        return payload["email"]

    def generate_token(self, email: str):
        return jwt.encode(
            {"email": email},
            config.jwt_secret,
            algorithm="HS256",
        )

    def logout(self):
        yield [rx.remove_cookie("access_token"), rx.redirect("/login")]


def get_email_from_token(jwt_token: str):
    payload = jwt.decode(
        jwt_token,
        config.jwt_secret,
        algorithms=["HS256"],
    )

    return payload["email"]
