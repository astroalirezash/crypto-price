import flet as ft
from api_exercise import res1
from time import sleep


def main(page: ft.Page):
    page.title = 'Crypto price App'

    def btn_click(e):
        if not coin_name.value:
            coin_name.error_text = "Please enter coin name or symbol"
            page.update()
        else:
            page.clean()
            while True:
                price = res1(coin_name.value)
                showprice = ft.Text(value=price, color='white')
                page.controls.append(showprice)
                page.update()
                page.controls.remove(showprice)
                sleep(3)

    coin_name = ft.TextField(label="Coin name or symbol", text_align=ft.TextAlign.CENTER)

    page.add(coin_name, ft.ElevatedButton("search", on_click=btn_click))


ft.app(target=main)
