import reflex as rx


from arris.schemas.user import AddUser


# class RegisterState(rx.State):
#     name: str = ""
#     username: str = ""
#     email: str = ""
#     password: str = ""


def handle_submit(form_data: dict):
    # Your submission logic here
    print(form_data.to_string())
    return rx.window_alert("Form submitted successfully")


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
                name="user_password",
            ),
            rx.form.submit(
                rx.button("Submit"),
                as_child=True,
            ),
            on_submit=handle_submit,
            reset_on_submit=True,
        ),
    )
