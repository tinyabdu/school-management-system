import flet as ft 


def login(page: ft.Page):
    
 
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
    

    def login_hover(e: ft.HoverEvent): 
        e.control.scale = 1.2 if e.data == "true" else 1
        e.control.opacity = 0.8 if e.data == "true" else 1
        page.update()

        
    return ft.View(
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
     