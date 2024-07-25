from cx_Freeze import setup, Executable
import os

include_files = [('Fotos', 'Fotos')]


executables = [
    Executable('face_detection.py', base=None),  
    Executable('server.py', base=None)           
]

setup(
    name='FaceDetectionApp',
    version='1.0',
    description='Aplicación de detección de rostros',
    options={'build_exe': {'include_files': include_files}},
    executables=executables
)
