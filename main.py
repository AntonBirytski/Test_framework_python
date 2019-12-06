from configurator import Configurator
from connector import Connector
from processor import Processor
from reporter import Reporter

def run():
    configuration = Configurator('QA')
    database_path = configuration.get_database()
    connector = Connector(database_path)

    reporter = Reporter()

    processor = Processor(configuration, connector, reporter)
    processor.execute()

    #reporter.finish_report()

if __name__=='__main__':
    run()