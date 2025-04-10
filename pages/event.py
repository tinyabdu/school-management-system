import flet as ft 
from utilities.bar import bar

def event(page:ft.Page):
    
    return ft.View(
        "/event",
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
                        content=ft.Column(controls=[ft.ElevatedButton("analys")])
                    )
                ]
            ),
        ]
    )