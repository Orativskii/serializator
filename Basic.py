from tkinter import *
from tkinter.ttk import *

from CsvSerialization import CsvSerialization
from JsonSerialization import JsonSerialization
from XmlSerialization import XmlSerialization


class Basic:
    def __init__(self):
        window = Tk()
        window.title("Serialization")
        x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
        y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
        window.wm_geometry("+%d+%d" % (x, y))
        window.geometry('270x115')
        window.minsize(270, 115)
        window.maxsize(270, 115)
        firstFieldLabel = Label(window, text="Field 1")
        firstFieldLabel.grid(column=0, row=0)
        self.firstFieldKey = Entry(window, width=10)
        self.firstFieldKey.grid(column=1, row=0)
        self.firstFieldValue = Entry(window, width=10)
        self.firstFieldValue.grid(column=2, row=0)

        self.secondFieldLabel = Label(window, text="Field 2")
        self.secondFieldLabel.grid(column=0, row=1)
        self.secondFieldKey = Entry(window, width=10)
        self.secondFieldKey.grid(column=1, row=1)
        self.secondFieldValue = Entry(window, width=10)
        self.secondFieldValue.grid(column=2, row=1)

        self.thirdFieldLabel = Label(window, text="Field 3")
        self.thirdFieldLabel.grid(column=0, row=2)
        self.thirdFieldKey = Entry(window, width=10)
        self.thirdFieldKey.grid(column=1, row=2)
        self.thirdFieldValue = Entry(window, width=10)
        self.thirdFieldValue.grid(column=2, row=2)

        self.csv = Button(window, text='Serialize to scv', command=self.serializateToCsv)
        self.json = Button(window, text='Serialize to  json', command=self.serializateToJson)
        self.xml = Button(window, text='Serialize to xml', command=self.serializateToXml)
        self.csv.grid(column=0, row=5)
        self.json.grid(column=1, row=5)
        self.xml.grid(column=2, row=5)

        self.csvd = Button(window, text='Deserialize scv', command=self.deserializateCsv)
        self.jsond = Button(window, text='Deserialize json', command=self.deserializateJson)
        self.xmld = Button(window, text='Deserialize xml', command=self.deserializateXml)
        self.csvd.grid(column=0, row=7)
        self.jsond.grid(column=1, row=7)
        self.xmld.grid(column=2, row=7)

        window.mainloop()

    def getValues(self):
        return {self.firstFieldKey.get(): self.firstFieldValue.get(),
                self.secondFieldKey.get(): self.secondFieldValue.get(),
                self.thirdFieldKey.get(): self.thirdFieldValue.get(), }

    def isNotEmpty(self):
        return all([self.firstFieldKey.get(), self.firstFieldValue.get(), self.secondFieldKey.get(),
                    self.secondFieldValue.get(), self.thirdFieldKey.get(), self.thirdFieldValue.get()])

    def serializateToCsv(self):
        if self.isNotEmpty():
            CsvSerialization().serialize(self.getValues())

    def deserializateCsv(self):
        CsvSerialization().deserialize()

    def serializateToJson(self):
        if self.isNotEmpty():
            JsonSerialization().serialize(self.getValues())

    def deserializateJson(self):
        JsonSerialization().deserialize()

    def serializateToXml(self):
        if self.isNotEmpty():
            XmlSerialization().serialize(self.getValues())

    def deserializateXml(self):
        XmlSerialization().deserialize()
