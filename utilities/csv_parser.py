import csv

class CsvParser:
    def __init__(self, file_path: str):
        self.csv_data = []

        with open(file_path) as f:
            csv_reader = csv.reader(f, delimiter=';')

            for row in csv_reader:
                self.csv_data.append(row)

    async def filter_on_test_case_id(self, test_case_id: str) -> list:
        data_list = [row for row in self.csv_data if row[0] == test_case_id]
        username = [row[2] for row in data_list][0]
        password = [row[3] for row in data_list][0]
        expected_message = [row[4] for row in data_list][0]
        return username, password, expected_message
