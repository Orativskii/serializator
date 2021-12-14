import os
import subprocess
import json
from tkinter import messagebox


class CsvSerialization:

    @staticmethod
    def serialize(data):
        csvData = ",".join(list(data.keys())) + '\n' + ",".join(list(data.values()))
        print(csvData)
        with open('temp\\csvData.csv', 'w') as f:
            f.write(str(csvData))

        currentDir = os.path.realpath(os.curdir) + '\\temp\\csvData.csv'
        subprocess.Popen(r'explorer /open, ' + currentDir)

    @staticmethod
    def deserialize():
        try:
            with open('temp\\csvData.csv') as f:
                fileData = f.read()
            fileData = fileData.split("\n")
            keys = fileData[0].split(",")
            values = fileData[1].split(",")

            parsedCsv = {keys[0]: values[0],
                         keys[1]: values[1],
                         keys[2]: values[2], }

            with open('temp/parsedCsvData.txt', 'w') as outfile:
                json.dump(parsedCsv, outfile)

            currentDir = os.path.realpath(os.curdir) + '\\temp\\parsedCsvData.txt'
            subprocess.Popen(r'explorer /open, ' + currentDir)

        except:
            print('File not found')
            messagebox.showerror(
                "Файл не найден",
                "Сначала сделайте серилизацию")
