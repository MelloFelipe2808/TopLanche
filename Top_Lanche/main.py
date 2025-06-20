import flet as ft
from fletx import Xapp, route
from views.home import HomeView
from views.newpage import NewView
from views.carrinho import CartView

def main(page:ft.Page):
    page.title = 'Top Lanche Delivery'
    page.theme_mode = ft.ThemeMode.DARK
    page.on_resized=True
    page.add(
        ft.Text('teste page',size=20,weight='bold', color='white'),
    )

    Xapp(page=page,
         routes=[
             route(route="/", view=HomeView),
             route(route="/new", view=NewView),
             route(route="/cart", view=CartView),
         ]
         )





ft.app(target=main,
       view=ft.WEB_BROWSER,
       assets_dir='assets',)