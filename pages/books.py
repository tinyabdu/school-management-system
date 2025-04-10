import flet as ft
from utilities.bar import bar 

def book(page:ft.Page):
    return ft.View(
        "/book",
        padding=0,
        controls=[
            ft.Row(
                expand=True,
                controls=[
                    ft.Container(
                        height=page.height,
                        width=200,
                        content=bar
                    ),
                                
                    ft.Container(
                        height=page.height,
                        width=page.width,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    border_radius=8,
                                    alignment=ft.alignment.center,
                                    height=200,
                                    width=page.width - 220,
                                    bgcolor="#000066",
                                    content=ft.Text("school library")
                                ),
                                ft.Container(
                                    height=page.height,
                                    width=page.width - 220,
                                    content=ft.Row(
                                        alignment="spacebetween",
                                        controls=[
                                            ft.GridView(
                                                controls=[
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                    ft.Icon("home"),
                                                ]
                                            ),
                                            ft.Card(
                                                width=200,
                                                content=ft.Container(
                                                    content=ft.Text("hello")
                                                )
                                            ),
                                            
                                        ]
                                    )
                                ),
                                
                            ]
                            
                        )
                    )
                ]
            ),
        ]
    )