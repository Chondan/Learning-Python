# Python Indentation 
# Indentation refers to the spaces at the begining of a code line
# Python uses identation to indicate a block of code

# if (5 > 2): print("Five is greater than two")
# The number of spaces is up to you as programmer, but it has  to be at least one

# ------ You have to use the same  number of spaces in the same block of code, otherwise Python will give you an error
# if 1 < 20: 
#     print(True) 
#     print("Yep")

# ------ Python Variables -> In Python, variables are created when you assign a value to it
# x = 5;
# greeting = "Hello world!";
# print(x, greeting)

# ------ Assign Value to Multiple Variables
def assignVariables():
    a, b, c = 1, 2, 3
    myName = "Chondan Susuwan"
    print(a + b + c)

# assignVariables();
# print("My name is " + myName)

# ------ Data Types
def dataTypes():
    x = 90;
    print(type(x))

    x = range(6)
    for i in x:
        print(i)

    x = b"Hello"
    print(x.__sizeof__())
# dataTypes();

# ----- Numbers
import random
def numbers():
    x = 3 + 5j
    y = 3 - 5j
    print(x * y)

    # Random Number
    check = 5
    txt = ""
    while (check > 0):
        x = random.randrange(1, 10) # random number between 1 and 9
        txt += str(x) + " "
        check -= 1
    print(txt)
# numbers();

# ----- Casting
def casting():
    # There may be times when you want to specify a type on to a variable. This can be done with casting.
    intX = int(1)
    floatX = float(1)
    y = 1
    z = 1
    print(intX, floatX, y, z)
# casting();

# ----- Strings
def strings():
    # Multiline Strings -> You can assign a multiline string to a variable by using three quotes
    hi = """Hello, 
    My name is 
    Chondan Susuwan."""
    print(hi)

    # Strings are Arrays -> Strings in Python are arrays of bytes representing unicode characters
    a = "Hello world"
    print(a[0])

    # Slicing -> You can return a range of character by using  the slice syntax
    print(a[2:5])

    # Negative  Indexing
    print(a[-5:-2])

    # String Length
    print("The length of string 'a' is " + str(len(a)))

    # String Methods
    # The strip() method removes any whitespace from the beginning or the end
    newStrng = " Hello, How are you? "
    print(newStrng)
    print(newStrng.strip())
    # The lower() method returns the string in lower case
    print(newStrng.lower())
    # The replace() method replaces a string with another string
    print(newStrng.replace("o", "a"))
    print(newStrng.replace("o", "a", 1))
    # The split() method splits the string into substring if it finds instances of the separator
    print(newStrng.strip().split(" "))
    # Check String -> To check if a certain phrase or character is present in string, we can use the keywords in or not in
    txt = "The rain in Spain stays mainly in the plain"
    for e in txt:
        if (e == 'e'):
            print("Whoah")
    x = "ain" in txt
    print(x)
    x = "ain" not in txt
    print(x)
    # String Concatenation
    fname = "Chonan"
    lname = "Susuwan"
    print(fname + " " + lname)
    # String Format
    # We can combine strings and numbers by using the format() method!
    # The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
    age = 22
    money = 0
    txt = "I am {0} years old. I have {1} THB."
    print(txt.format(age, money))
    # Escape Character
    # To insert characters that are illegal in string, use an escape character
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)
# strings();

# ----- Booleans
def booleans():
    x = 10
    y = 0
    def check(num):
        if (num):
            print("The value of num is {0}".format(num))
        else:
            print("The value of num is 0 or null.")
    check(x)
    check(y)
    # Most Values are True
    # Alomost any value is evaluated to True if it has some sort of content
    print(bool(False), bool(None), bool(0), bool(""), bool(()), bool([]), bool({}))

    # Functions can Return a Boolean
    def IsEven(num):
        if (num % 2 != 0):
            return False
        return True
    def TellMeIsThisNumEven(x):
        if (IsEven(x)):
            print("{} is even.".format(x))
        else:
            print("{} is odd.".format(x))
    TellMeIsThisNumEven(8)
    # Pthon also has many built-in functions that returns a boolean value, like the isinstance() function, 
    # which can be use to determine if an object is of a certain data type
    x = 200.00
    print(isinstance(x, int), "{} is not an instance of integer".format(x))
