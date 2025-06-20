import flet as ft
from fletx import Xview

# Lista de itens do cardápio
itens = [
    # Hamburgueres
    {"categoria": "Hamburgueres", "imagem": "xegg.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"},
    *[{"categoria": "Hamburgueres", "imagem": "toplogo.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"} for _ in range(5)],

    # Trios
    {"categoria": "Trios", "imagem": "trio.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"},
    *[{"categoria": "Trios", "imagem": "toplogo.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"} for _ in range(5)],

    # Combos
    {"categoria": "Combos", "imagem": "combo.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"},
    *[{"categoria": "Combos", "imagem": "toplogo.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"} for _ in range(5)],

    # Bebidas
    {"categoria": "Bebidas", "imagem": "coca600.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"},
    *[{"categoria": "Bebidas", "imagem": "toplogo.png", "nome": "X-EGG-BACON", "descricao": "Pão, Carne, Queijo, Presunto e Ovos", "preço": "R$:25,80"} for _ in range(5)],
]

# ListView que mostrará os cards
lista = ft.ListView(
    expand=True,
    spacing=10,
    padding=10
)

# Função para criar cada card de item
def criar_card(item):
    return ft.Container(
        bgcolor="#0dff00",
        border_radius=10,
        padding=10,
        content=ft.Row(
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Image(item["imagem"], height=100, width=100, border_radius=10),
                ft.Column(
                    spacing=5,
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.Text(item["nome"], size=20, weight="bold", color="white"),
                        ft.Text(item["descricao"], size=14, color="white"),
                        ft.Text(item["preço"], size=18, weight="bold", color="white"),
                    ]
                )
            ]
        )
    )

# Função para filtrar e mostrar uma categoria
def mostrar_categoria(categoria):
    lista.controls.clear()
    for item in itens:
        if item["categoria"] == categoria:
            lista.controls.append(criar_card(item))
    lista.update()

# Lista de categorias
categorias = ["Hamburgueres", "Trios", "Combos", "Bebidas"]

# Barra de botões de categorias
def criar_botao_categoria(cat):
    return ft.ElevatedButton(
        content=ft.Text(value=cat, size=16, weight="bold", color="green"),
        on_click=lambda e: mostrar_categoria(cat)
    )

botoes_categorias = ft.Row(
    spacing=10,
    scroll=ft.ScrollMode.AUTO,
    controls=[criar_botao_categoria(c) for c in categorias]
)


# View principal
class NewView(Xview):
    def build(self):
        return ft.View(
            vertical_alignment='top',
            horizontal_alignment='center',
            controls=[
                # Top Bar
                ft.Row(
                    width='100%',
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            spacing=10,
                            controls=[
                                ft.Image('toplogo.png', width=50, height=50),
                                ft.Text('Top Lanche', size=25, weight='bold', color='white'),
                            ]
                        ),
                        ft.IconButton(
                            ft.Icons.SHOPPING_CART_CHECKOUT_OUTLINED,
                            icon_color='#0dff00',
                            icon_size=35,
                            on_click=lambda e: self.go("/cart")
                        ),
                    ]
                ),
                # Botões de Categoria
                botoes_categorias,
                # Lista de Itens
                lista
            ]
        )

    def did_mount(self):
    # Agora a lista já está na página, então podemos atualizar sem erro
        mostrar_categoria("Hamburgueres")
