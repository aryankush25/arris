import os
import reflex as rx

database_url = os.environ.get(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/arris"
)


config = rx.Config(
    app_name="arris",
    db_url=database_url,
)