# booleans();

class myclass():
    name = ""
    def __init__(self, name):
        if (name != None):
            self.name = name
    def __len__(self):
        return len(self.name)
    
def runClass():
    myobj = myclass(None)
    myobj2 = myclass("Chondan")
    print(bool(myobj))
    print(bool(myobj2), myobj2.__len__())
# runClass();

# ----- Operators
def operators():
    # Arithmetic Operators
    x = 15 // 7 # floor division
    print("15 // 7 = {}".format(x))    
    # Binary  Operation
    print(5 | 3) # 101 | 011 = 111 (which is equal to 7)
    # Identity Operators
    a = 10; b = 10.0
    print(a == b, a is b)
    # Membership Operators
    fruits = ["Apple", "Banana"]
    print("Apple" in fruits)
    # Bitwise Operators
    print(~10)
    print(10<<1)
# operators();

# ----- Lists
def lists():
    cars = ["Aston Marin", "BMW", "Mazda"]
    del cars[2]
    print(len(cars), cars)
    # Copy a List 
    # You cannot copy a list simply by typing list2 = list1, because list2 will be a reference to list1.
    cars2 = cars.copy()
    cars2.append("Ford")
    print(cars, cars2)
    # Join two lists
    nums = [1, 2, 3]
    print(nums + cars2)
    # You can use the extend() method, which purpose is to add elements from one list to another list
    nums2 = [4, 5, 6]
    nums.extend(nums2)
    print(nums)
    # The list() Constructor
    # It is also possible to use the list() constructor to make a new list
    fruits = list(("Apple", "Banana"))
    print(fruits)  
# lists();

# ----- Tuples
def tuples():
    # A tuple is collection which is ordered and unchangeable
    thistuple = ("Apple", "Banana", "Cherry", "Orange", "Kiwi", "Mango")
    print(thistuple[0])
    # Negative Indexing
    print(thistuple[-1])
    # Range of Indexes
    print(thistuple[1: 4])
    # Change Tuple Values
    # Once a tuple is created, you cannot change its value. Tuples are unchangable, or immutable as it also is called
    # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple
    tupleNumbers = (1, 2, 3, 4)
    listNumbers = list(tupleNumbers)
    listNumbers[-1] = 5
    tupleNumbers = tuple(listNumbers)
    print(tupleNumbers)
    # Loop Through a Tuple
    def loopThroughTuple():
        txt = ""
        for x in tupleNumbers:
            txt += str(x) + " "
        print(txt)
    loopThroughTuple();
    # Check if Item Exists
    def checkItemExists(item, tuple):
        if item in tuple:
            print("Yes, {} is in the numbers tuple.".format(item))
        else:
            print("No, {} is not in the numbers tuple.".format(item))
    checkItemExists(5, tupleNumbers)
    # Add Items
    # Once a tuple is created, you cannot add items to it. Tuples are unchangeable

    # Create Tuple With One Item
    # To create a tuple with only one item, you have to add a common after the item, otherwise Python will not recognize it as a tuple
    garage = ("Honda", )
    cars = ("Toyota") # The type is string
    print(type(garage), garage, type(cars), cars)

    # Remove Items
    # Tuples are unchangeble, so you cannot remove items from it, but you can delete the tuple completely
    del garage
    print("garage" in locals(), "The garage tuple have been deleted.")
    print(locals())
    print(locals().keys())
# tuples();

