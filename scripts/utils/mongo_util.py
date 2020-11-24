from pymongo import MongoClient


class MongoDB:  # Classes generally are camel-case, starting with uppercase
    def __init__(self, dbname):
        # the __init__ method is the class constructor, where you define
        # instance members.  We'll make conn an instance member rather
        # than a class level member
        self._conn = MongoClient("143.110.191.155", 37217)
        self._db = self._conn[dbname]

    def createCollection(self, name=""):
        return self._db[name]

    @staticmethod
    def create(collection, add_user):
        x = collection.insert_one(add_user)
        if x:
            return "Customer Record Created"
        return False

    @staticmethod
    def drop(collection):
        my_col = collection
        my_col.drop()

    @staticmethod
    def search(collection, query):
        my_col = collection
        my_doc = my_col.find(query, {"_id": 0})
        return list(my_doc)

    @staticmethod
    def update(collection, query, newvalues):
        my_col = collection
        # return( my_col.update(query, newvalues))
        x = (my_col.update(query, newvalues))
        if x:
            return "Changes Made!"
        return False

    @staticmethod
    def delete(collection, query):
        my_col = collection
        x = my_col.delete_one(query)
        if x:
            return "Deleted Document"
        # print("Document Deleted!")

    @staticmethod
    def one_update(collection, query, newvalue):
        collection.update_one(query, newvalue)
