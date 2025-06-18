import flet as ft
from fletx import Xview

class HomeView(Xview):
    def build(self):
        return ft.View(
            vertical_alignment='center',
            horizontal_alignment='center',
            bgcolor='black',
            controls=[
                ft.Image(src='toplogo.png',width=150, height=150),
                ft.Text("Home Page On", size=20, weight='bold', color='white'),
                ft.ElevatedButton(bgcolor='#0dff00',
                                  content= ft.Text('Cardápio', color='white', weight='bold', size=15),
                                  on_click= lambda e:self.go("/new") ),
            ]
        )