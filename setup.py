
import os
from setuptools import setup

def get_resource_files(directory):
    resource_files = []
    for files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            destination_dir = os.path.relpath(file_path, directory)
            resource_files.append((destination_dir, [file_path]))
    return resource_files

resource_files = get_resource_files('resources')

APP = ['main.py']
DATA_FILES = resource_files
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'],
    'plist': {
        'CFBundleName': 'main',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleGetInfoString': 'Mrs. Barry Game',
        'CFBundleExecutable': 'MrsBarry',
        'CFBundleIdentifier': 'com.yourcompany.mrsbarry',
    },
    'resources': DATA_FILES,
}


setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app', 'pyinstaller'],
)
