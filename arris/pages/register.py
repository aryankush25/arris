import reflex as rx  # type: ignore
from passlib.hash import pbkdf2_sha256  # type: ignore
from arris.utils import ClientStorageState
from arris.schemas.user import add_user
from arris.protected import not_require_login


class RadixFormSubmissionState(ClientStorageState):
    form_data: dict

    def handle_submit(self, form_data: dict):

        add_user(
            email=form_data["email"],
            full_name=form_data["name"],
            password=pbkdf2_sha256.hash(form_data["password"]),
        )

        encoded = self.generate_token(form_data["email"])

        # jwt.decode(encoded, "secret", algorithms=["HS256"])

        yield [rx.redirect("/home"), ClientStorageState.set_custom_cookie(encoded)]


@not_require_login
def register() -> rx.Component:
    def redirect_to_signin():
        return rx.redirect("/login")

    return rx.box(
        rx.box(
            rx.image(
                src="/right_rectangle.png",
                alt="Descriptive text about the image",
                height="300px",
            ),
            class_name="w-full flex absolute top-0",  # Adjust positioning
        ),
        rx.box(
            rx.box(
                rx.image(
                    src="/company_logo.png",
                    alt="Descriptive text about the image",
                    height="45px",
                    width="45px",
                ),
                rx.text("ARRIS", class_name="text-2xl font-bold text-black"),
                class_name="w-full flex gap-2 justify-center items-center",
            ),
            rx.form.root(
                rx.box(
                    rx.text(
                        "Create an Account",
                        class_name="font-bold text-2xl text-black pb-2",
                    ),
                    rx.text(
                        "Create an account to access the world of",
                        class_name="font-normal text-black text-sm",
                    ),
                    rx.text(
                        "building AI powered webpages.",
                        class_name="font-normal text-black text-sm",
                    ),
                    class_name="flex flex-col items-center justify-center",
                ),
                rx.form.field(
                    rx.flex(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Full Name",
                                # type attribute is required for "typeMismatch" validation
                                type="name",
                                height="40px",
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
                    width="100%",
                ),
                rx.form.field(
                    rx.flex(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Email Address",
                                # type attribute is required for "typeMismatch" validation
                                type="email",
                                height="40px",
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
                    width="100%",
                ),
                rx.form.field(
                    rx.flex(
                        rx.form.control(
                            rx.input.input(
                                placeholder="Enter your password",
                                type="password",
                                min_length=8,
                                height="40px",
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
                    width="100%",
                ),
                rx.form.submit(
                    rx.button(
                        "Create Account",
                        class_name="border w-full h-[45px] border-black rounded-lg text-lg font-bold items-center justify-center text-white bg-black p-1.5 cursor-pointer",
                    ),
                    as_child=True,
                    display="flex",
                    align_items="center",
                    width="180px",
                    justify_content="center",
                ),
                rx.box(
                    rx.text(
                        "Already have an Account?",
                        class_name="font-normal text-black text-sm",
                    ),
                    rx.text(
                        "Sign In",
                        class_name="text-decoration-line: underline font-normal text-[#4193F3] text-sm cursor-pointer",
                        on_click=redirect_to_signin,
                    ),
                    class_name="flex justify-center gap-1 items-center",
                ),
                on_submit=RadixFormSubmissionState.handle_submit,
                padding="20px 20px 20px 20px",
                width="400px",
                display="flex",
                background_color="white",
                flex_direction="column",
                justify_content="center",
                align_items="center",
                gap="20px",
                border="1px solid #DBF0FF",
                border_radius="10px",
            ),
            class_name="flex gap-8 flex-col z-50 justify-center items-center",
        ),
        rx.box(
            rx.image(
                src="/left_rectangle.png",
                alt="Descriptive text about the image",
                height="300px",
            ),
            class_name="w-full flex justify-end items-center absolute bottom-0",
        ),
        class_name="h-screen w-full flex items-center justify-center flex-col bg-[#DBF0FF] relative",
    )
