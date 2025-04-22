import os

def listar_images (path):
    pathCompleto = f'../data/{path}'
    images = os.listdir(pathCompleto)
    # print("lista de imagenes", images)
    return images