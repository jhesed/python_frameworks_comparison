"""
    Creates A factory of database storages
    :Author: Jhesed Tacadena
    :Date: 2017-06-14
"""
# ------------------------------------------------------------------------------
# SECTION :: Imports
# ------------------------------------------------------------------------------

from cassandra_db import CassandraDB

# ------------------------------------------------------------------------------
# SECTION :: Static variable
# ------------------------------------------------------------------------------

db_factory = {
    'cassandra': CassandraDB
}

def get_db_store(store_name):
    """
    Helper function for retrieving database store
    """
    return db_factory[store_name]
