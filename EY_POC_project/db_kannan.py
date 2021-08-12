SELECT_TRIAGE_TASKS = """
    SELECT id,
           sfdcCaseID,
           issueStatus,
           resolutionMessage,
           resolutionTime
    FROM apiIssue
        WHERE sfdcCaseIDType = 'task'
          AND issueStatus IN ('Triage');
"""

UPDATE_TASK_AS_RESOLVED = """
    UPDATE apiIssue
        SET resolutionMessage = %s,
            resolutionTime = %s,
            issueStatus = "Resolved"
    WHERE id = %s
"""


class CanopyDB:
    def __init__(self, host, user, password, database):
        self.pool_cnx = self.connection_pool(host, user, password, database)



    def connection_pool(self, host, user, password, database):
        try:
            dbconfig = {
                "database": database,
                "user": user,
                "password": password,
                "host": host
            }
            return mysql.connector.pooling.MySQLConnectionPool(pool_name="canopy_sfdc",
                                                               pool_size=3,
                                                               **dbconfig)
        except Error as e:
            logger.error(f"Error while connecting to MySQL using Connection pool: {e}")
            raise SystemExit(e)

    @contextmanager
    def db_connection(self):
        connection = self.pool_cnx.get_connection()
        try:
            yield connection
        finally:
            if connection.is_connected():
                connection.commit()
                connection.close()

    @contextmanager
    def get_cursor(self):
        with self.db_connection() as connection:
            with connection.cursor() as cursor:
                yield cursor

    def get_api_issue_records(self, select_query):
        try:
            with self.get_cursor() as cursor:
                cursor.execute(select_query)
                return cursor.fetchall()
        except Error as e:
            logger.info(f"Error while Selecting MySQL: {e}")

    def update_task_status(self, update_query, values):
        try:
            with self.get_cursor() as cursor:
                for value in values:
                    try:
                        cursor.execute(update_query, value)
                    except Error as e:
                        logger.info(f"Error while updating MySQL: {e} for Value: {value}")
        except Error as e:
            logger.info(f"Error while updating MySQL: {e}")