# ----- Sets
def sets():
    # A set is collection which is unordered and unindexed. In Python sets are written with curly brackets
    fruits = {"Apple", "Banana", "Cherry"}
    print(fruits)
    # Access Items
    # You cannot access items in a set by referring to an index, since sets are unordered the items has no index
    # But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword
    for f in fruits:
        print(f)
    # Check Item
    print("Apple" in fruits, "Apple is in fruits set")    
    # Change Items -> Once a set is created, you cannot change its items, but you can add new items

    # Add Items
    fruits.add("Mango")
    print(fruits)
    # Add Multiple items to a set, using the update() method
    fruits.update(["Orange", "Apple", "Lemon"])
    print(fruits)
    # Get the Length of a Set
    print(fruits, len(fruits))
    # Remove Item -> To remove an item in a set, use the remove(), or the discard() method
    fruits.remove("Lemon") # If the item to remove does not exist, remove() will raise an error
    print(fruits)
    fruits.discard("Lemon") # If the itme to remove does not exist, discard() will NOT raise an error
    print(bool(fruits.discard("Lemon")), fruits)
    # Join Two Sets
    # You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts  all the items from one set into another
    set1 = {"a", "b", "c"}
    set2 = {1, 3, 4}
    # set1 = set1.union(set2)
    # print(set1, set2)
    # set3 = set1.union(set2)
    # print(set3)
    set1.update(set2)
    print(set1)        
# sets();

# ------ Dictionaries
def dictionaries():
    # A dictionary is a collection which is unordered, changeable and indexed.
    # In Python dictionaries are written with curly bracket, and they have keys and values
    cars = {
        "brand": "Aston Martin",
        "model": "DB11",
        "year": 2020,
        "num": [1, 2, 3, 4, 5]
    }
    print(cars)
    # Accessing Items
    print(cars["brand"], cars["num"])
    # There is also a method called get() that will give you the same result
    print(cars.get("model"))
    # Change Values
    # You can change the value of a specific item by referring to its key name
    cars["model"] = "DB9"
    print(cars)
    # Loop Through a Dictionary
    def loopThroughDict(dict):
        txt = ""
        check = 0
        for x in dict:
            if (check == 3):
                continue
            txt += str(dict[x]) + " "
            check += 1
        print(txt)
    loopThroughDict(cars)
# dictionaries();

# ----- If...Else
def ifElse():
    a = 3; b = 3;
    if (b > a):
        print("b is greater than a")
    elif (a == b):
        print("a and b are equal")
    else:
        print("a is greater than b")
    # Shorthand If
    print("A") if a > b else print("B") if a < b else print("equal")
    # The pass Statement
    # if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
    if (b != a):
        pass
    else: 
        print("Hello")
# ifElse();

# ----- While Loops
def whileLoops():
    i = 0
    txt = ""
    while (i < 10):
        if (i == 2):
            i += 1
            continue
        if (i >= 7):
            break
        txt += str(i) + " "
        i += 1;
    print(txt)
# whileLoops();

# ----- For Loop
def forLoop():
    txt = ""
    for x in range(1, 11):
        txt += str(x) + " "
    else:
        print("Fisnished")
    print(txt)

    # Nested Loop
    for i in range(2, 4):
        for j in range(1, 13):
            print("{0} x {1} = {2}".format(i, j, i * j))
# forLoop();

# Functions
def functions():
    # default arguments
    def greeting(name, phrase = "How are you?"):
        print("Hello " + name + ", " + phrase)
    greeting("Chondan");
    # Parameters or Arguments?
    # A parameter is the variable  listed inside the parentheses in the functino definition
    # An argument is the value that is sent to the function when it is called

    # Arbitary Argument, *args
    def youngestKid(hi, *kids):
        print(hi + ", The youngest is " + kids[2])
    youngestKid("Hello", "Emil", "Tobias", "Linus")
    # Keyword Arguments
    def hi(name, age):
        print("My name is " + name + ". I am " + str(age) + " years old.")
    hi(age = 22, name = "Chondan");
    # Arbitary Keyword Argument, **kwargs
    def introduce(**person):
        print("His last name is " + person["lname"])
    introduce(fname = "Chondan", lname = "Susuwan")
    # pass dictionary to function
    dict = {"name": "Chondan", "age": 22}
    def hello(name, age):
        print(name, age)
    hello(**dict)
    # Passing a List as an Argument
    def showFruits(fruitsList):
        txt = ""
        for f in fruitsList:
            txt += f + " "
        print(txt)
    showFruits(["Apple", "Banana", "Cherry"])
    # Recursion
    def sumBetween(a, b):
        if (a < b):
            return a + sumBetween(a + 1, b)
        else:
            return a
    print(sumBetween(4, 10))
