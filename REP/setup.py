#!/usr/bin/env python3.4

from distutils.core import setup

setup(name='ejemplo_solid',
      version=1.0,
      description='Paquete de definición de Entidades',
      author='VV',
      packages=['modelo','acceso_datos', 'adquisidor',
                'identificador', 'procesador', 'tratamiento', 'utiles',
                'visualizador'],
      scripts=['runner','lanzador.py']
      )