import flet as ft
import requests

class Wicktionary(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

        # search text field
        self.search_word = ft.TextField(
            hint_text="search anything...", 
            border_radius=20, 
            color="#038F75", 
            border_color="#038F75", 
            cursor_color="#04705C", 
            selection_color="#DFF7F3", 
            on_submit=lambda e: self.search_click(e),
        )

        # search button
        self.search_button = ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=self.search_click, bgcolor="#DFF7F3")
        
        # search view
        self.definitions_list_view = ft.ListView(expand=True, spacing=10)

        # developer view
        self.developer_view = ft.Column(
            controls=[
                ft.Image(
                    src="dev/dev.png",
                    width=250,
                    height=250,
                ),
                ft.Row(
                    [
                        ft.Text(
                            "Inspiration: Bhavani\nDeveloper: Anurag",
                            font_family="CabinSketchRegular",
                            text_align="center",
                            style="titleLarge",
                            weight="bold",
                        ),
                    ],
                    alignment="center"
                ),
                ft.Text(
                    "Copyright Ⓒ All rights reserved",
                    font_family="CabinSketchRegular",
                    text_align="center",
                    style="titleSmall",
                    weight="bold",
                    color=ft.colors.RED_900,
                ),
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True,
        )

        # setting the inital developer view to False
        self.developer_view.visible = False

        # welcome page
        self.welcome_page = ft.Column(
            controls = [
                ft.Row([ft.Text("WICKTIONARY", font_family="CabinSketchBold", color="#FFFFFF", style="displayMedium", text_align="center")],alignment="center"),
                ft.Image(
                    src="logo/app_logo.jpg",
                    width=300,
                    height=300,
                ),
                ft.ElevatedButton(content=ft.Row([ft.Text("LAUNCH DICTIONARY",font_family="CabinSketchRegular", weight="bold"),ft.Icon(ft.icons.LAUNCH)], alignment="center",width=200), on_click=lambda e: self.go_to_homepage(e)),
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True,
        )

        # app bar
        self.app_bar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK_IOS_SHARP, icon_color="#FFFFFF", on_click=lambda _: self.page.go("/")),
            leading_width=40,
            title=ft.Text("WICKTIONARY", font_family="CabinSketchBold"),
            color="#FFFFFF",
            center_title=False,
            bgcolor="#038F75",
            toolbar_height=60,
        )

        # navigation bar
        self.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.HOME_OUTLINED,
                    selected_icon=ft.icons.HOME,
                    label="Home",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.PERSON_OUTLINE,
                    selected_icon=ft.icons.PERSON,
                    label="Developer",
                ),
            ],
            on_change=lambda e: self.developer_info(e),
            height=60,
            bgcolor="#FFFFFF"
        )

    # search functionality
    def search_click(self,e):
        self.definitions_list_view.clean()
        json_response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{self.search_word.value}")
        if self.search_word.value.lower() == "bhavani":
            self.definitions_list_view.controls.append(
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
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.Alignment(0.8, 1),
                        colors=[
                            "0xDFF7F3",
                            "0xFFFFFF",
                        ],
                    ),
                )
            )
        else:
            try:
                if json_response.json()['title'] == "No Definitions Found":
                    self.definitions_list_view.controls.append(
                        ft.Container(
                            ft.Text(f"Oops! no definitions found, please re-check the word...", style="titleMedium", color=ft.colors.BLUE_GREY),
                            margin=5,
                            padding=10,
                            border_radius=ft.border_radius.all(20),
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.top_left,
                                end=ft.Alignment(0.8, 1),
                                colors=[
                                    "0xDFF7F3",
                                    "0xFFFFFF",
                                ],
                            ),
                        )
                    )
            except:
                for i in json_response.json():
                    for j in i['meanings'][0]['definitions']:
                        self.definitions_list_view.controls.append(
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
                                gradient=ft.LinearGradient(
                                    begin=ft.alignment.top_left,
                                    end=ft.Alignment(0.8, 1),
                                    colors=[
                                        "0xDFF7F3",
                                        "0xFFFFFF",
                                    ],
                                ),
                            )
                        )
        self.page.update()

    # enabling the developer view
    def developer_info(self, e):
        if e.control.selected_index == 1:
            self.search_word.visible = False
            self.search_button.visible = False
            self.definitions_list_view.visible = False
            self.developer_view.visible = True
        else:
            self.search_word.visible = True
            self.search_button.visible = True
            self.definitions_list_view.visible = True
            self.developer_view.visible = False
        self.page.update()

    # page route to homepage from welcome page
    def go_to_homepage(self, e):
        self.search_word.visible = True
        self.search_button.visible = True
        self.definitions_list_view.visible = True
        self.developer_view.visible = False
        self.navigation_bar.selected_index = 0
        self.page.go("/homepage")