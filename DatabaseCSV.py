#!/usr/bin/env python3
import csv

class CSVHandler:
    def __init__(self, obiekt):
        self.obiekt = obiekt

    def initialCsvFactory(self):
        header = ['id', 'imie', 'nazwisko', 'klasa', 'profil']
        data = ['1', 'Adrian', "Kortyla", 3, 'A']
        with open(self.obiekt, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)

    def userReadCSV(self):
        print("Dane wewnatrz bazy danych: ")
        rows = []
        with open(self.obiekt, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        print("Kolumny jakie zawiera nasza baza danych: ")
        print(header)
        for i in rows:
            print(i)


    def writePreviousData(self):
        rows = []
        with open(self.obiekt, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)

        return header, rows

    def deleteSingleRecord(self):
        self.userReadCSV()
        recordToBeDeleted = int(input("Ktory rekord chcesz usunac ? "))
        header, data = self.writePreviousData()
        print(data)
        indexOfrecordToBeDeleted = None

        for i in range(len(data)):
            if(int(data[i][0]) == recordToBeDeleted):
                indexOfrecordToBeDeleted = i
                break
        try:
            data.pop(indexOfrecordToBeDeleted)
        except IndexError:      # exception error grouping
            print("Nie ma takiego id: {}\nNic nie zostalo usuniete".format(recordToBeDeleted))

        with open('spis_uczniow.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for i in data:
                writer.writerow(i)

    def writeSingleLineCSV(self):
        header, data = self.writePreviousData()
        count = 1
        with open(self.obiekt, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            userInputData = input("Podaj nowy rekord bazy danych: (komorki rozdziel spacja) ").split(' ')
            userInputData.insert(0,1 + len(data))
            data.append(userInputData)
            # write the data
            for i in data:
                writer.writerow(i)


if __name__ == '__main__':
    handler = CSVHandler('spis_uczniow.csv')
    handler.initialCsvFactory()
    handler.userReadCSV()

    handler.writeSingleLineCSV()
    handler.writeSingleLineCSV()
    handler.deleteSingleRecord()
    handler.userReadCSV()

# obiekt do obslugi bazy danych