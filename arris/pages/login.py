import reflex as rx
from passlib.hash import pbkdf2_sha256
from arris.utils import ClientStorageState
from arris.protected import not_require_login


from arris.schemas.user import get_user

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
class LoginState(ClientStorageState):
    is_loading= False
    form_data: dict

    def validate_email(self, email: str) -> bool:
        """Validate the email format using a regex pattern."""
        return rx.match(EMAIL_REGEX, email) is not None

    def handle_submit(self, form_data: dict):

        if form_data["email"] is "" or form_data["password"] is "":
            return rx.window_alert("Please fill all the fields")

        self.is_loading = True
        user = get_user(
            email=form_data["email"],
        )

        self.is_loading = False

        if user and pbkdf2_sha256.verify(form_data["password"], user.password):
            encoded = self.generate_token(form_data["email"])

            yield [rx.redirect("/home"), ClientStorageState.set_custom_cookie(encoded)]
        else:
            yield rx.window_alert("Invalid email or password")


@not_require_login
def login() -> rx.Component:

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
                rx.text("ARRIS", font_family="Integral CF", class_name="text-2xl font-bold text-black"),
                class_name="w-full flex gap-2 justify-center items-center",
            ),
            rx.form.root(
                rx.box(
                    rx.text("Sign In", class_name="font-bold text-2xl text-black pb-2"),
                    rx.text(
                        "Sign In account to access the world of",
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
                        rx.cond(LoginState.is_loading, "Loading...", "Continue"),
                         border="1px solid black",
                         height="45px",
                         border_radius="10px",
                         background_color="black",
                         color="white",
                         display="flex",
                         justify_content="center",
                         align_items="center",
                         padding="6px",
                         font_size="18px",
                         line_height="28px",
                         font_weight="700",
                    ),
                    as_child=True,
                    display="flex",
                    align_items="center",
                    width="180px",
                    justify_content="center",
                ),
                rx.box(
                    rx.text(
                        "Don't have an Account?",
                        class_name="font-normal text-black text-sm",
                    ),
                    rx.text(
                        "Create Account",
                        class_name="text-decoration-line: underline font-normal text-[#4193F3] text-sm cursor-pointer",
                        on_click=lambda: rx.redirect("/register"),
                    ),
                    class_name="flex justify-center gap-1 items-center",
                ),
                on_submit=LoginState.handle_submit,
                padding="20px 20px 20px 20px",
                width=["300px", "350px", "400px", "400px" "400px"],
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
