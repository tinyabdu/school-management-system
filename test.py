import flet as ft  
from typing import Union, Optional
from enum import Enum

# from fletmint import UserProfile


class Status(Enum):
    ACTIVE: str = "blue",
    OFFLINE: str = "black"
    NONE = None
    

    
class Profile(ft.Container):
    def __init__(
        self, 
        name: Optional[str] = None, 
        control: Union[ft.Icon, ft.Image] = None, 
        status = Status.ACTIVE
    ):
        super().__init__()
        self.status = status
        if self.status == Status.ACTIVE:
            return 
        thicker = ft.Container(
            height=5,
            width=8,
        )
        self.content = ft.Row(
            controls=[
                control,
                ft.Text(f"{name}"),
                ft.Container(content=self.status)
                
            ]
        )
        if self.status == Status.ACTIVE:
            thicker.bgcolor = "blue"
        elif self.status == Status.OFFLINE:
            thicker.bgcolor = "black"
            
        

def main(page:ft.Page):
    
    # def pick_files_result(e: ft.FilePickerResultEvent):
    #     selected_files.value = (
    #         ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
    #     )
    #     selected_files.update()

    # pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    # selected_files = ft.Text("image name")

    # page.overlay.append(pick_files_dialog)

    # page.add(
    #     ft.Row(
    #         [
    #             ft.ElevatedButton(
    #                 "Pick files",
    #                 icon=ft.icons.UPLOAD_FILE,
    #                 on_click=lambda _: pick_files_dialog.pick_files(
    #                     allow_multiple=True
    #                 ),
    #             ),
    #             selected_files,
    #         ]
    #     )
    # )
    
    # button = [
    #     {"id":1, "name":"login", "status":"active100"},
    #     {"id":2, "name":"logout", "status":"active200"},
    #     {"id":3, "name":"signin", "status":"active300"}
    # ]

    # col = ft.Column()
    
    # def print_something(e):
    #     id = e.control.data
    #     data = next((item for item in button if item["id"] == id), None)
    #     print(data)
    #     page.open(
    #         ft.AlertDialog(
    #             content=ft.Container(
    #                 content=ft.Column(
    #                     controls=[
    #                         ft.Text(data["name"]),
    #                         ft.Text(data["status"]),
    #                         ft.Text("good"),
    #                     ]
    #                 )
    #             )
    #         )
    #     )
    #     print(e.control.data)
    
    # for btn in button:
    #     col.controls.append(
    #         ft.Button(f"{btn["name"]}", data=btn["id"], on_click=print_something)
    #     )
    # page.add(
    #     col
    # )
    page.add(
        Profile(
            name="abdul",
            control=ft.Icon(name="home"),
            status=Status.ACTIVE
        ),
    #    UserProfile()
    )


ft.app(target=main)