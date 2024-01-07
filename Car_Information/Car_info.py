import csv

class CarInfo:
    def __init__(self, filename):
        self.filename = filename
        self.carManufacturerList = self._load_manufacturers()
        self.carModelList = self._load_models()

    def _load_manufacturers(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return {row[1].lower() for row in reader}

    def _load_models(self):
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            return {row[2].lower() for row in reader}

    def prompt(self):
        carManufacturer = self._prompt_for_value("What is your car Manufacture?", self.carManufacturerList)
        carModel = self._prompt_for_value("What is your car Model?", self.carModelList)
        carYear = self._prompt_for_year("What is the year your car was manufactured?")

        return [carManufacturer, carModel, carYear]

    def _prompt_for_value(self, prompt_message, valid_values):
        while True:
            value = input(prompt_message + " ").lower()
            if value in valid_values:
                return value
            else:
                print("Input is not valid, please check your input.")

    def _prompt_for_year(self, prompt_message):
        while True:
            try:
                year = int(input(prompt_message + " "))
                if 1980 <= year <= 2023:
                    return year
                else:
                    print('Please enter a valid year from 1980 to 2023.')
            except ValueError:
                print("Invalid input. Please enter a year in numeric format.")