# functions();

# ----- Lambda
def lambdaFunction():
    x = lambda a, b : a * b
    print(x(5, 3))
    # Why use lambda function?
    # The power of lambda is better shown when you use them as an anonymous function inside another function
    def myFunc(n):
        return lambda x : x * n
    double = myFunc(2)
    triple = myFunc(3)
    print(double(10))
    print(triple(20))
# lambdaFunction();

# ----- Classes and Objects
def classesAndObjects():
    # Python is an object oriented programming language
    # Almost everything in Python is an object, with its properties and methods
    class cars:
        def __init__(self, brand):
            self.brand = brand
        def __len__(self):
            return len(self.brand)
    car1 = cars("Aston Martin");
    print(car1.brand)
    class persons:
        badhabit = "Smoking"
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def greeting(self):
            return self.name + " " + str(self.age)
    person1 = persons("Chondan", 22)
    print(person1.greeting())
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class

    # Modify Object Properties
    person1.age = 23
    print("Next year " + person1.name + " will be " + str(person1.age) + " years old.")
    person2 = persons("badGuys", 18)
    # print(person1.badhabit)
    # del person1.badhabit # delete all object's badhabit attributes
    # print(person2.badhabit)

    # The pass Statement
    # class definition cannot be empty, but if you for some reason have a class definition with no conten, put in the pass statement to avoid getting an error

    # Python Inheritance
    class Son(persons):
        def __init__(self, name, age, toy):
            persons.__init__(self, name, age)
            self.toy = toy           
    myson = Son("Trent", 5, "Play Station")
    print(myson.greeting() + " love playing " + myson.toy)
    # use the super() Function to inherit all the methods and properties from its parent
    class Daughter(persons):
        def __init__(self, name, age, toy):
            super().__init__(name, age)
            self.toy = toy
        def welcome(self):
            print("Hello, My name is " + self.name)
    mydaughter = Daughter("Anna", 3, "Dolls")
    print(mydaughter.greeting() + " love playing " + mydaughter.toy)
    mydaughter.welcome();
# classesAndObjects();

# ----- Iterators
def iterators():
    # An iterator is an object that contains a countable number of values
    # An iterator is an object that can be iterated upon, meaning that you can traverse through  all the values
    # Tehcnically, in Python, an iterator is an object which implements the iterator protocol, which consist of the method __iter__() and __next__()

    # Iterator vs Iterable
    # Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from
    myTuple = ("Apple", "Banana", "Cherry")
    myIterator = iter(myTuple)

    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))
    # print(next(myIterator)) #  give an error (out of index)

    # Looping through an Iterator
    for f in myTuple:
        print(f)

    # --- Create an Iterator
    # To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object
    class myNumbers:
        def __iter__(self):
            self.a = 1
            return self
        def __next__(self):
            if (self.a > 5):
                raise StopIteration
            else:
                x = self.a
                self.a += 1
                return x 

    nums = myNumbers();
    myiter = iter(nums)

    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))

    # StopIeration
    # The example above would continue forever if you had enough next() statements, or if it was used in a for loop
    # To prevent the iteration to go on forever, we can use the StopIteration statement
    for x in myiter:
        print(x)

    print("-------------")
    # --- Create my own array
    class ArrayList:
        def __init__(self):
            self.myArray = list()
        def add(self, item):
            self.myArray.append(item)
        def size(self):
            return len(self.myArray)   
        def getVal(self, index):
            if (index < self.size()):
                return self.myArray[index]
            else:
                return "Out of index"
    arr = ArrayList();
    arr.add(3)
    arr.add(5)
    print(arr.size())
    print(arr.getVal(1))
    print(arr.getVal(10))
