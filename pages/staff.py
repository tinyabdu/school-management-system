import flet as ft
from utilities.bar import bar

def staff(page: ft.Page):
    
    
   
    TeacherName = ft.TextField(
        label="name",
        width=450,
        border_radius=8,
        hint_text="flet dev"
    )
    
    TeacherEmail = ft.TextField(
        label="email",
        width=450,
        border_radius=8,
        hint_text="flet@example.com"
    )
    
    TeacherAddress = ft.TextField(
        label="address",
        width=450,
        max_lines=5,
        min_lines=5,
        hint_text="address"
    )
    
    TeacherDOB = ft.TextField(
        label="DOB",
        width=450,
        border_radius=8
    )
    
    TeacherPhone = ft.TextField(
        label="phone",
        hint_text="+234 81 6657 9829",
        width=450,
        border_radius=8
    )
    
    TeacherCity = ft.TextField(
        label="city",
        width=450,
        border_radius=8,
        hint_text="kaduna nigeria"
    )
    
    TeacherEduUniversity = ft.TextField(
        label="University",
        hint_text="university attendent",
        width=450,
        border_radius=8
    )
    
    TeacherEduYearStart = ft.TextField(
        label="Start and End Date",
        hint_text="year starting",
        width=220,
        border_radius=8
    )
    
    TeacherEduYearEnd = ft.TextField(
        label="Start and End Date",
        hint_text="year end",
        width=220,
        border_radius=8
    )
    
    TeacherEduDegree = ft.TextField(
        label="degree",
        hint_text="university attendent",
        width=450,
        border_radius=8
    )
    
    TeacherEduCity = ft.TextField(
        label="city",
        hint_text="university location",
        width=450,
        border_radius=8
    )
    
    return ft.View(
        "/staff",
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
                            scroll=ft.ScrollMode.ADAPTIVE,
                            controls=[
                                ft.Container(
                                    width=page.width  - 210,
                                    padding=10,
                                    content=ft.Row(
                                        alignment="spacebetween",
                                        controls=[
                                            ft.Text("Add New Teacher"),
                                            ft.Row(
                                                controls=[
                                                    ft.Text("School"),
                                                    ft.Icon("person")
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    height=40,
                                    width=500,
                                    bgcolor="blue",
                                    border_radius=8,
                                    padding=10,
                                    alignment=ft.alignment.center_left,
                                    content=ft.Text("Teacher Details"),
                                ),
                                ft.Card(
                                    surface_tint_color="blue",
                                    content=ft.Container(
                                        border_radius=8,
                                        width=page.width  - 250,
                                        height=500,
                                        content=ft.Row(
                                            vertical_alignment="center",
                                            alignment="center",
                                            spacing=40,
                                            controls=[
                                                ft.Column(
                                                    alignment="center",
                                                    spacing=25,
                                                    controls=[
                                                        TeacherName,
                                                        TeacherEmail,
                                                        TeacherAddress,
                                                        TeacherDOB
                                                    ]
                                                ),
                                                ft.Column(
                                                    alignment="center",
                                                    spacing=25,
                                                    controls=[
                                                        TeacherPhone,
                                                        ft.Container(
                                                            content=ft.Icon(
                                                                size=200,
                                                                name="image"
                                                            )
                                                        ),
                                                        TeacherCity
                                                    ]
                                                ),
                                            ]
                                        )
                                    )
                                ),
                                ft.Container(
                                    height=40,
                                    width=500,
                                    bgcolor="blue",
                                    border_radius=8,
                                    padding=10,
                                    alignment=ft.alignment.center_left,
                                    content=ft.Text("Education"),
                                ),
                                ft.Card(
                                    surface_tint_color="red",
                                    content=ft.Container(
                                        border_radius=8,
                                        width=page.width - 250,
                                        height=250,
                                        content=ft.Row(
                                            spacing=40,
                                            alignment="center",
                                            vertical_alignment="center",
                                            controls=[
                                                ft.Column(
                                                    alignment="center",
                                                    spacing=25,
                                                    controls=[
                                                        TeacherEduUniversity,
                                                        ft.Row(
                                                            controls=[
                                                                TeacherEduYearStart,
                                                                TeacherEduYearEnd,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                ft.Column(
                                                    alignment="center",
                                                    spacing=25,
                                                    controls=[
                                                        TeacherEduDegree,
                                                        TeacherEduCity
                                                    ]
                                                )
                                            ]
                                        )
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.all(25),
                                    width=page.width - 250,
                                    alignment=ft.alignment.top_right,
                                    content=ft.ElevatedButton("Save", width=200, height=45)
                                )
                            ]
                        )
                    ),
                ]
            ),

        ]
    )