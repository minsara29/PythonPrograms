import configparser
import pyodbc

INSERT_TestingResults = '''
       INSERT INTO dbo.TestingResults 
              (Id, TranscriptId, ModelId, IntentTraverse, IntentName, Result, Score, ProcessingTime, Version, CreatedAt)
       VALUES
              (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
       '''

SELECT_TestingLabeledData = '''
        SELECT DISTINCT ld.Id, ld.SceneId, ld.Transcript
          FROM dbo.LabeledData as ld  
         INNER JOIN dbo.TestingLabeledData AS tld
            ON (ld.Id = tld.TranscriptId)
       '''

# '''
#         SELECT DISTINCT tld.TranscriptId, tld.SceneId, ld.Transcript
#           FROM dbo.TestingLabeledData AS tld
#          INNER JOIN dbo.LabeledData AS ld
#             ON (tld.TranscriptId = ld.Id)
# '''

class PowerBiDB(object):
    """
    Python SQL functions for PowerBiDB
    """
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

    def update_test_results(self, result):
        """
        Update the ML Model candidate's results in TestingLabeledData tables .

        Parameters:
        result (dict or list of dict): ML Moles candidate's result

        Returns:
        Boolean: return true if insert successful, otherwise false
        """
        values = self.validate_values(result)
        try:
            for value in values:
                self.cursor.execute(INSERT_TestingResults, value)
            self.conn.commit()
        except pyodbc.Error as ex:
            print(f"Error while inserting value:{value} into 'TestingResults': {ex}")
            return False
        else:
            return True

    def fetchall_testing_data(self):
        """
        Get all testing labeled records from table 'TestingLabeledData'

        Parameters:
        None

        Returns:
        list(dict): return all records from TestingLabeledData
        """
        try:
            self.cursor.execute(SELECT_TestingLabeledData)
            rows = self.cursor.fetchall()
        except pyodbc.Error as ex:
            print(f"Error while selecting from 'TestingLabeledData' : {ex}")

        return self.dict_data(rows)

    def fetchone_testing_data(self):
        """
        Get only one testing labeled records from table 'TestingLabeledData'

        Parameters:
        None

        Returns:
        list(dict): return only one record from TestingLabeledData
        """
        try:
            self.cursor.execute(SELECT_TestingLabeledData)
            row = self.cursor.fetchone()
        except pyodbc.Error as ex:
            print(f"Error while selecting from 'TestingLabeledData' : {ex}")

        return self.dict_data([row])

    def dict_data(self, rows):
        """
        Convert the tables' records into list of dict format

        Parameters:
        tuple: values in tuple

        Returns:
        list(dict): return in list of dict
        """
        data = []
        for row in rows:
            data.append({
                'TranscriptId': row[0],
                'SceneId': row[1],
                'Transcript': row[2]
            })
        return data

    def validate_values(self, values):
        """
        Validate the table's data

        Parameters:
        list(dict)/dict: values in tuple

        Returns:
        tuple: query placeholder
        """
        if isinstance(values, list):
            pass
        elif isinstance(values, dict):
            values = [values]
        else:
            raise ValueError(f'Invalid format: {type(values)}. Results should be either dict or list of Dict !!!')

        values_in_tuple = []
        for value in values:
            try:
                transcript_id = value['TranscriptId']
                model_id = value['ModelId']
            except KeyError as e:
                print(f'{e} must provided for insertion')
            new_id = self._get_uniqueidentifier()
            values_in_tuple.append(
                (new_id, transcript_id, model_id, value.get('IntentTraverse'), value.get('IntentName'), value.get('Result'),
                 value.get('Score'), value.get('ProcessingTime'), value.get('Version'))
            )
        return values_in_tuple

    @staticmethod
    def get_config():
        """
        Validate the table's data

        Parameters:
        None

        Returns:
        dict: PowerBi DB configuration details
        """
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

    def _get_uniqueidentifier(self):
        try:
            self.cursor.execute("SELECT NEWID() as id")
            unique = self.cursor.fetchone()
            print(unique.id)
            return str(unique.id)

        except pyodbc.Error as ex:
            print(f"Error while getting UniqueIdentifier' : {ex}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def __str__(self):
        return f"PowerBiDB SQL Operation "


if __name__ == '__main__':

    results_value = {
        'TranscriptId': 'E89C4C5B-412D-434C-A7B6-02E92CD8FEAA',
        'SceneId': 'D74B9A51-F7B1-4CA3-BCF5-C3B27C4ECB2E',
        'ModelId': 1,
        'IntentTraverse': 3,
        'IntentName': str(('intent1', 'intent2')),
        'Result': '(0, 0)',
        'Score': 0.20,
        'ProcessingTime': '00:00:05',
        'Version': 1
    }
    # 'intent_name': ['Meaning', 'Sentence', 'Keyword'],
    # 'result': [0.20, 0.50, 0.20],
    # results_value = "kannan"
    db = PowerBiDB()
    # results = db.fetchall_testing_data()
    # print(results)
    db.update_test_results(result=results_value)
    #
    # results = db.fetchone_testing_data()
    # print(results)

