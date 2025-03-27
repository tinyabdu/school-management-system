import flet as ft
import time
import datetime

def main(page: ft.Page):
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary="black"),
        color_scheme_seed="#FF724C",
        icon_button_theme=ft.IconTheme(color="#2A2C41"),
        snackbar_theme=ft.SnackBarTheme(bgcolor="#2A2C41"),
        elevated_button_theme=ft.ElevatedButtonTheme(bgcolor="#FDBF50"),
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )
    page.theme = theme
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary="white"),
        color_scheme_seed="#FF724C",
        icon_button_theme=ft.IconTheme(color="#2A2C41"),
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )
    #page.theme_mode = "dark"
    page.update()
    

    
    
    page.add(ft.Container(
        alignment=ft.alignment.center,
        expand=True,
        content=ft.ProgressRing(stroke_width=5, bgcolor="blue")
    ))
    page.update()
    time.sleep(0.7)
   
    
    email = ft.TextField(
        icon="mail",
        label="email",
        hint_text="@example.com",
        width=450,
        border_radius=11
    )
    
    password = ft.TextField(
        icon="password",
        label="password",
        hint_text="your password",
        width=450,
        password=True,
        can_reveal_password=True,
        border_radius=11
    )
    def func_event(e):
        index = e.control.selected_index
        if index == 0:
            page.go("/home")
        if index == 1:
            page.go("/analysis")
        if index == 2:
            page.go("/grade")
        if index == 3:
            page.go("/payment")
        if index == 4:
            page.go("/search")
        if index == 5:
            page.go("/staff")
        if index == 6:
            page.go("/event")
            
    bar = ft.NavigationRail(
        selected_index=0,
        bgcolor="#000066",
        extended=True,
        indicator_color="white",
        indicator_shape=ft.RoundedRectangleBorder(radius=5),
        leading=ft.Text("School", size=25, weight="bold", color="WHITE38"),
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icon("HOME_ROUNDED", color="black", size=30), label_content=ft.Text("Home", color="WHITE38", weight="bold")), 
            ft.NavigationRailDestination(icon=ft.Icon("ANALYTICS", size=30), label_content=ft.Text("Analysis", color="WHITE38", weight="bold")),
            ft.NavigationRailDestination(icon=ft.Icon("SYSTEM_UPDATE_ROUNDED", size=30), label_content=ft.Text("Grade", color="WHITE38", weight="bold")),
            ft.NavigationRailDestination(icon=ft.Icon("payment", size=30), label_content=ft.Text("Payment", color="WHITE38", weight="bold")),
            ft.NavigationRailDestination(icon=ft.Icon("search", size=30), label_content=ft.Text("Search", color="WHITE38", weight="bold")),
            ft.NavigationRailDestination(icon=ft.Icon("CAST_FOR_EDUCATION", size=30), label_content=ft.Text("Staff", color="WHITE38", weight="bold")),
            ft.NavigationRailDestination(icon=ft.Icon("event", size=30), label_content=ft.Text("Event", color="WHITE38", weight="bold"))
        ],
        on_change=func_event
    )
     
    StudentNurseryNo: int = 240
    StudentPrimaryNo: int = 360
    StudentSecondaryNo: int = 540
    
    StudentNurseryLoan: float = 200.000
    StudentPrimaryLoan: float = 300.000
    StudentSecondaryLoan: float = 150.000
    
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
                first_date=datetime.datetime(year=2000, month=12, day=1),
                last_date=datetime.datetime(year=3000, month=12, day=1),
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
    
    if Class.value == "jss":
        print("jss num")
    
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
    
    ft.FilePicker()
    
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
    
    
    def login(e):
        if email.value == "admin" and password.value == "admin123":
            page.go("/home")
        else:
            page.open(
                ft.SnackBar(
                    content=ft.Text("wrong details"),
                    dismiss_direction=ft.DismissDirection.START_TO_END
                )
            )

    def login_hover(e: ft.HoverEvent): 
        e.control.scale = 1.2 if e.data == "true" else 1
        e.control.opacity = 0.8 if e.data == "true" else 1
        page.update()

        
    
    
    def change_route(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                horizontal_alignment="center",
                vertical_alignment="center",
                controls=[
                    ft.Image(
                        height=200,
                        width=200,
                        src="logo.png"
                    ),
                    ft.Text("login"),
                    email,
                    password,
                    ft.OutlinedButton(
                        "login",
                        width=200,
                        height=50,
                        scale=1,
                        opacity=1,
                        animate_opacity=ft.Animation(duration=300, curve=ft.AnimationCurve.EASE_IN),
                        animate_scale=ft.Animation(duration=300, curve=ft.AnimationCurve.BOUNCE_IN_OUT),
                        on_click=login,
                        on_hover=login_hover
                    ),
                    
                ]
            )
        )
        if page.route == "/home":
            page.views.append(
                ft.View(
                    "/home",
                    padding=0,
                    controls=[
                        #ft.Text("home"),
                        ft.Row(
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
                                    width=page.width,
                                    content=dbtable
                                )
                            ]
                        ),
                        ft.FloatingActionButton(
                            icon="add",
                            hover_elevation=32,
                            on_click=lambda e: page.open(alert)
                        )
                    ]
                )
            )
        if page.route == "/analysis":
            page.views.append(
                ft.View(
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
                                                    ft.Card(
                                                        surface_tint_color="green",
                                                        content=ft.Container(
                                                            width=300,
                                                            height=130,
                                                            border_radius=6,
                                                            padding=10,
                                                            content=ft.Column(
                                                                spacing=20,
                                                                controls=[
                                                                    ft.Container(content=ft.Text("NUSERY 1,2,3")),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon("person", size=50),
                                                                            ft.Column(
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Text("Nursey", size=20),
                                                                                    ft.Text(f"{StudentNurseryNo} pupils"),
                                                                                    #ft.Row(spacing=0,controls=[ft.Icon("person",size=20), ft.Text("pupils")])
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    ft.Card(
                                                        surface_tint_color="red",
                                                        content=ft.Container(
                                                            width=300,
                                                            height=130,
                                                            border_radius=6,
                                                            padding=10,
                                                            content=ft.Column(
                                                                spacing=20,
                                                                controls=[
                                                                    ft.Container(content=ft.Text("PRIMARY 1,2,3 4, 5,")),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon("Group", size=50),
                                                                            ft.Column(
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Text("Primary", size=20),
                                                                                    ft.Text(f"{StudentPrimaryNo} pupils"),
                                                                                    #ft.Row(spacing=0,controls=[ft.Icon("person",size=20), ft.Text("pupils")])
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        )
                                                    ),
                                                    ft.Card(
                                                        surface_tint_color="blue",
                                                        content=ft.Container(
                                                            width=300,
                                                            height=130,
                                                            border_radius=6,
                                                            padding=10,
                                                            content=ft.Column(
                                                                spacing=20,
                                                                controls=[
                                                                    ft.Container(content=ft.Text("JSS,SSS 1,2,3,1,2,3")),
                                                                    ft.Row(
                                                                        controls=[
                                                                            ft.Icon("Group", size=50),
                                                                            ft.Column(
                                                                                spacing=0,
                                                                                controls=[
                                                                                    ft.Text("Secondary", size=20),
                                                                                    ft.Text(f"{StudentSecondaryNo} pupils"),
                                                                                    #ft.Row(spacing=0,controls=[ft.Icon("person",size=20), ft.Text("pupils")])
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        )
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
            )
        if page.route == "/grade":
            page.views.append(
                ft.View(
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
            )
        if page.route == "/payment":
            page.views.append(
                ft.View(
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
                                                        ft.Card(
                                                            surface_tint_color="green",
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
                                                                                        ft.Text("Nusery", size=25),
                                                                                        ft.Text("30,000", weight="bold", color="BLUE_800", size=30)
                                                                                    ]
                                                                                ),
                                                                                ft.Row(
                                                                                    alignment="spacebetween",
                                                                                    controls=[
                                                                                        ft.Text(f"total student {StudentNurseryNo}", size=12),
                                                                                        ft.Text(f"total fee", size=11),
                                                                                        
                                                                                    ]
                                                                                ),
                                                                            ]
                                                                        ),
                                                                        ft.Row(
                                                                            alignment="spacebetween",
                                                                            controls=[
                                                                                ft.Text("Loan"),
                                                                                ft.Text(f"{StudentNurseryLoan}")
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ),
                                                        
                                                        ft.Card(
                                                            surface_tint_color="blue",
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
                                                                                        ft.Text("Primary", size=25),
                                                                                        ft.Text("45,000", weight="bold", color="BLUE_800", size=30)
                                                                                    ]
                                                                                ),
                                                                                ft.Row(
                                                                                    alignment="spacebetween",
                                                                                    controls=[
                                                                                        ft.Text(f"total student {StudentPrimaryNo}", size=12),
                                                                                        ft.Text("total fee", size=11),
                                                                                        
                                                                                    ]
                                                                                ),
                                                                            ]
                                                                        ),
                                                                        ft.Row(
                                                                            alignment="spacebetween",
                                                                            controls=[
                                                                                ft.Text("Loan"),
                                                                                ft.Text(f"{StudentPrimaryLoan}")
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        ),
                                                          
                                                        ft.Card(
                                                            surface_tint_color="red",
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
                                                                                        ft.Text("Secondary", size=25),
                                                                                        ft.Text("65,000", weight="bold", color="BLUE_800", size=30)
                                                                                    ]
                                                                                ),
                                                                                ft.Row(
                                                                                    alignment="spacebetween",
                                                                                    controls=[
                                                                                        ft.Text(f"total student {StudentSecondaryNo}", size=12),
                                                                                        ft.Text("total fee", size=11),
                                                                                        
                                                                                    ]  
                                                                                ),
                                                                            ]
                                                                        ),
                                                                        ft.Row(
                                                                            alignment="spacebetween",
                                                                            controls=[
                                                                                ft.Text("Loan"),
                                                                                ft.Text(f"{StudentSecondaryLoan}")
                                                                            ]
                                                                        )
                                                                    ]
                                                                )
                                                            )
                                                        )
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
            )
        if page.route == "/search":
            page.views.append(
                ft.View(
                    "/search",
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
            )
        if page.route == "/staff":
            page.views.append(
                ft.View(
                    "/",
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
                                                                        on_click=lambda e: file_picker.pick_files(),
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
            )
        if page.route == "/event":
            page.views.append(
                ft.View(
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
            )
            
        page.update()
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = change_route
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
    