import flet as ft
from utilities.bar import bar

def result(page:ft.Page):
    
    return ft.View(
        "/result",
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
                            controls=[
                                ft.ElevatedButton("reslt")
                            ]
                        )
                    )
                ]
            ),
        ]
    )