from images_processor import images as ima
from windows_processor import windows as win
from folder_processor import folder as fol




if __name__ == '__main__':
    listaMisiones = fol.listar_images('misiones')
    # section = detectar_ventanas('release')
    
    ima.procesar_imagenes(listaMisiones,'misiones')
    listaObjetos = fol.listar_images('objetos')
    ima.procesar_imagenes(listaObjetos, 'objetos')
