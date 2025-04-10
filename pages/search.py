import flet as ft
from utilities.bar import bar

def search(page:ft.Page):
    
    dbtable = ft.DataTable(
        show_bottom_border=True,
        columns=[
            ft.DataColumn(label=ft.Text("Regno")),
            ft.DataColumn(label=ft.Text("Section")),
            ft.DataColumn(label=ft.Text("Class")),
            ft.DataColumn(label=ft.Text("Performance")),
            ft.DataColumn(label=ft.Text("Status")),
    
        ]
    )
    return  ft.View(
        "/search",
        padding=0,
        controls=[
            ft.Row(
                spacing=10,
                expand=True,
                controls=[
                    ft.Container(
                        height=page.height,
                        width=200,
                        content=bar
                    ),
                                
                    ft.Container(
                        expand=True,
                        height=page.height,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    border_radius=8,
                                    height=150,
                                    width=page.width,
                                    bgcolor="#000066",
                                    content=ft.Row(
                                        alignment="center",
                                        spacing=25,
                                        controls=[
                                            ft.Text("Search Student", weight="bold", size=25, font_family="Arial", opacity=0.4, color="white"),
                                            ft.SearchBar(bar_hint_text="search")
                                        ]
                                    )
                                ),
                                ft.Container(
                                    width=page.width,
                                    content=dbtable
                                ),
                                
                            ]
                        )
                    )
                ]
            ),
        ]
    )