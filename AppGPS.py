import listasEnlazadas as listas
import flet as ft
import os
import base64


def imagen(nombre,carpeta):
    dirrecionImagen = os.path.join(os.path.dirname(__file__), carpeta,nombre)
    with open(dirrecionImagen,"rb") as img:
        bytesImagen = base64.b64encode(img.read()).decode()
    return ft.Column([
        ft.Image(
            src_base64=bytesImagen,
            width=1000,
            height=1200,
            fit=ft.ImageFit.CONTAIN,),
            ])


def main(page: ft.Page):
    page.title = "GPS"
    page.theme_mode = ft.ThemeMode.DARK

    def nombresImagenes(carpeta):
        lista = listas.ListaEnlazadas()
        for i in os.listdir(carpeta):
            ruta = os.path.join(carpeta,i)
            if os.path.isfile(ruta):
                lista.agregarInicio(i)
        return lista



    def crearEntrada(nombre,color):
        #carpeta = "app/" + nombre #Si se selecciona proyecto Gps
        carpeta = nombre
        contenido = crearContenido(carpeta,nombre) #Si se selecciona directo app
        def entrar(e):
            page.clean()
            page.add(contenido)
            page.update()
        boton = ft.ElevatedButton(text="Escojer ubicacion",color=ft.Colors.WHITE60,on_click=entrar)
        return ft.Container(
            content=ft.Column([
                    ft.Text(nombre,size=16),
                    boton
                ]),
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
    )

    def listaEntradas(carpeta):
        
        lista = listas.ListaEnlazadas()
   
        for i in os.listdir(carpeta):

            nombre = os.path.splitext(i)[0]
            lista.agregarInicio(crearEntrada(nombre, ft.Colors.random()))
        return lista


    def crearUbicacion(nombre,color,nombreimagen,carpeta):
        def mapa(e):
            page.clean()
            page.add(ft.Column([
                    imagen(nombreimagen,carpeta),],
                    scroll=ft.ScrollMode.AUTO, expand=True))
            page.update()

        boton = ft.ElevatedButton(text="Escojer ubicacion",color=ft.Colors.WHITE60,on_click=mapa)
        return ft.Container(
            content=ft.Column([
                    ft.Text(nombre,size=16),
                    boton
                ]),
            bgcolor=color,
            border_radius=10,
            padding=20,
            alignment=ft.alignment.center,
    )

    def listaUbicaciones(carpeta,nombresImagenes,carpetaImg):
        listaNombres = nombresImagenes
        contador = 1
        lista = listas.ListaEnlazadas()
        for i in os.listdir(carpeta):
            contador+=1
        
        for i in os.listdir(carpeta):
            contador-=1
            os.path.splitext(i)[0]
            lista.agregarInicio(crearUbicacion(i,ft.Colors.random(),listaNombres.buscarPos(contador),carpetaImg))
        return lista



    def crearContenido(carpeta,carpetaImg):
        entrada = nombresImagenes(carpeta)
        ubicaciones = listaUbicaciones(carpeta,entrada,carpetaImg)
        galeria = ft.ResponsiveRow(
        [ft.Container(ubicacion, col={"sm":12,"md":6,"lg":3}) for ubicacion in ubicaciones],
            )
        return ft.Column([
            ft.Text("Escoje una ubicacion", size= 32,weight=ft.FontWeight.BOLD),
            ft.Divider(height=10,color=ft.Colors.WHITE12),
            galeria
            ],scroll=ft.ScrollMode.AUTO, expand=True)

    

    #entradas = listaEntradas("app/Entradas")
    entradas = listaEntradas("Entradas")
    galeriaprincipal = ft.ResponsiveRow(
        [ft.Container(entrada, col={"sm":10,"md":5,"lg":2}) for entrada in entradas],
    )
    contenidoPrincipal = ft.Column([
        ft.Text("Escoje tu ubicacion actual",size=32,weight=ft.FontWeight.BOLD),
        galeriaprincipal
    ],scroll=ft.ScrollMode.AUTO,expand=True)
    page.add(contenidoPrincipal)

ft.app(main)
