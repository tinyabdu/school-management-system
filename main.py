import flet as ft
from pages.login import login
from pages.home import home
from pages.analysis import analysis
from pages.grade import grade
from pages.payment import payment
from pages.search import search
from pages.staff import staff
from pages.event import event
from pages.books import book
from pages.result import result
import time
from utilities.bar import bar


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
        if index == 7:
            page.go("/book")
        if index == 8:
            page.go("/result")
            
    bar.on_change=func_event
     

    
   
    
  
    
   
    
    
    def change_route(route):
        page.views.clear()
        page.views.append(login(page))
        if page.route == "/home":
            page.views.append(home(page))
        if page.route == "/analysis":
            page.views.append(analysis(page))
        if page.route == "/grade":
            page.views.append(grade(page))
        if page.route == "/payment":
            page.views.append(payment(page))
        if page.route == "/search":
            page.views.append(search(page))
        if page.route == "/staff":
            page.views.append(staff(page))
        if page.route == "/event":
            page.views.append(event(page)) 
        if page.route == "/book":
            page.views.append(book(page))
        if page.route == "/result":
            page.views.append(result(page))
            
        page.update()
    page.on_route_change = change_route
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main, assets_dir="assets")
    