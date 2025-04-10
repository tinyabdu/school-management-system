import flet as ft 
from utilities.bar import bar
from utilities.utility import PaymentCard

def payment(page: ft.Page):
    
    StudentNurseryNo: int = 240
    StudentPrimaryNo: int = 360
    StudentSecondaryNo: int = 540
    
    StudentNurseryLoan: float = 200.000
    StudentPrimaryLoan: float = 300.000
    StudentSecondaryLoan: float = 150.000
    
    
    regno = ft.TextField(
        label="RehNo",
        icon="FIND_IN_PAGE",
        border_radius=8
    )
    
    fees = ft.AlertDialog(
        content=ft.Container(
            width=200,
            height=200,
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    ft.Text("pay"),
                    regno
                ]
            )
        )
    )   
    
    
    
    return ft.View(
        "/payment",
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
                                ft.Container(
                                    width=page.width - 210,
                                    padding=10,
                                    content=ft.Row(
                                        alignment="spacebetween",
                                        controls=[
                                            ft.Text("School Fees", size=35, weight="bold", font_family="Arial"),
                                            ft.OutlinedButton(
                                                "Pay Me",
                                                height=60,
                                                width=150,
                                                on_click=lambda e: page.open(fees),
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    margin=20,
                                    content=ft.Row(
                                        controls=[
                                            PaymentCard(
                                                class_name="nursery",
                                                card_color="green",
                                                total_student=StudentNurseryNo,
                                                price=30000,
                                                loan=StudentNurseryLoan
                                                            
                                            ),
                                            PaymentCard(
                                                class_name="primary",
                                                card_color="blue",
                                                total_student=26,
                                                price=180,
                                                loan=2456
                                                            
                                            ),
                                            PaymentCard(
                                                class_name="Primary",
                                                card_color="red",
                                                total_student=StudentSecondaryNo,
                                                price=38999,
                                                loan=StudentSecondaryLoan
                                            ),
                                              
                                                        
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            ),
        ]
    )