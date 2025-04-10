import flet as ft 

bar = bar = ft.NavigationRail(
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
        ft.NavigationRailDestination(icon=ft.Icon("event", size=30), label_content=ft.Text("Event", color="WHITE38", weight="bold")),
        ft.NavigationRailDestination(icon=ft.Icon("book", size=30), label_content=ft.Text("Library", color="WHITE38", weight="bold")),
        ft.NavigationRailDestination(icon=ft.Icon("upload", size=30), label_content=ft.Text("Result", color="WHITE38", weight="bold"))
    ]
)