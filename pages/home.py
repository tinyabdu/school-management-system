import flet as ft 
import time
from datetime import datetime
from utilities.bar import bar

def home(page: ft.Page):
    
    StudentFirstName = ft.TextField(
        label="Firstname",
        border_radius=8,
        width=300
    )
    
    StudentLastName = ft.TextField(
        label="Surname",
        border_radius=8,
        width=300
    )
    
    StudentEmail = ft.TextField(
        label="Email",
        border_radius=8,
        width=300
    )
    
    StudentBloadGroup = ft.Dropdown(
        border_radius=8,
        label="Blood Group",
        width=300,
        options=[
            ft.dropdown.Option("O"),
            ft.dropdown.Option("A"),
            ft.dropdown.Option("B"),
        ]
    )
    
    StudentBloodType = ft.Dropdown(
        border_radius=8,
        label="Blood Type",
        width=300,
        options=[
            ft.dropdown.Option("AA"),
            ft.dropdown.Option("AS"),
            ft.dropdown.Option("SS"),
        ]
    )
    
    StudentCountry = ft.Dropdown(
        border_radius=8,
        label="Country",
        width=300,
        options=[
            ft.dropdown.Option("Nigeria"),
            ft.dropdown.Option("Ghana"),
            ft.dropdown.Option("Rwanda"),
            ft.dropdown.Option("Mali"),
            ft.dropdown.Option("Niger"),
            ft.dropdown.Option("US"),
            ft.dropdown.Option("Mexico"),
            ft.dropdown.Option("Columbia"),
            ft.dropdown.Option("Syria"),
            ft.dropdown.Option("Iran"),
            ft.dropdown.Option("Pakistan"),
            ft.dropdown.Option("India"),
            
        ]
    )
    
    Gender = ft.Dropdown(
        border_radius=8,
        label="Gender",
        width=300,                 
        options=[
            ft.dropdown.Option("Male"),
            ft.dropdown.Option("Female"),
        ]
    )
    
    dop_tx = ft.Text()
        
    def handle_date_change(e: ft.ControlEvent):
        dop_tx.value = f"date is {e.control.value.strftime('%y-%m-%d')}"
        #page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d %H:%M %p')}"))

 
    
    DateBirth = ft.ElevatedButton(
        "DOB",
        width=300,
        height=40,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime(year=2000, month=12, day=1),
                last_date=datetime(year=3000, month=12, day=1),
                on_change=handle_date_change,
            )
        )
    )
    
    #parent infromation
    ParentName = ft.TextField(
        label="parent name",
        border_radius=8,
        width=300,
    )
    
    ParentEmail = ft.TextField(
        label="parent email",
        border_radius=8,
        width=300
    )
    
    ParentOccupation = ft.TextField(
        label="parent job",
        border_radius=8,
        width=300
    )
    
    Address = ft.TextField(
        label="address",
        border_radius=8,
        width=300
    )
    
    Section = ft.Dropdown(
        label="section",
        width=300,
        options=[
            ft.dropdown.Option("Nusery"),
            ft.dropdown.Option("Primary"),
            ft.dropdown.Option("Secondary"),
        ],
        
    )
    
    def handle_class(e):
        selected_value = Class.value
        if selected_value == "JSS":
            Class_level.options=[ft.dropdown.Option(f"jss {in_}") for in_ in range(1, 4)] 
        elif selected_value == "SSS":
            Class_level.options=[ft.dropdown.Option(f"sss {in1_}") for in1_ in range(1, 4)]
        elif selected_value == "PRIMARY":
            Class_level.options=[ft.dropdown.Option(f"primary {in2_}") for in2_ in range(1, 6)]
        elif selected_value == "NUSERY":
            Class_level.options=[ft.dropdown.Option(f"nusery {in3_}") for in3_ in range(1, 4)]
            page.update()
    
    Class = ft.Dropdown(
        label="class",
        width=300,
        options=[
            ft.dropdown.Option("NUSERY"),
            ft.dropdown.Option("PRIMARY"),
            ft.dropdown.Option("JSS"),
            ft.dropdown.Option("SSS"),
        ],
        on_change=handle_class
    )
    
    
    Class_level = ft.Dropdown(
        label="class type",
        width=300,
        options=[ft.dropdown.Option(f"{Class.value} {class_}") for class_ in range(1, 4)], 
    )
    
    def Register(e):
        alert.modal = False
        page.open(
            ft.AlertDialog(
                content=ft.Container(
                    width=100,
                    height=100,
                    alignment=ft.alignment.center,
                    content=ft.Icon(name="done", size=100, color="green")
                )
            )
        )
        page.update()
        time.sleep(0.8)
        
    def pic_image(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()
        
    file_picker = ft.FilePicker(on_result=pic_image)
    selected_files = ft.Text("image name")
    
    page.overlay.append(file_picker)
    
    def image_hover(e):
        e.control.content = ft.Icon("home") 
        page.update()
  
    
    alert = ft.AlertDialog(
        content=ft.Container(
            padding=ft.padding.all(15),
            height=650,
            width=650,
            content=ft.Column(
                scroll=ft.ScrollMode.ALWAYS,
                alignment="center",
                horizontal_alignment="center",
                controls=[
                    ft.Container(
                        height=40,
                        width=100,
                        bgcolor="blue",
                        border_radius=8,
                        padding=10,
                        alignment=ft.alignment.center,
                        content=ft.Text("Add student")
                    ),
                    ft.Row(
                        alignment="center",
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        height=40,
                                        width=200,
                                        bgcolor="blue",
                                        border_radius=8,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        content=ft.Text("Student information")
                                    ),
                                    StudentFirstName,
                                    StudentLastName,
                                    StudentEmail,
                                    StudentCountry,
                                    StudentBloadGroup,
                                    StudentBloodType,
                                    dop_tx,
                                    DateBirth,
                                    Gender
                                ]
                            ),
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        height=40,
                                        width=200,
                                        bgcolor="blue",
                                        border_radius=8,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        content=ft.Text("Parent information")
                                    ),
                                    ParentName,
                                    ParentEmail,
                                    ParentOccupation,
                                    Address,
                                ]
                            )
                        ]
                    ),
                    ft.Container(
                        alignment=ft.alignment.top_left,
                        padding=10,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    height=40,
                                    width=200,
                                    bgcolor="blue",
                                    border_radius=8,
                                    padding=10,
                                    alignment=ft.alignment.center,
                                    content=ft.Text("School Details")
                                ),
                                Section,
                                Class,
                                Class_level,
                                selected_files,
                                ft.Container(
                                    on_hover=image_hover,
                                    on_click=lambda e: file_picker.pick_files(),
                                    content=ft.Icon(
                                        size=200,
                                        name="image"
                                    )
                                )
                            ]
                        )
                    ),
                    ft.OutlinedButton(
                        "Register",
                        height=60,
                        width=400,
                        on_click=Register
                    )
                    
                ]
            )
        )
    )
    
    dbtable = ft.DataTable(
        show_bottom_border=True,
        columns=[
            ft.DataColumn(label=ft.Text("firstname")),
            ft.DataColumn(label=ft.Text("lastname")),
            ft.DataColumn(label=ft.Text("email")),
            ft.DataColumn(label=ft.Text("phone number")),
            ft.DataColumn(label=ft.Text("admission number")),
            ft.DataColumn(label=ft.Text("section")),
            ft.DataColumn(label=ft.Text("address")),
    
        ]
    )
    
   
    return ft.View(
        "/home",
        floating_action_button=ft.FloatingActionButton(
            icon="add",
            hover_elevation=32,
            on_click=lambda e: page.open(alert)
        ),
        padding=0,
        controls=[
            ft.Row(
                expand_loose=1,
                spacing=0,
                expand=True,
                controls=[
                    ft.Container(
                        height=page.height,
                        width=200,
                        content=bar
                    ),      
                    ft.Container(
                        height=page.height,
                        width=page.width - 200,
                        content=dbtable
                    )
                ]
            ),
        ]
    )