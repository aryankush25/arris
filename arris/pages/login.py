import reflex as rx
from passlib.hash import pbkdf2_sha256
from arris.utils import ClientStorageState
import jwt
from rxconfig import config
from arris.protected import not_require_login


from arris.schemas.user import get_user


class LoginRadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):

        user = get_user(
            email=form_data["email"],
        )

        user.password

        # TODO: Use .env file for secret

        if user and pbkdf2_sha256.verify(form_data["password"], user.password):
            encoded = jwt.encode(
                {"email": form_data["email"]}, config.jwt_secret, algorithm="HS256"
            )
            yield [rx.redirect("/"), ClientStorageState.set_custom_cookie(encoded)]


@not_require_login
def login() -> rx.Component:

    return rx.box(
        rx.form.root(
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
            on_submit=LoginRadixFormSubmissionState.handle_submit,
        ),
    )
