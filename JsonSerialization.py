import os
import subprocess
import json
from tkinter import messagebox


class JsonSerialization:

    @staticmethod
    def serialize(values):
        data = json.dumps(values)

        with open('temp/jsonData.json', 'w') as outfile:
            json.dump(data, outfile)

        currentDir = os.path.realpath(os.curdir) + '\\temp\\jsonData.json'
        subprocess.Popen(r'explorer /open, ' + currentDir)

    @staticmethod
    def deserialize():
        try:
            with open('temp/jsonData.json') as f:
                data = json.loads(json.load(f))

            with open('temp/parsedJsonData.txt', 'w') as outfile:
                json.dump(data, outfile)

            currentDir = os.path.realpath(os.curdir) + '\\temp\\parsedJsonData.txt'
            subprocess.Popen(r'explorer /open, ' + currentDir)

        except:
            print('File not found')
            messagebox.showerror(
                "Файл не найден",
                "Сначала сделайте серилизацию")
