
class Reporter:
    def __init__(self):
        self.result_file = open('Report/report.log', 'w')

    def start_report(self, file_name):
        self.result_file.write('\n\nTesting of {} was started\n'.format(file_name))

    def start_case(self, file_name):
        self.result_file.write("\n\nTest case '{}'".format(file_name))

    def add_pass(self, query, actual_result):
        self.result_file.write("\nQuery: {0}"
                               "\nTEST PASS: Result is '{1}' as expected".format(query,actual_result))

    def add_fail(self, query, actual_result, expected_result):
        self.result_file.write("\nQuery: {0}"
                               "\nTEST FAIL: Result is '{1}', but expected '{2}".format(query, actual_result, expected_result))

    def finish_report(self):
        self.report_file.close()