# iterators();

# ----- Scoper
def scope():
    # A variable is only available from inside the region it is created. This is called scope

    # Local Scope -> A variable inside a function belongs to the local scope of that function, and can only be used inside that function
    
    # Function Inside Function
    # The variable is not available outside the function, but it is available for any function inside the function
    
    # Global Scope
    # A variable created in the main body of the Python code is a global variable and belongs to the global scope

    global x
    x = 50
# x = 10
# scope();
# print(x)
    
# ----- Modules
def modules():
    # What is a Module?
    # Consider a module to be the same as a code library
    # A file containing a set of functions you want to include in your apllication
    import module1
    module1.helloWorld();

    # Variables in Module
    # The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
    print(module1.module1Var)
    person = module1.person
    print(person["name"], person["age"], person["country"])

    # Naming a Module
    # Re-naming a Module -> You can create an alias when you import a module, by using the as keyword

    # Built-in Modules
    # There are several built-in modules in Python, which you can import whenever you like
    import platform as p
    print(p.system())

    # Using the dir() Function
    # use dir() function to list all the function names (or variable names) in a module
    allFunction = dir(module1)
    print(allFunction)

    # Import From Module
    # You can choose to import only parts from a module, by using the from keyword
    from platform import system as s
    print(s())
# modules();

# ------ Datetime
def dateTime():
    # A date in Python is not a date type of its own, but we can import a module named dateTime to work with dates as date objects
    import datetime
    timeNow = datetime.datetime.now()
    print(timeNow)
    # The datetime module has many  methods to return information about the date object
    print(timeNow.year)
    print(timeNow.month)
    print(timeNow.day)
    print(timeNow.strftime("%A"))
    # Creating Date Objects
    tomorrow = datetime.datetime(timeNow.year, timeNow.month, timeNow.day + 1)
    print(tomorrow.date(), tomorrow)
    # The strftime() Method
    # The datetime object has a method  for formatting date objects into readable strings
    # The method is called strftime(), and take one parameter, format, to specify the format of the returned string
    print(tomorrow.strftime("%A"), tomorrow.strftime("%B"), timeNow.strftime("%X"))
# dateTime();

# ----- Math
def math():
    nums = [1, 2, 3, 4]
    # nums = tuple(nums)
    minn = min(nums)
    print(type(nums), minn)
    print(pow(2, 10))
    print(abs(-122))
    # The Math Module
    import math
    print(math.sqrt(64))
    x = 1.3
    xup = math.ceil(x)
    xdown = math.floor(x)
    print(xup, xdown)
    square = lambda x : x * x
    def areaCircle(r):
        return math.pi * square(r) 
    print("The are of circle which has 7 unit radius is {} unit-square".format(areaCircle(7)))
# math();

# ----- JSON
def pythonJson():
    # JSON in Python -> Python has a built-in package called json, which can be used to work with JSON data

    # Parse JOSN - Convert from JSON to Python -> The result will be a Python dictionary
    import json
    jsonString = '{"name": "Chondan", "age": 22}'
    obj = json.loads(jsonString)
    print(obj)
    print("Hello, I am {0}. I am {1} years old.".format(obj["name"], obj["age"]))

    cars = {
        "brand": "Aston Martin",
        "model": "DB11",
        "year": 2020,
        "enging": "V12"
    }
    jsonCars = json.dumps(cars)
    print(jsonCars, type(jsonCars))
    # When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript)
    numbers = (1, 2, 3, 4)
    score = {
        "math": numbers
    }
    jsonScore = json.dumps(score)
    print(jsonScore, json.loads(jsonScore)["math"][1])
    # Format the Result
    # The example above prints a JSON string, but it is not very easy to read, with no indentations and lines breaks
    # The json.dumps() method has parameters to make it easier to read the result
    print(json.dumps(score, indent = 4))
    # order the result
    print(json.dumps(cars, indent=4, sort_keys=True))
# pythonJson();

