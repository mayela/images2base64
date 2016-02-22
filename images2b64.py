#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Script para codificar todas las imagenes de un directorio a base64
1. Obtener un list de toas las imagenes
2. comprobar que sean archivos y no directorios
3. Codificar a base64
4. Guardar en un csv nombre de la imagen y su string en base64
"""

import os
import base64

files = os.listdir(".")
for item in files:
    if os.path.isfile(item):
        with open(item, "rb") as image:
            encode_image = base64.b64encode(image.read())
            encode_image = encode_image.decode("ascii")
            print("%s, %s"%(item, encode_image))
            #escribir en un csv
    else:
        pass


