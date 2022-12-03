import flet as ft
import requests

def main(page: ft.Page):
    # setting the app title
    page.title="Wicktionary"

    # enabling scroll in the page
    page.auto_scroll=True

    # setting the app background color
    page.theme_mode="light"
    page.theme = ft.theme.Theme(color_scheme_seed="#038F75")

    # show BottomSheet function
    def show_bs(e):
        bs.open=True
        bs.update()

    # search functionality
    def search_click(e):
        definitions_list_view.clean()
        json_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{search_word.value}")
        if search_word.value.lower() == "bhavani":
            definitions_list_view.controls.append(
                ft.Container(
                    ft.Column(
                                    controls=[
                                        ft.Text(f"bhavani", style="titleMedium", weight="bold", color=ft.colors.BLUE_GREY),
                                        ft.Text(f"an amazing friend", style="titleMedium", italic=False, color=ft.colors.RED),
                                        ft.Text(f"The most beautiful and cute girl on the planet.", style="titleMedium", color=ft.colors.BLUE_GREY),
                                    ]
                                ),
                                margin=5,
                                padding=10,
                                border_radius=ft.border_radius.all(20),
                                bgcolor="#DFF7F3",
                )
            )
        else:
            try:
                if json_response.json()['title'] == "No Definitions Found":
                    definitions_list_view.controls.append(
                        ft.Container(
                            ft.Text(f"Oops! no definitions found, please re-check the word...", style="titleMedium", color=ft.colors.BLUE_GREY),
                            margin=5,
                            padding=10,
                            border_radius=ft.border_radius.all(20),
                            bgcolor="#DFF7F3",
                        )
                    )
            except:
                for i in json_response.json():
                    for j in i['meanings'][0]['definitions']:
                        definitions_list_view.controls.append(
                            ft.Container(
                                ft.Column(
                                    controls=[
                                        ft.Text(f"{i['word']}", style="titleMedium", weight="bold", color=ft.colors.BLUE_GREY),
                                        ft.Text(f"as {i['meanings'][0]['partOfSpeech']}", style="titleMedium", italic=False, color=ft.colors.RED),
                                        ft.Text(f"{j['definition']}", style="titleMedium", color=ft.colors.BLUE_GREY),
                                    ]
                                ),
                                margin=5,
                                padding=10,
                                border_radius=ft.border_radius.all(20),
                                bgcolor="#DFF7F3",
                            )
                        )
        page.update()

    # search
    search_word = ft.TextField(hint_text="search anything...", color="#038F75", border_color="#038F75", cursor_color="#04705C", selection_color="#DFF7F3")
    search_button = ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=search_click, bgcolor="#DFF7F3")
    definitions_list_view = ft.ListView(expand=True, spacing=10)

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
        ),
        definitions_list_view,
    )

ft.app(target=main, view=ft.WEB_BROWSER)