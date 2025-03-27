import flet as ft
import time
from flet_assets import AssetsServer

server = AssetsServer(directory="assets")

def main(page:ft.Page):
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary="black"),
        color_scheme_seed="#FF724C",
        icon_button_theme=ft.IconTheme(color="#2A2C41"),
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(primary="white"),
        color_scheme_seed="#FF724C",
        icon_button_theme=ft.IconTheme(color="#2A2C41"),
        page_transitions=ft.PageTransitionsTheme(windows=ft.PageTransitionTheme.NONE)
    )
    page.theme_mode="dark"
    page.theme = theme
    page.update()
    
    bottom_bar = ft.BottomAppBar(
        surface_tint_color="red",
        shape=ft.NotchShape.CIRCULAR,
        content=ft.Row(
            alignment="center",
            spacing=30,
            controls=[
                ft.IconButton(icon="home", on_click=lambda e: page.go("/main"), icon_size=35),
                ft.IconButton(icon="chat",  on_click=lambda e: page.go("/bot-chat"), icon_size=35),
                ft.IconButton(icon="newspaper", on_click=lambda e: page.go("/news"), icon_size=35),
                ft.IconButton(icon="library_books", on_click=lambda e: page.go("/library"), icon_size=35),
            ]
        )
    )
    
    img_theme = ft.colors
    if page.theme_mode == "dark":
        img_theme = ft.colors("white")
        
    profile_alert = ft.AlertDialog(
        content=ft.Container(
            width=150,
            height=150,
            content=ft.Column(
                alignment="center",
                spacing=5,
                horizontal_alignment="Center",
                controls=[
                    ft.Image(f"doctor.svg"),
                    ft.Text("Abdullahi haruna"),
                    ft.Text("JSS 3"),
                    ft.Container(
                        on_click=lambda e: page.go("/"),
                        content=ft.Icon("logout")
                    ),
                ]
            )
        )
    )

    email = ft.TextField(
        hint_text="email or regno",
        label="Email/Regno",
        width=page.width - 50,
        keyboard_type=ft.KeyboardType.EMAIL,
        border_radius=17,
        icon="login"
    )
    
    password = ft.TextField(
        hint_text="*******",
        label="password",
        width=page.width - 50,
        password=True,
        can_reveal_password=True,
        border_radius=17,
        icon="password"
    )
    
    chat_response = ft.Column(expand=True)
    
    def chat_func(e):
        text_send = ft.Text(f"{chat.value}")
        chat_response.controls.append(text_send)
        if chat.value.lower() == "what is your name":
            chat_response.controls.append(
                ft.Container(
                    padding= 10,
                    expand=True,
                    alignment=ft.alignment.top_right,
                    content=ft.Text("tiny")
                )
            )
        chat.value = ""
        page.update()
    
    
   
    
    
    
    
    chat = ft.TextField(
        hint_text="message",
        border_radius=18,
        width=page.width,
        suffix_icon=ft.IconButton("send", on_click=chat_func)
    )
    
    
    
    def login(e):
        if email.value == "" or password.value == "":
            page.open(
                ft.SnackBar(
                    content=ft.Column(
                        controls=[
                            ft.ProgressBar(),
                            ft.Text("type your details")
                        ]
                    )
                )
            )
        if email.value == "student/2025" and password.value == "student":
            page.open(
                ft.AlertDialog(
                    content=ft.Container(
                        width=200,
                        height=150,
                        content=ft.Column(
                            horizontal_alignment="center",
                            alignment="center",
                            controls=[
                                ft.Icon("done", size=65),
                                ft.Text("Succefull", size=25)
                            ]
                        )
                    )
                )
            )
            time.sleep(0.7)
            page.go("/main")
            
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                horizontal_alignment="center",
                vertical_alignment="center",
                controls=[
                    ft.Text("login"),
                    email,
                    password,
                    ft.ElevatedButton(
                        text="next", 
                        width=350, 
                        height=55, 
                        bgcolor="#FDBF50",
                        color="#2A2C41", 
                        style=ft.ButtonStyle(text_style=ft.TextStyle(size=25)),
                        on_click=login,
                        on_long_press=lambda _: page.go("/main")
                    )
                ]
            )
        )
        if page.route == "/main":
            page.views.append(
                ft.View(
                    "/main",
                    appbar=ft.AppBar(
                        leading=ft.Container(
                            padding=5,
                            border_radius=30,
                            on_click=lambda e: page.open(profile_alert),
                            content=ft.Image(src=f"{server.assets}/doctor.svg", width=30, height=30)
                        ),
                        center_title=True,
                        title=ft.Text("Abullahi harun"),
                        actions=[
                            ft.Icon("notifications")
                        ]
                    ),
                    bottom_appbar=bottom_bar,
                    spacing=30,
                    horizontal_alignment="center",
                    controls=[
                        ft.Text("Academics"),
                        ft.Container(
                            width=page.width,
                            alignment=ft.alignment.center,
                            content=ft.GridView(
                                width=page.width,
                                expand=1,
                                runs_count=5,
                                max_extent=150,
                                child_aspect_ratio=1.0,
                                spacing=5,
                                run_spacing=5,
                                controls=[
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            on_click=lambda _: page.go("/student"),
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Image(src=f"{server.assets}/user-check.png", width=50, height=50, color=img_theme),
                                                    ft.Text("Student")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("my_library_books_sharp", size=50),
                                                    ft.Text("Studies")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Image(src=f"{server.assets}/calendar.png", width=50, height=50, color=img_theme),
                                                    ft.Text("Time table")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("sticky_note_2", size=50),
                                                    ft.Text("Results")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("menu_book", size=50),
                                                    ft.Text("Syllabus")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("school", size=50),
                                                    ft.Text("Fees")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("assignment", size=50),
                                                    ft.Text("Assignment")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("event", size=50),
                                                    ft.Text("Event")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("info", size=50),
                                                    ft.Text("information")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("document_scanner", size=50),
                                                    ft.Text("document")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon("biotech", size=50),
                                                    ft.Text("health")
                                                ]
                                            )
                                        ),
                                    ),
                                    ft.Card(
                                        height=100,
                                        width=100,
                                        content=ft.Container(
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                alignment="center",
                                                controls=[
                                                    ft.Icon(ft.icons.ONLINE_PREDICTION, size=50),
                                                    ft.Text("courses")
                                                ]
                                            )
                                        ),
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )
        if page.route == "/bot-chat":
            page.views.append(
                ft.View(
                    "/bot-chat",
                    bottom_appbar=bottom_bar,
                    appbar=ft.AppBar(
                        title=ft.Text("chat"),
                        automatically_imply_leading=False,
                        center_title=True
                    ),
                    padding=0,
                    controls=[
                        chat_response,
                        ft.Container(
                            expand=True,
                            padding=10,
                            alignment=ft.alignment.bottom_center,
                            content=chat,
                        )
                    ]
                )
            )
        if page.route == "/news":
            page.views.append(
                ft.View(
                    "/news",
                    bottom_appbar=bottom_bar,
                    appbar=ft.AppBar(
                        title=ft.Text("News"),
                        center_title=True,
                        automatically_imply_leading=False,
                    ),
                    controls=[
                        
                    ]
                )
            )
        if page.route == "/library":
            page.views.append(
                ft.View(
                    "/library",
                    bottom_appbar=bottom_bar,
                    controls=[
                        
                    ]
                )
            )
        if page.route == "/student":
            page.views.append(
                ft.View(
                    "/student",
                    appbar=ft.AppBar(
                        title=ft.Text("Student Details"),
                        center_title=True,
                        leading=ft.IconButton("arrow_back_ios_new", on_click=lambda _: page.go("/main"))
                    ),
                    padding=0,
                    controls=[
                        ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src=f"{server.assets}/doctor.svg",
                                        width=200,
                                        height=200
                                    ),
                                    ft.Text("Name: Abdullahi Haruna"),
                                    ft.Text("Reg no: sec/sss/2"),
                                    ft.Text("Section: Secondary"),
                                    ft.Text("Class: SS2"),
                                    ft.Text("Age: 19"),
                                    ft.Text("Admited: 2014"),
                                    ft.Text("Type: Art student"),
                                    ft.Text("Training: Bussiness Adminintration"),
                                    
                                    ft.Container(
                                        content=ft.Column(
                                            controls=[
                                                ft.Container(
                                                    width=200,
                                                    height=45,
                                                    padding=10,
                                                    bgcolor="#FDBF50",
                                                    border_radius=8,
                                                    alignment=ft.alignment.center,
                                                    content=ft.Text("Other Details", color="#2A2C41", size=25, weight="bold"),
                                                ),
                                                ft.Text("Parent Name: Haruna Ibrahim"),
                                                ft.Text("Parent Occupation: Journalist"),
                                                ft.Text("State of Origin: Kaduna"),
                                                ft.Text("Address: Inuwa Road Nassarawa Kaduna"),
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
        page.update()
    page.on_route_change=route_change
    page.go(page.route)#
    
if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
    
    