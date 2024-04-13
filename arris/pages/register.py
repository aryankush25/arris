import reflex as rx
from passlib.hash import pbkdf2_sha256
from arris.utils import ClientStorageState
import jwt
from arris.schemas.user import add_user
from arris.protected import not_require_login


class RadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):

        add_user(
            email=form_data["email"],
            full_name=form_data["name"],
            password=pbkdf2_sha256.hash(form_data["password"]),
        )

        # TODO: Use .env file for secret
        encoded = jwt.encode({"some": form_data["email"]}, "secret", algorithm="HS256")

        # jwt.decode(encoded, "secret", algorithms=["HS256"])

        yield [rx.redirect("/"), ClientStorageState.set_custom_cookie(encoded)]


@not_require_login
def register() -> rx.Component:

    return rx.box(
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Full Name"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Full Name",
                            # type attribute is required for "typeMismatch" validation
                            type="name",
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a valid full name",
                        match="typeMismatch",
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="name",
            ),
            rx.form.field(
                rx.flex(
                    rx.form.label("Email"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Email Address",
                            # type attribute is required for "typeMismatch" validation
                            type="email",
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a valid email",
                        match="typeMismatch",
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="email",
            ),
            rx.form.field(
                rx.flex(
                    rx.form.label("Password"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Enter your password",
                            type="password",
                            min_length=8,
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a password length >= 8",
                        match="tooShort",
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="password",
            ),
            rx.form.submit(
                rx.button("Submit"),
                as_child=True,
            ),
            on_submit=RadixFormSubmissionState.handle_submit,
        ),
    )
