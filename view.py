import flet as ft


def main(page: ft.Page):
    page.title="Аналитический комплекс для АЭС"
    page.theme="dark" #"light"
    page.bgcolor="BLACK900"
    page.scroll=True
    page.auto_scroll=True
    page.padding=ft.Padding(left=0,bottom=0,right=0,top=0)






    all_page_cont=ft.Container(content=None,padding=ft.Padding(left=20,right=20,top=30,bottom=20))
    page_bg_img=ft.Image(src="")
    all_page_stack=ft.Stack(controls=[page_bg_img,all_page_cont])
    page.add(all_page_stack)
    page.update()


ft.app(target=main)

#flet run view.py --web
