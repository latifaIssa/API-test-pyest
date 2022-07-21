import csv
from Helpers.Helper import Helper


class CsvHelper:


    def __init__(self, path):
        self.values = []
        with open(Helper.get_path(path), mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                self.values.append(row)
            csv_file.close()

    def __get_data(self, method_type):

        data_list = [row for row in self.values if str(row[0]).lower() in method_type
                     and (Helper.get_classification() == "" or Helper.get_classification() in str(row[11]).split(","))]

        for data in data_list:
            data.pop(11)
            data.pop(0)

        return data_list

    def get_post_data(self):

        return self.__get_data('post')

    def get_all_data(self):

        return [row for row in self.values]

    def get_get_data(self):

        return self.__get_data('get')

    def get_put_data(self):

        return self.__get_data('put')

    def get_patch_data(self):

        return self.__get_data('patch')

    def get_delete_data(self):

        return self.__get_data('delete')