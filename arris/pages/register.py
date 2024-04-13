import reflex as rx


from arris.schemas.user import add_user


class RadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        print(form_data)

        add_user(
            email=form_data["email"],
            full_name=form_data["name"],
            password=form_data["user_password"],
        )

    @rx.var
    def form_data_keys(self) -> list:
        return list(self.form_data.keys())

    @rx.var
    def form_data_values(self) -> list:
        return list(self.form_data.values())


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
            on_submit=RadixFormSubmissionState.handle_submit,
        ),
        # rx.divider(size="4"),
        # rx.text(
        #     "Results",
        #     weight="bold",
        # ),
        # rx.foreach(
        #     RadixFormSubmissionState.form_data_keys,
        #     lambda key, idx: rx.text(
        #         key,
        #         " : ",
        #         RadixFormSubmissionState.form_data_values[idx],
        #     ),
        # ),
    )
