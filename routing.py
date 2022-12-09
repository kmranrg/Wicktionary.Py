import flet as ft
from wicktionary import Wicktionary

class AppRouting(Wicktionary):
    def __init__(self, page):
        super().__init__(page)
        
        # setting the routing variables
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(self.page.route)

    # routing functionality
    def route_change(self,route):
        self.page.views.clear()
        self.page.views.append(
            ft.View(
                "/",
                [
                    self.welcome_page,
                ],
                bgcolor="#038F75",
            )
        )
        if self.page.route == "/homepage":
            self.page.views.append(
                ft.View(
                    "/homepage",
                    [
                        self.app_bar,
                        ft.Row(
                            [
                                self.search_word,
                                self.search_button
                            ],
                            alignment="center"
                        ),
                        self.definitions_list_view,
                        self.developer_view,
                        self.navigation_bar,
                    ],
                )
            )
        self.page.update()

    def view_pop(self,view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)