# ----- RegEx
def regEx():
    # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern
    # RegEx can be used to check if a string contains the specified search pattern
    import re
    txt = "The rain in Spain"
    srch = re.search("^The.*Spain$", txt)
    print(srch)

    # The findall() Function
    srch = re.findall("ai", txt)
    print(srch)

    # The search() Function
    # The search() function searches the string for a match, and returns a Match object if there is a match. If there is more than one match, only the first occurrence of the match will be returned
    srch = re.search(r"ain\b", txt) 
    # the 'r' in the beginning is making sure that the string is being treated as a 'raw string'
    # raw string -> Python raw string treats backslash as a literal character.
    # This is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character
    print("hi\nhello")
    print(r"hi\nhello")
    print("The first 'ain' is located in position: ", srch.start())

    # The split() Function
    # The split() function returns a list where the string has been split at each match
    srch = re.split("\s", txt)
    print(srch)
    # The sub() Function
    # The sub() function replaces the mathces with the text of your choice
    srch = re.sub("\s", "-", txt)
    print(srch)
    # You can control the number of replacements by specifying hte count parameter
    srch = re.sub("\s", "-", txt, 2)
    print(srch)

    # Match Object 
    # A Match Object is an object containing information about the search and the result
    # If there is no match, the value None will be returned, instead of the Match Object
    srch = re.search(r"\bS\w+", txt)
    print(srch, srch.span(), srch.group(), srch.string)
# regEx();

# ----- PIP
def pip():
    # What is PIP?
    # PIP is a package for Python packages, or modules if you like

    # What is a Package?
    # A package contains all the files you need for a module
    # Modules are Python code libraries you can include in your project

    import camelcase
    c = camelcase.CamelCase()
    txt = "hello world"
    print(c.hump(txt))
# pip();

# ----- Try Except
def tryExcept():
    # The try block lets you test a block of code for errors. The except block lets you handle the error. 
    # The finally block lets you execute code, regardless of the result of the try- and except blocks
    x = 1
    try:
        print(x)
    except:
        print("An exception occured")    
    
    # Many Exceptions
    # You can define as many exception block as you want, e.g. if you want to execute a special block of code for a special kind of error
    try:
        print(a)
    except NameError:
        print("Variable a is not define")
    except:
        print("Something else went wrong")
    
    # Else and Finally
    try: 
        print("Hello world")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong") # You can use else keyword to define a block of code to be executed if no errors were raised
    finally: 
        print("Finished") # The finally block, if specified, will be execute regardless if the try block raises an error or not

    # Finally is useful to close objects and clean up resources
    try:
        f = open("./Note.txt")
        print(f.readline())
    except: 
        print("Something went wrong when reading the file")
    finally:
        f.close()

    # Rais an exception
    # As a Python developer you can choose to throw an exception if a condition occurs
    # To throw (or raise) an exception, use the raise keyword

    # x = -1
    # if (x < 0):
    #     raise Exception("Sorry, no numbers below zero")

    x = "hello"
    if not type(x) is int:
        raise TypeError("Only tntegers are allowed")

# tryExcept();

# ----- User Input
def userInput():
    name = input("Enter your name: ")
    print("Hello " + name + ", How are you?")

    a, b, c = input().split(" ")
    print(a, b, c)

    a, b, c = input().split("/")
    print(a, b, c)

    a, b, c = [int(x) for x in input("Enter 3 numbers: ").split()]
    print("The sum is {}".format(a + b + c))
# userInput();

# ----- String Formatting
def stringFormatting():
    # To make sure a string will display as expected, we can format the result with the format() method

    # String format()
    # The format() method allows you to format selected parts of a string
    price = 2e6
    print("The price is {} dollars".format(price))
    price = 49
    print("The price is {} dollars".format(price))

    # You can add parameters inside the curly brackets to specify how to convert the value
    print("The price is {:.2f} dollars".format(price))

    # Named Indexes
    fname = "Chondan"
    lname = "Susuwan"
    print("Hello everyone, My name is {fname} {lname}.".format(fname = fname, lname = lname))
stringFormatting();






