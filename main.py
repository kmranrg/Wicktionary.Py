import flet as ft

def main(page: ft.Page):
    # setting the app title
    page.title="Wicktionary"

    # enabling scroll in the page
    page.scroll="hidden"

    # setting the app background color
    page.theme_mode="light"

    # show BottomSheet function
    def show_bs(e):
        bs.open=True
        bs.update()

    def search_click(e):
        pass

    # search
    search_word = ft.TextField(hint_text="search anything...", color="#038F75", border_color="#038F75", expand=True)
    search_button = ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=search_click)

    # BottomSheet for Developer Info
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Developer: Anurag || Inspired By: Bhavani", color=ft.colors.WHITE),
                ],
                tight=True,
                horizontal_alignment="center"
            ),
            padding=10,
            bgcolor="#04705C"
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

    page.add(
        ft.Row(
            [
                search_word,
                search_button
            ],
            alignment="center"
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)