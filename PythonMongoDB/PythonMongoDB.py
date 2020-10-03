from pymongo import MongoClient
from random import randint


client = MongoClient("192.168.1.36:27017")
def createDatabase():
    # creating database name player
    db = client.player
    names = ["Gerrard", "Torres", "Chondan"]
    positions = ["MF", "ST", "MF"]
    # adding data to collection name liverpoo;
    # result = db.liverpool.insert_one({"Chondan":"Midfield"})

    for x in range(1, 21):
        data = {
            "name": names[randint(0, len(names) - 1)] + " " + names[randint(0, len(names) - 1)],
            "position": positions[randint(0, len(positions) - 1)]
        }
        db.liverpool.insert_one(data)

    print("finished creat 20 player")
# Important!: In mongoDB, a database is not created until it gets content
# MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection)

# Check if Database Exists
def listDatabaseNeme():
    print(client.list_database_names())
# listDatabaseNeme();

def listCollection(database):
    db = client[database]
    print(db.list_collection_names())

# ----- CreateColection
def createColection():
    db = client["newDatabase"]
    mycol = db["customers"]
    db.customers.insert_one({
        "id": 1, 
        "name": "Chondan"
    })
    print(db.list_collection_names())
# createColection();

# ------ Insert Into Collection
def insertIntoCollection(database, collection, data):
    db = client[database]
    mycol = db[collection]
    x = mycol.insert_one(data)
    # Return the _id Field
    print(x, "\n", x.inserted_id)
    # If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
data = {"_id": 10, "name": "Lionel Messi", "team": "Barcelona", "nation": "Spain"}
# Insert with specified IDS -> If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the docement(s)
# insertIntoCollection("newDatabase", "customers", data)

# ------ Insert Multiple Documents
def insertManyIntoCollection(database, collection, dataList):
    # To insert multiple documents into a collection in MongoDB, we use the insert_many() method
    # The first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert
    db = client[database]
    mycol = db[collection]
    x = mycol.insert_many(dataList)
    print("{} document(s) inserted into the collection".format(len(dataList)))
    # The insert_many() method returns a InsertManyResult object, which has a property, insert_ids, that holds the ids of the inserted documents
    print(x.inserted_ids)
team = "Liverpool"
position = ("ST", "MF", "DF", "GK")
data = [{"name": "Mohamed Salah", "team": team, "position": position[0]},
        {"name": "Roberto Firmino", "team": team, "position": position[0]},
        {"name": "Virgil Van Dijk", "team": team, "position": position[2]},
        {"name": "Alisson Becker", "team": team, "position": position[3]}
        ]
# insertManyIntoCollection("newDatabase", "customers", data)

# ----- MongoDB Find
def mongodbFind(database, collection, findOne=True, query={}, condition=None):
    """ to find one enter findOne = True (boolean), to find all enter findOne = False (boolean)
    By default, the findOne was set to True\n
    set condition which field to be returned.
    For Example: condition = {'_id':0, 'name':1, 'address':1} will return only name and address field, not the _id\n
    query is used to filter the document. For Example: query = {'address': 'Park Lane 38'}
    By default, the query was set to {} which mean no filter"""

    # By default, the first string in the body of a method is used as its docstring (or documentation string). Python will use this when help() is called for that method

    # In MongoDB we use the find and findOne methods to find data in a collection
    # --- Finde One -> The find_one() method returns the first occurence in the selection
    db = client[database]
    mycol = db[collection]

    if (findOne != True):
        result = mycol.find(query)
        if (condition):
            result = mycol.find(query, condition)
        for x in result:
            print(x)
        return
    result = mycol.find_one(query)
    if (condition):
        result = mycol.find_one(query, condition)
    print(result) 
# mongodbFind("newDatabase", "customers", findOne=False);
# mongodbFind("newDatabase", "customers", findOne=False, condition={"_id": 0})
# mongodbFind("newDatabase", "customers", False, {"_id": 0, "address": 0})
# --- You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields in the _id field)
# mongodbFind("newDatabase", "customers", findOne=False, condition={"_id": 0, "name": 1, "address": 1})
# --- If you specify a field with the value 0, all other fields get the value 1, and vice versa 
# mongodbFind("newDatabase", "customers", findOne=False, condition={"address": 0})
    
def showData(database, collection):
    # db = client.database
    db = client[database]
    for p in db[collection].find():
        print(p)
# showData("newDatabase", "customers");

