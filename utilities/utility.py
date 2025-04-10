import flet as ft



class Section:
    @staticmethod
    def class_value(class_name: str):
        match class_name:
            case "nursery":
                return "Nursery 1, 2, 3"
            case "primary":
                return "Primary 1, 2, 3, 4, 5"
            case "secondary":
                return "SSS, JSS, 1, 2, 3, 1, 2, 3"
            case _:
                return "your value must be nursery, primary, secondary"




class Card(ft.Card):
    
    def __init__(self, section: str, icon: str, Class: str, classno: str, card_color: str):
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
                        ft.Container(content=ft.Text(f"{Section.class_value(section)}")),
                        ft.Row(
                            controls=[
                                ft.Icon(icon, size=50),
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
        
class PaymentCard(ft.Card):
    def __init__(self, class_name: str, price: int, card_color: str, total_student: int, loan: int):
        super().__init__(
            surface_tint_color=card_color,
            content=ft.Container(
                width=300,
                height=130,
                border_radius=6,
                padding=10,
                content=ft.Column(
                    alignment="spacebetween",
                    controls=[
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Row(
                                    alignment="spacebetween",
                                    controls=[
                                        ft.Text(f"{class_name}", size=25),
                                        ft.Text(f"{price}", weight="bold", color="BLUE_800", size=30)
                                    ]
                                ),
                                ft.Row(
                                    alignment="spacebetween",
                                    controls=[
                                        ft.Text(f"total student {total_student}", size=12),
                                        ft.Text(f"total fee {price * total_student:.2f}")
                                    ]
                                )
                            ]
                        ),
                        ft.Row(
                            alignment="spacebetween",
                            controls=[
                                ft.Text("Loan"),
                                ft.Text(f"{loan}")
                            ]
                        )
                    ]
                )
            )
        )
        

