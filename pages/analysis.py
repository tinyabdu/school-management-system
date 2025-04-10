import flet as ft 
from utilities.bar import bar
from utilities.utility import Card

def analysis(page: ft.Page):
    
    StudentNurseryNo: int = 240
    StudentPrimaryNo: int = 360
    StudentSecondaryNo: int = 540
    
   
    return ft.View(
        "/analysis",
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
                            padding=ft.padding.only(left=35, top=15),
                            content=ft.Column(
                                controls=[
                                    ft.Row(
                                        spacing=35,
                                        controls=[
                                            Card(
                                                section="nursery",
                                                icon="person",
                                                Class="Nursery",
                                                classno=StudentNurseryNo,
                                                card_color="green"
                                            ),
                                            Card(
                                                section="primary",
                                                icon="person",
                                                Class="Primary",
                                                classno=StudentPrimaryNo,
                                                card_color="red"
                                            ),
                                            Card(
                                                section="secondary",
                                                icon="person",
                                                Class="Secondary",
                                                classno=StudentSecondaryNo,
                                                card_color="blue"
                                            ),

                                        ]
                                    ),
                                ft.Container(
                                    content=ft.Row(
                                        spacing=5,
                                        controls=[
                                            ft.Card(
                                                ft.Container(
                                                    width=200,
                                                    height=150,
                                                    padding=10,
                                                    content=ft.Column(
                                                        alignment="center",
                                                        horizontal_alignment="center",
                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Container(width=30, height=15, bgcolor="green"),
                                                                    ft.Text("Nursery"),
                                                                ]
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Container(width=30, height=15, bgcolor="red"),
                                                                    ft.Text("Primary"),
                                                                ]
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Container(width=30, height=15, bgcolor="blue"),
                                                                    ft.Text("Secondary"),
                                                                ]
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ),
                                                        
                                        ]   
                                    )
                                ),
                                #chart
                                ft.PieChart(
                                    sections=[
                                        ft.PieChartSection(value=StudentNurseryNo, color="green"),
                                        ft.PieChartSection(value=StudentPrimaryNo, color="red"),
                                        ft.PieChartSection(value=StudentSecondaryNo, color="blue"),
                                    ] 
                                )
                            ]
                        )
                    )
                ]
            ),          
        ]
    )