import os
import subprocess
import json
from tkinter import messagebox

from dicttoxml import dicttoxml
import xmltodict


class XmlSerialization:

    @staticmethod
    def serialize(data):
        xml = dicttoxml(data)
        xml_decode = xml.decode()
        xmlfile = open("temp\\xmlData.xml", "w")
        xmlfile.write(xml_decode)
        xmlfile.close()

        currentDir = os.path.realpath(os.curdir) + '\\temp\\xmlData.xml'
        subprocess.Popen(r'explorer /open, ' + currentDir)

    @staticmethod
    def deserialize():
        try:
            with open('temp/xmlData.xml') as f:
                data = xmltodict.parse(f.read())

            with open('temp/parsedXmlData.txt', 'w') as outputFile:
                json.dump(data, outputFile)

            currentDir = os.path.realpath(os.curdir) + '\\temp\\parsedXmlData.txt'
            subprocess.Popen(r'explorer /open, ' + currentDir)

        except:
            print('File not found')
            messagebox.showerror(
                "Файл не найден",
                "Сначала сделайте серилизацию")
