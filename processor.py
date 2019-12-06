import glob

class Processor:
    def __init__(self,configuration,connector,reporter):
        self.configuration = configuration
        self.connector = connector
        self.reporter = reporter

    def execute(self):
        test_data_files = self.find_test_data()
        for file in test_data_files:
            self.run_test(file)

    def find_test_data(self):
        test_data_folder = self.configuration.get_test_cases()
        return [f for f in glob.glob(test_data_folder + '/*.json', recursive=True)]

    def run_test(self, file_name):
        self.reporter.start_report(file_name)

        with open(file_name) as file:
            test_data = eval(file.read())

            for test in test_data['tests']:
                self.reporter.start_case(test['test_name'])

                query = test['query']
                expected_result = test['expected']
                actual_result = self.connector.execute_query(query)

                if actual_result == expected_result:
                    self.reporter.add_pass(query, actual_result)
                else:
                    self.reporter.add_fail(query, actual_result, expected_result)
