import configparser
from datetime import datetime

import pyodbc


insert_query_testing_results = '''
                               INSERT INTO dbo.TestingResults 
                               (id, scene_id, model_id, transcript_id, intent_traverse, intent_name, result, score, processing_time, version, created_at)
                               VALUES
                               (newid(), newid(), newid(), newid(), ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                               '''


class PowerBiDB(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            env = PowerBiDB.get_config()

            try:
                conn = PowerBiDB._instance.conn = pyodbc.connect(
                    'DRIVER=' + env['driver'] + ';SERVER=tcp:' + env['server'] + ';PORT=1433;DATABASE=' + env['database'] + ';UID=' + env['username'] + ';PWD=' + env['password'])
                PowerBiDB._instance.cursor = conn.cursor()
            except pyodbc.Error as ex:
                print(f"Error while connecting into SQL server: {ex}")

        return cls._instance

    def __init__(self):
        self.conn = self._instance.conn
        self.cursor = self._instance.cursor

    def update_test_results(self, values):

        values = PowerBiDB.validate_values(values)

        try:
            for value in values:
                print(value)
                result = self.cursor.execute(insert_query_testing_results, value)
            self.conn.commit()
        except pyodbc.Error as ex:
            print(f"Error while inserting value:{value} into 'TestingResults': {ex}")
        else:
            return result

    def get_test_results(self):
        try:
            row = self.cursor.fetchone()
            while row:
                print(str(row[0]) + " " + str(row[1]))
                row = self.cursor.fetchone()


        except pyodbc.Error as ex:
            print(f"Error while inserting into SQL server: {ex}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()


    @staticmethod
    def get_config():
        config = configparser.ConfigParser()
        config.read('db.ini')

        env = {
                'server': config['mssql']['server'],
                'database': config['mssql']['database'],
                'username': config['mssql']['username'],
                'password': config['mssql']['password'],
                'driver': config['mssql']['driver']
        }
        return env

    @staticmethod
    def validate_values(values):
        if isinstance(values, list):
            pass
        elif isinstance(values, dict):
            values = [values]
        else:
            raise ValueError('Invalid parameters!!!')

        values_in_tuple = []
        for value in values:
            values_in_tuple.append(
                # (value['scene_id'], value['model_id'], value['transcript_id'], value['intent_traverse'], value['intent_name'], value['result'], value['score'], value['processing_time'],
                (value['intent_traverse'], value['intent_name'], value['result'], value['score'], value['processing_time'],
                 value['version'])
            )
        return values_in_tuple


if __name__ == '__main__':

    results_value = {
        'scene_id': None,
        'model_id': None,
        'transcript_id': None,
        'intent_traverse': 3,
        'intent_name': None,
        'result': None,
        'score': 0.20,
        'processing_time': None,
        'version': None
    }

    # 'intent_name': ['Meaning', 'Sentence', 'Keyword'],
    # 'result': [0.20, 0.50, 0.20],

    db = PowerBiDB()
    db.update_test_results(values=results_value)


