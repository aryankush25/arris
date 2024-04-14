import reflex as rx
from arris.services.shopify_page import ShopifyPageService
from arris.protected import require_login
from arris.utils import ClientStorageState


class ShopifyRadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):
        return ShopifyService.install_app(form_data["store_name"])

def createPage():
    return ShopifyPageService.craete_page("xg-dev", "ISHITA", "<h1>ARRIS</h1>")


@require_login
def home() -> rx.Component:

    return rx.box(
        rx.button(
            "Logout",
            color_scheme="ruby",
            on_click=ClientStorageState.logout,
        ),
        rx.button(
            "Craete Page",
            color_scheme="ruby",
            on_click=createPage,
        ),
        rx.form.root(
            rx.form.field(
                rx.flex(
                    rx.form.label("Store Name"),
                    rx.form.control(
                        rx.input.input(
                            placeholder="Store Name",
                            type="name",
                        ),
                        as_child=True,
                    ),
                    rx.form.message(
                        "Please enter a valid store name",
                        match="typeMismatch",
                    ),
                    direction="column",
                    spacing="2",
                ),
                name="store_name",
            ),
            rx.form.submit(
                rx.button("Connect Shopify"),
                as_child=True,
            ),
            on_submit=ShopifyRadixFormSubmissionState.handle_submit,
        ),
        # rx.button(
        #     "Test Page",
        #     color_scheme="ruby",
        #     on_click=ShopifyThemeService.publish_page_and_update_theme,
        # ),
        # rx.button(
        #     "Test",
        #     color_scheme="ruby",
        #     on_click=createStoreTheme(name='arris-ui',role='main',src="https://arris-aryankush25.s3.eu-north-1.amazonaws.com/theme_export__xg-dev-myshopify-com-spotlight__13APR2024-0426am.zip?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCmV1LW5vcnRoLTEiSDBGAiEA9%2Fv2i9YC20qK4V3E0iF3cby39V2dhHSS7yYi9GjPoigCIQCj74WsA8SY%2FUiKBmy%2FTtRVF6FeTaEYVRH45e7HciA7ISroAghyEAUaDDQwNDA4NzcxNzI2MCIMwFvtqUT8v7RqhldhKsUCWqPQOdBaPIXM8xODTZA4Tl6KYqHRh1cMT43eTuqJFfP%2BDPUbrFqb4kCknx1Qc2CC8e4rKtLg%2FLJlG2JVoe5Eo54e%2FwdJa42QxcW1iZbbVIa1AUzxbo7H%2FiXhDTPdkCZvXEltkQRm%2Flo25zKfNFaz%2BLsLytUFXWzD6l9JYXAhQbUBBWGLu%2BeCPbWeKHiS2yt4Le0OSOZIRpbpnRx%2FSJFczrzDTz1XVzbHSaOhh0VHdDhNHw5zIZeJjWPisAIFXA3sBikSfYPPErYvCiiSOS%2FT2JCt5RVdTnA%2FFx8iIvpEd5RVZvgTR%2F5gGZKCb7CxZ%2FYw3iD4bD%2BPo0bf6vKstqOroTWI6wTDU93OA6CEOVCXj4NsgBIAJQ7jYn28nlISkue%2BVyjeACu%2BwQdKXjqY9hvNJA6sUZ9RcZz0Xz0AReYcYgkonHqd6jDShemwBjqyAlneQLc%2F%2B4Y0IaSFiTIDe8KfEcr88rIeTqNSbq%2Bb%2Fd7iTmrvbFdmJIjt8QSr9aRFnosuPbE3nR0oolih9T3iT8pQUpplPQOePqNb0Ilb0HDEF10x82I2U5Z9UPzEQ8XYOk2f4EX%2Fn%2BW0Pzy2CINM40KNfXiI%2Fouy4GlNv%2Fv%2BzA5G4RJSz16ZxIKGAJEVPz%2BuwcVF5x%2FF2BNB9lxxpe%2FN8UXKkYEr%2BFccTnnBsVhQRCwaixX%2F4qX6sG5LYeCp%2Bl4wHVDFn0%2Bg4M59mQ6nPGb9yY2kuWOo2CTNINlzya4%2B5RkOR6oDi8jEmZvlsQOawJb80IMcTrfayolv5BW1fkft6NudLc%2FkLXAJpndSs0GvJNfdALJvmbxJwNWDbON2zVuymf2EYhDxcUSIsAZRbNj3XIhf1A%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240413T084911Z&X-Amz-SignedHeaders=host&X-Amz-Expires=43200&X-Amz-Credential=ASIAV4FMBHWGC6KS4SN3%2F20240413%2Feu-north-1%2Fs3%2Faws4_request&X-Amz-Signature=2dde30873c7fba598354baa24be612d79103e9e15939d4dc24b2a3809dc0a6a3",storeName='xg-dev'),
        # ),
    )
