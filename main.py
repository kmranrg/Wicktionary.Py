import flet as ft

def main(page: ft.Page):
    # setting the app title
    page.title = "Wicktionary"

    # setting the app background color
    page.bgcolor = "#FFFFFF"

    # show BottomSheet function
    def show_bs(e):
        bs.open = True
        bs.update()

    # BottomSheet for Developer Info
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Developer: Kumar Anurag || Instagram: kmranrg"),
                ],
                tight=True,
                horizontal_alignment="center"
            ),
            padding=10,
        ),
        open=False,
    )
    page.overlay.append(bs)

    # app bar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.BOOK),
        leading_width=40,
        title=ft.Text("Wicktionary"),
        color="#FFFFFF",
        center_title=False,
        bgcolor="#038F75",
        actions=[
            ft.IconButton(ft.icons.PERSON, icon_color=ft.colors.WHITE, on_click=show_bs),
        ],
    )

    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)