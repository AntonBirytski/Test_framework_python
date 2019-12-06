class Configurator:
    def __init__(self,env):
        with open('Configuration.json') as c:
            self.configuration = eval(c.read())
        self.configuration = self.configuration[env]

    def get_database(self):
        return self.configuration['database']

    def get_test_cases(self):
        return self.configuration['test_case_folder']