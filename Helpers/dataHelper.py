class DataHelper:

    @staticmethod
    def compare_expected_with_actual(actual, expected):
        # get object's keys
        if (len(expected) > 0):
            keys = expected[0].keys()
        # Iterating through the json list
        for index, item in enumerate(expected):
            for key in keys:
                assert actual[index][key] == item[key]
