import csv

class CsvParser:
    def __init__(self, file_path: str):
        self.csv_data = []

        with open(file_path) as f:
            csv_reader = csv.reader(f, delimiter=';')

            for row in csv_reader:
                self.csv_data.append(row)

    async def filter_on_test_case_id(self, test_case_id: str) -> list:
        data_list = await [row for row in self.csv_data if row.test_case_id == test_case_id]
        return data_list
