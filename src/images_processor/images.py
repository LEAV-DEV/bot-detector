import pyautogui ,sys, cv2, os
import time

pyautogui.FAILSAFE = True


def procesar_imagenes(images, path):

    for image in images:
        pathImage = f"../data/{path}/{image}"
        if not os.path.exists(pathImage):
            print(f"❌ Imagen no encontrada en la ruta: {pathImage}")
        else:
            # print(f"🆗 Imagen encontrada en la ruta: {pathImage}")
            try:
                locate = (pyautogui.locateOnScreen(pathImage, confidence = 0.8))
                if locate is not None:
                    ejecutar_clicks(locate)

            except pyautogui.ImageNotFoundException:
                print(f"❌ No se pudo localizar la imagen con al ruta '{pathImage}' en la pantalla.")
        # if locate is not None:
        #     ejecutar_clicks(locate, section)

def ejecutar_clicks(locate):
    if locate is not None:
        center = pyautogui.center(locate)
        pyautogui.moveTo(center[0],center[1],duration=0.1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(2)