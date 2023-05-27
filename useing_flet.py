import flet as ft
from api_exercise import res1
from time import sleep


def main(page: ft.Page):
    page.title = 'Crypto price App'
    page.window_width = 500
    page.window_height = 500
    page.window_center()
    page.theme = ft.Theme(color_scheme_seed="#184C46")

    page.bgcolor = '#145252'

    def btn_click(e):
        if not coin_name.value:
            coin_name.error_text = "Please enter coin name or symbol"
            page.update()
        else:
            page.clean()
            progressbar = ft.ProgressBar(width=page.width, color='#C960E1')
            page.add(progressbar)

            while True:
                price = res1(coin_name.value)
                showprice = ft.Text(value=price)
                page.controls.append(showprice)
                page.update()
                page.controls.remove(showprice)
                sleep(3)

    coin_name = ft.TextField(label="Coin name or symbol", border_color='#C960E1')
    btn = ft.ElevatedButton("search", on_click=btn_click, width=page.width, color='#C960E1')

    page.add(coin_name, btn)


ft.app(target=main)
