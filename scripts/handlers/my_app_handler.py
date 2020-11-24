from scripts.utils.mongo_util import MongoDB

database = MongoDB("TestUtilDB")
collection = database.createCollection("Customers")


def create(add_user):
    return MongoDB.create(collection, add_user)


def my_search(query):
    return MongoDB.search(collection, query)


def update(query, new_value):
    return MongoDB.update(collection, query, new_value)


def oupdate(query, new_value):
    MongoDB.one_update(collection, query, new_value)


def delete(query):
    return MongoDB.delete(collection, query)


def drop():
    MongoDB.drop(collection)
