import flet as ft 
from utilities.bar import bar

def grade(page: ft.Page):
    
    StudentNurseryNo: int = 240
    StudentPrimaryNo: int = 360
    StudentSecondaryNo: int = 540
    
   
    return ft.View(
        "/grade",
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
                            alignment=ft.alignment.top_left,
                            spacing=25,
                            controls=[
                                ft.Container(content=ft.Text("Graduation student"), padding=10),     
                                ft.Card(
                                    content=ft.Container(
                                        padding=10,
                                        width=450,
                                        content=ft.Row(
                                            spacing=3,
                                            controls=[
                                                ft.Icon("Group", size=40),
                                                    ft.Column(
                                                        spacing=0,
                                                        controls=[
                                                            ft.Text("Total student", size=11),
                                                            ft.Text(f"{StudentNurseryNo + StudentPrimaryNo + StudentSecondaryNo}", size=20),
                                                                    
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                ),
                                ft.Card(
                                    width=500,
                                    height=150,
                                    surface_tint_color="green",
                                    #margin=40,
                                    content=ft.Container(
                                    #alignment=ft.alignment.top_center,
                                        content=ft.Column(
                                            controls=[
                                                ft.DataTable(
                                                    columns=[
                                                        ft.DataColumn(label=ft.Text("Name")),
                                                        ft.DataColumn(label=ft.Text("Class")),
                                                        ft.DataColumn(label=ft.Text("Number")),
                                                        ft.DataColumn(label=ft.Text("Grade")),
                                                    ]
                                                 )
                                            ]
                                        )
                                    )
                                ),        
                            ]
                        )
                    )
                ]
            ),
        ]
    )