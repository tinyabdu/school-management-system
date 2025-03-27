import flet as ft


class Card(ft.Card):
    def __init__(self, section: ft.Text, icon: ft.Icon, Class: ft.Text, classno: ft.Text, card_color: str):
        super().__init__(
            surface_tint_color=card_color,
            content=ft.Container(
                width=300,
                height=130,
                border_radius=6,
                padding=10,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        ft.Container(content=ft.Text(f"{section} 1, 2, 3, 4, 5")),
                        ft.Row(
                            controls=[
                                icon,
                                ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.Text(Class, size=20),
                                        ft.Text(f"{classno} pupils")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
        )
        