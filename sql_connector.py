import pyodbc
import constants


# This class manages the Azure SQL DB connection
class SQLConnection:
    __instance = None
    __connection = None

    def __new__(cls):
        if SQLConnection.__instance is None:
            SQLConnection.__instance = object.__new__(cls)
        return SQLConnection.__instance

    def get_connection(self):
        if self.__connection is None:
            self.__connection = pyodbc.connect(
                "DRIVER="+constants.DRIVER+";SERVER=tcp:"+constants.SERVER+";PORT=1433;DATABASE=" +
                constants.DATABASE+";UID="+constants.USERNAME+";PWD="+constants.PASSWORD
            )

        return self.__connection

    def remove_connection(self):
        self.__connection = None