# ----- MongoDB Query
def mongodbQuery():
    # --- Filter the Result -> When finding a documents in a collection, you can filter the result by using a query object
    # The first argument of the find() method is a query object, and is used to limit the search

    # mongodbFind("newDatabase", "customers", findOne=False, query={"team": "Liverpool"})
    # --- Advanced Query -> To make advanced queries you can use modifiers as values in the query object
    # E.g. to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}
    
    # mongodbFind("newDatabase", "customers", findOne=False, query={"position": {"$gt": "G"}})
    # --- Filter With Regular  Expressions (Regular expressions can only be used to query strings)
    # E.g. to find the documents where the "position" field start with the letter "S", use the regular expression {'$regex': '^S'}
    mongodbFind("newDatabase", "customers", findOne=False, query={"position": {"$regex": "^[GK]"}})
# mongodbQuery();

# ----- MongoDB Sort
def mongodbSort():
    # --- Use the sort() method to sort the result in ascending or descending order
    db = client["newDatabase"]
    mycol = db["customers"]
    mydoc = mycol.find().sort([("team", -1), ("name", 1)])
    for x in mydoc:
        print(x)
    # sort("name", 1) -> ascending
    # sort("name", -1) -> descending
# mongodbSort();

# ----- MongoDB Delete Document
def mongodbDeleteDocument(database, collection, deleteOne=True, query={}):
    # --- To delete one document, we use the delete_one() method -> The first parameter of the delete_one() method is  query object defining which document to delete
    # Note: If the query finds more than one document, only the first occurrence is deleted

    db = client[database]
    mycol = db[collection]
    # Delete one Document
    if (query):
        if (deleteOne != True):
            x = mycol.delete_many(query)
            print(x.deleted_count, "documents deleted.")
            return
        try:
            mycol.delete_one(query)
            print("Delete success")
        except:
            print("There is an error.")
# mongodbDeleteDocument("newDatabase", "customers", query={"address": "Barcelona"})
# mongodbDeleteDocument("newDatabase", "customers", query={"team": "Barcelona"})
# mongodbDeleteDocument("newDatabase", "customers", deleteOne=False, query={"name": {"$regex": "^T"}})

# ----- Delete All Documents
def deleteAllDocuments(database, collection):
    db = client[database]
    mycol = db[collection]
    x = mycol.delete_many({})
    print(x.deleted_count, " documents deleted.")

# insertIntoCollection("newDatabase", "customers", {"name": "Kevin de bruyne", "team": "Sunderland", "positon": "ST"})
# insertIntoCollection("phone", "samsung", {"model": "Galaxy S9+", "price": 30000})

# mongodbDeleteDocument("phone", "samsung", deleteOne=False, query={}) # Delete all of the documents
# showData("phone", "samsung")

# showData("newDatabase", "customers");
# listDatabaseNeme();
# listCollection("phone")

# ----- MongoDB Drop Collection
def mongodbDropCollection(database, collection):
    # --- Delete Collection -> You can delete, or collection as it is called in MongoDB, by using the drop() method
    db = client[database]
    mycol = db[collection]
    mycol.drop()
    print("drop success")

# ----- MongoDB Update 
def mongodbUpdate(database, collection, query, newvalues, updateOne=True):
    # --- Update Collection -> You can update a record, or document as it is called in MongoDB, by using the update_one() method
    # The first parameter of the update_one() method is a query object defining which document to update
    # The second parameter is an object defining the new values of the document
    db = client[database]
    mycol = db[collection]
    if (updateOne != True):
        x = mycol.update_many(query, newvalues)
        print(x.modified_count, "documents updated")
        return
    x = mycol.update_one(query, newvalues)
    print("1 document updated")

# mongodbUpdate("football", "players", {"name": "Kevin de bruyne"}, {"$set": {"team": "Manchester city"}})
# mongodbUpdate("football", "players", query={"team": {"$regex": "^B[aeiou]riram\sutd"}}, newvalues={"$set": {"team": "Liverpool"}}, updateOne=False)

# ----- MongoDB Limit
def mongodbLimit(database, collection, limitNumbers):
    # --- Limit the Result => To limit the result in MongoDB, we use the limit() method
    db = client[database]
    mycol = db[collection]
    # print(mycol.find().count())
    myresult = mycol.find().limit(limitNumbers)
    for x in myresult:
        print(x)

mongodbLimit("football", "players", 3)
    
# showData("football", "players")


