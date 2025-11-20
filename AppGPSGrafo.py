import grafoListas
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

    def volver(e):
        page.clean()
        page.add(contenidoPrincipal)
        page.update()

    def nombresImagenes(carpeta):
        grafo = grafoListas.Grafo()
        for i in os.listdir(carpeta):
            ruta = os.path.join(carpeta,i)
            if os.path.isfile(ruta):
                grafo.insertar(i)
        return grafo



    def crearEntrada(nombre,color):
        carpeta = nombre
        contenido = crearContenido(carpeta,nombre) 
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

    def grafoEntradas(carpeta):
        
        grafo = grafoListas.Grafo()
   
        for i in os.listdir(carpeta):
            nombre = os.path.splitext(i)[0]
            color = ft.Colors.random()
            contenedor = crearEntrada(nombre, color)
            grafo.insertar(nombre, contenedor)
        return grafo


    def crearUbicacion(nombre,color,nombreimagen,carpeta):
        def mapa(e):
            page.clean()
            page.add(ft.Column([
                    ft.ElevatedButton(text="Volver al inicio",color=ft.Colors.WHITE60,on_click=volver),
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

    def grafoUbicaciones(carpeta, nombresArbol, carpetaImg):
        ubicaciones = grafoListas.Grafo()
        nombresLista = nombresArbol.nombres()

        archivos = os.listdir(carpeta)
        for i, archivo in enumerate(archivos):
            nombre = os.path.splitext(archivo)[0]
            nombreimagen = nombresLista[i % len(nombresLista)] if nombresLista else archivo
            color = ft.Colors.random()
            contenedor = crearUbicacion(nombre, color, nombreimagen, carpetaImg)
            ubicaciones.insertar(nombre, contenedor)

        return ubicaciones


    def crearContenido(carpeta,carpetaImg):
        entrada = nombresImagenes(carpeta)
        ubicaciones = grafoUbicaciones(carpeta,entrada,carpetaImg)
        galeria = ft.ResponsiveRow(
        [ft.Container(ubicacion.data, col={"sm":12,"md":6,"lg":3}) for ubicacion in ubicaciones],
            )
        return ft.Column([
            ft.Text("Escoje una ubicacion", size= 32,weight=ft.FontWeight.BOLD),
            ft.Divider(height=10,color=ft.Colors.WHITE12),
            galeria
            ],scroll=ft.ScrollMode.AUTO, expand=True)

    

    entradas = grafoEntradas("Entradas")
    
    galeriaprincipal = ft.ResponsiveRow(
        [ft.Container(entrada.data, col={"sm":10,"md":5,"lg":2}) for entrada in entradas],
    )

    contenidoPrincipal = ft.Column([
        ft.Text("Escoje tu ubicacion actual",size=32,weight=ft.FontWeight.BOLD),
        galeriaprincipal
    ],scroll=ft.ScrollMode.AUTO,expand=True)
    page.add(contenidoPrincipal)

ft.app(main)
