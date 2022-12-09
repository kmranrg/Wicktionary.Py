import flet as ft
from routing import AppRouting

def main(page: ft.Page):
    # setting the app title
    page.title = "Wicktionary"

    # enabling scroll in the page
    page.auto_scroll = True

    # setting the app background color
    page.theme_mode = "light"
    page.theme = ft.theme.Theme(color_scheme_seed="#038F75")

    # setting the custom font
    page.fonts = {
        "CabinSketchBold": "fonts/CabinSketchBold.ttf",
        "CabinSketchRegular": "fonts/CabinSketchRegular.ttf"
    }

    app = AppRouting(page)

    page.add(app)

ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")