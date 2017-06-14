"""
    Creates a DB storage using cassandra
    :Author: Jhesed Tacadena
    :Date: 2017-06-14
"""

# ------------------------------------------------------------------------------
# SECTION :: Imports
# ------------------------------------------------------------------------------

from cassandra.cluster import Cluster
from base import BaseDB


class CassandraDB(BaseDB):
    """
    Extends BaseDB to user Cassandra as the base DB
    """

    # --------------------------------------------------------------------------
    def __init__(self, cluster_name='cdb'):
        self.cluster = Cluster()
        self.session = self.cluser.connect(cluster_name)

    # --------------------------------------------------------------------------
    def save(self, key, value, table='tmp_table'):
        """
        Saves data
        """

        query = "INSERT INTO {} ({}) VALUES ('{}')".format(table, key, value)
        return self.session.execute(query)

    # --------------------------------------------------------------------------
    def retrieve(self, key, value, table='tmp_table'):
        """
        Obtains specific data
        """

        query = "SELECT * FROM {} WHERE {} = '{}'".format(table, key, value)
        return self.session(query)

    # --------------------------------------------------------------------------
    def retrieve_all(self, table='tmp_table'):
        """
        Obtains all data from table
        """

        query = "SELECT * FROM {}".format(table)
        return self.session(query)

