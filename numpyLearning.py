import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
def gettingStart():
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)

    #  version
    print(np.__version__)
# gettingStart();

def creatingArrays():
    # Create a np ndarray Object
    list1 = [1, 3, 5, 6]
    arr = np.array(list1)
    print(type(list1), type(arr))
    # To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an array
    arr = np.array(("Apple", "Banan", "Cherry"))
    print(arr, arr[0])
    # Dimensions in Arrays -> A dimension in arrays is one level of array depth (nested array)

    # --- 0-D Arrays
    # 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array
    arr = np.array(42)
    print(type(arr), arr)
    # --- 1-D Arrays
    # An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
    arr = np.array(["Aston Maring", "BMW", "Mercedes Benz"])
    print(arr)
    # --- 2-D Arrays
    # An array that has 1-D arrays as its elements is called a 2-D array
    # These are often used to represent matrix or 2nd order tensors
    arr = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
    print(arr, arr[1][1])
    # --- 3-D Arrays
    # An array that has 2-D arrays (matrices) as its elements is called 3-D array
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(arr)
    # --- Check Number of Dimensions?
    print(arr.ndim)
    # --- Higher Dimensional Arrays
    # When the array is created, you can define the number of dimensions by using the ndim argument
    arr = np.array([1, 2, 3, 4], ndmin = 5)
    print(arr)
# creatingArrays();

# ----- Array Indexing 
def arrayIndexing():
    # ---- Acess 3-D Arrays
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(arr, arr[1][-1][-1])
# arrayIndexing();\

# ----- Array Slicing
def arraySlicing():
    # Slicing in Python means taking elements from one given index to another given index
    # We pass slice insted of index like this: [start:end:step]
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr, arr[0][0:5:2])
    print(arr[0], arr[0][:3]) # Slice elements from the beginning to index 4 (not included) 
    # --- Negative Slicing
    print(arr[0], arr[0][-3:-1])
    # --- Slicing 2-D Arrays
    print(arr[1, 1:4]) # From the second element, slice elements from index 1 to index 4 (not included)
    print(arr[:2, 2]) # From both elements, return index 2
    print(arr[:, 2]) # Retuen every other element from the entire array
    print(arr[1, ::2])
# arraySlicing();

# ----- Data Types
def dataTypes():
    # Numpy has some extra data types, and refer to data types with one character, like i for integer, u for unsigned integers
    # Checking the Data type of an array
    arr = np.array([1, 2, 3, 4, 5])
    print(arr, arr.dtype)
    arr = np.array(["Apple", "Banana"])
    print(arr, arr.dtype)
    # Creating Arrays With a Defined Data Type
    arr = np.array([1, 2, 3, 4], dtype = 'S')
    print(arr, arr.dtype, arr[0])
    # For i, u, f, S and U we can define size as well
    arr = np.array([1, 2, 3, 4], 'i4')
    print(arr, arr.dtype)
    # Converting Data Type on Existing Arrays
    # The best way to change the data type of an existing array, is to make a copy of the array with the astype() method
    arr = np.array([1.1, 2.2, 3.3])
    newarr = arr.astype('i8')
    print(arr, newarr, newarr.dtype)
    # Change data type from integer to boolean
    arr = np.array([1, 0, 3])
    newarr = arr.astype(bool)
    print(arr, newarr)
    newarr = newarr.astype('i')
    print(newarr)
# dataTypes();

# ----- Array Copy as View
def arrayCopyAsView():
    # The difference between copy and view
    # Tha main difference between a copy and a view of an array is that the copy is a new array, 
    # and the view is just a view of the original array

    # The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy
    # The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view

    # --- COPY
    arr = np.array([1, 2, 3, 4])
    copyArr = arr.copy()
    print(arr, copyArr, arr == copyArr)
    arr[0] = 10
    print(arr, copyArr)
    # --- VIEW
    arr = np.array([5, 6, 7, 8])
    viewArr = arr.view()
    print(arr, viewArr)
    arr[-1] = 25
    print(arr, viewArr)
    viewArr[0] = 50
    print(arr, viewArr)
    # ---- Check if array owns it's data
    # Every Numpy array has the attribute base that returns None if the array owns the data
    print(copyArr.base, viewArr.base) # The copyArr returns None, The view returns the original array
# arrayCopyAsView();

# ----- arrayShape
def arrayShape():
    # --- Shape of an array -> The shape of an array is the number of elements in each dimension
    # --- Get the Shape of an Array
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(arr, arr.shape, arr[1,].shape)
    arr = np.array([1, 2, 3, 4, 5], ndmin = 5)
    print(arr, arr.shape, arr[0, 0, 0, 0, 1])
    # What does the shape tuple represent?
    # Integers at every index tell about the number of elements the corresponding dimension has
# arrayShape();

# ----- Array Reshaping
def arrayReshaping():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print(arr)
    newArr = arr.reshape(2, 2, 3)
    print(newArr, newArr.ndim, newArr.base)
    newArr[1, 1, -1] = 100
    print(newArr, arr)
    # --- Unknown Dimension
    # You are allowed to have one 'unknown' dimension 
    # Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method
    # Pass -1 as the value, and NumPy will calculate this number for you
    newArr = arr.reshape(2, -1, 2)
    print(arr, "\n", newArr)
    # Flattening the arrays
    # Flattening array means converting a multidimensional array into a 1D array
    flatArr = newArr.reshape(-1)
    print(arr, newArr, flatArr, flatArr.base)
# arrayReshaping();

# ----- Iterating Arrays
def iteratingArrays():
    # Iterating means going through elements one by one
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    def loop1D(array):
        for x in array:
            print(x, end = " ")
    loop1D(arr);
    # Iterating 2-D Arrays
    arr = arr.reshape(2, -1)
    loop1D(arr);
    def loop2D(array):
        for i in array:
            for j in i:
                print(j, end = " ")
    loop2D(arr)
    # Iterating 3-D Arrays
    arr = arr.base.reshape(3, 2, -1)
    def loop3D(array):
        sum = 0
        txt = ""
        for twoD in array:
            for oneD  in twoD:
                for elem in oneD:
                    sum += elem
                    txt += str(elem) + " + "
        txt = txt[0:len(txt) - 3] + " ="
        print("\n", txt, sum)
    loop3D(arr)
    # Iterating Arrays Using nditer()
    # The function nditer() is a helping function that can be used from very basic to very advanced iterations

    # --- Iterating on Each Scalar Element
    # In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality
    arr = arr.reshape(-1)
    print(arr)
    def iteratingFunction(array):
        for x in np.nditer(array):
            print(x)
    iteratingFunction(arr)
    # --- Iterating Array With Different Data Types
    # We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating

    # Numpy does not change the data type of the element in-place (where the element is in array)
    # So it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flag = ['bufferd']
    def iteratingWithDifferentDataTypes(array):
        for x in np.nditer(array, flags = ['buffered'], op_dtypes = ['S']):
            print(x , end = " ")
    iteratingWithDifferentDataTypes(arr)
    # Iterating with different step size
    arr = arr.reshape(2, -1)
    print(arr)
    iteratingFunction(arr[:, ::2])
    # Enumerated Iteration Using ndenumerate()
    def EnumeratedIteration(array):
        for idx, x in np.ndenumerate(array):
            print(idx, x)
    EnumeratedIteration(arr)
# iteratingArrays();

# ----- Joing Array
def joiningArray():
    # Joining means putting contents ot two or more arrays in a single array
    # In SQL we join table based on a key, whereas in Numpy we join arrays by axes
    # We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If exis is not explicity passed, it is taken as 0
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    arrJoin = np.concatenate((arr1, arr2))
    # print(arrJoin)
    # Join two 2-D arrays along rows (axis = 1)
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    arrJoin = np.concatenate((arr1, arr2), axis = 1)
    print(arrJoin)
    # Join Arrays using stack function
    # Stacking is same as concatenation, the only difference is that stacking is done along a new axis
    arrJoin = np.stack((arr1, arr2), axis=0)
    print(arrJoin)
    arrJoin = np.stack((arr1, arr2), axis=1)
    print(arrJoin)
    arrJoin = np.stack((arr1, arr2), axis=-1)
    print(arrJoin)
    # Stacking Along Rows
    arrStack = np.hstack((arr1, arr2))
    print(arrStack)
    # Stacking Along Columns
    arrStack = np.vstack((arr1, arr2))
    print(arrStack)
    # Stacking Along Height
    arrStack = np.dstack((arr1, arr2))
    print(arrStack)
# joiningArray();

# ----- Array Split
def arraySplit():
    # Splitting is reverse operation of Joining
    # Joining merges multiple arrays into one and Splitting breaks one array into multiple
    arr = np.arange(12).reshape(-1)
    print(arr)
    newArr = np.array_split(arr, 3)
    print(newArr)
    # If the array has less elements than required, it will adjust from the end accordingly
    newArr = np.array_split(arr, 8) # There will be 2 elements and 3 elements array -> 2x + 3y = 12, x + y = 8 -> x = 4, y = 4
    print(newArr)
    # Split Into Arrays
    print(newArr[0], newArr[-1])

    # Split 2-D Arrays
    arr = np.arange(12).reshape(6, 2)
    print(arr)
    newArr = np.array_split(arr, 3)
    print(newArr, newArr[0].ndim)
    arr = np.arange(18).reshape(6, -1)
    print(arr)
    newArr = np.array_split(arr, 5)
    print(newArr)
    # In addition, you can specify which axis you want to do the split around
    newArr = np.array_split(arr, 2, axis=1)
    print(newArr)
    # Use the hsplit() method to split the 2-D array along rows
    newArr = np.hsplit(arr, 3)
    print(newArr)
# arraySplit();

# ---- Searching Arrays
def searchingArrays():
    # You can search an array for a certain value, and return the indexes that get a match
    # To search an array, use the where() method
    arr = np.array([1, 2, 3, 4, 5, 4, 4, 9])
    x = np.where(arr == 4)
    print(x, x[0]) # return a tuple: (array([3, 5, 6]),)
    # Find the indexes where the values are even
    x = np.where(arr%2 == 0)
    print(x)
    arr = arr.reshape(2, -1)
    print(arr)
    x = np.where(arr == 4)
    print(x) # return a tuple: (array([0, 1, 1]), array([3, 1, 2])) -> the first tuple represents the row and the second tuple represent the column
    # Search Sorted
    # There is a method called searchsorted() which performs a binary search in the array, 
    # and returns the index where the specified value would be inserted to maintain the search order
    arr = np.arange(10)
    print(arr)
    x = np.searchsorted(arr, 5)
    # The method starts the search from the left and returns the first index where the number 5 is no longer larger than the next value
    print(x)
    x = np.searchsorted(arr, 5, side='right')
    print(x)
    # Multiple Values
    arr = np.array([1, 3, 5, 7])
    x = np.searchsorted(arr, [2, 4, 6])
    print(x)
# searchingArrays();

# ----- Sorting Arrays
def sortingArrays():
    # Sorting means putting elements in a ordered sequence
    arr = np.array([3, 2, 0, 1])
    print(np.sort(arr))
    arr = arr.reshape(2, 2)
    print(np.sort(arr)) # Sort the most inner array
    # You can also sort arrays of strings, or any other data type
    arr = np.array(["Apple", "Cherry", "Banana"])
    print(np.sort(arr))
    arr = np.array([2, 0, 2])
    arr = arr.astype(bool)
    print(arr, arr.dtype, np.sort(arr))    
# sortingArrays();

# ---- Filter Array
def filterArray():
    # Filtering Arrays -> Getting some elements out of an existing array and creating a new array out of them is called filtering
    arr = np.array([41, 42, 43, 44])
    # In Numpy, you filter an array using a boolean index list
    booleanIndexList = [True, False, False, True]
    newArr = arr[booleanIndexList]
    print(newArr)
    # Creating the Filter Array
    # In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions
    def creatingFilter(array):
        filterArr = []
        for elem in array:
            if (elem < 43):
                filterArr.append(True)
            else:
                filterArr.append(False)
        return filterArr
    filter = creatingFilter(arr)
    print(filter, arr[filter])
    # Creating Filter Directly From Array
    filterArr = arr > 42
    print(filterArr, arr[filterArr])
    # Create a filter array that will return only even elements from the original array
    filterArr = arr % 2 == 0
    print(filterArr, arr[filterArr])
# filterArray();

# ----- Numpy Random
def numpyRandom():
    # Random Numbers in Numpy
    # What is a Random Number?
    # Random number does NOT mean a different nubmer every time. Random means something that can not be predicted logicallly

    # Pseudo Random and True Random
    # Computer work on programs, and programs are difinitive set of instructions. So it means there must be some algorithm to generate a random number as well
    # If there is a program to generate random number it can be predicted, thus it is not truly random
    # Random numbers generated through a generation algorithm are called pseudo random

    # --- Generate Random Number
    def randomNTime(n, upperbound):
        for x in range(n):
            ran = random.randint(upperbound)
            print(ran, end = " ")
    # randomNTime(3, upperbound=100)
    
    # --- Generate Random Float
    # returns a random float between 0 and 1
    def randomFloat(n):
        for x in range(n):
            ran = random.rand()
            print(ran, end = " ")
    # randomFloat(5)

    # --- Generate Random Array
    # Integers -> The randint() method takes a size parameter where you can specify the shape of an array
    randomArr = random.randint(100, size = (5, 5))
    print(randomArr)

    # Floats -> The rand() method also allows you to specify the shape of the array
    randomArr = random.rand(5, 5)
    print(randomArr)

    # --- Generate Random Number From Array
    # The choice() method allows you to generate a random value based on an array of values
    # The choice() method takes an array as a parameter and randomly returns one of the values
    x = random.choice([3, 5, 7, 8])
    print(x)
    # The choice() method also allows you to return an array of value
    x = random.choice(np.arange(20), size = (3, 3))
    print(x)
# numpyRandom();

# ---- Random Data Distribution
def randomDataDistribution():
    # What is Data Distribution?
    # Data distribution is a list of all possible values, and how often each value occurs
    # Such lists are important when working with statistics and data science

    # --- Random Distribution
    # A random distribution is a set of random numbers that follow a cetain probability density function
    x = random.choice([3, 5, 6, 7], p = [0.1, 0.3, 0.0, 0.6], size = (10, 10))
    print(x)
    searchArr = np.where(x == 7)
    print(searchArr, "\n", "The total number of 7 is", searchArr[0].shape[0])
# randomDataDistribution();

# ----- Random Permutations
def randomPermutations():
    # Random Permutations of Elements
    # A permutation refers to an arangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa
    
    # --- Shuffling Arrays
    arr = np.array([1, 2, 3, 4, 5])
    random.shuffle(arr)
    print(arr)
    # --- Generating Permutation of Arrays
    # The permutation() method returns a re-arranged array (and leaves the original array un-changed)
    newArr = random.permutation(arr)
    print(newArr, newArr.base, arr)
# randomPermutations();

# ----- Seaborn Module
def seabornModule():
    # Visualize Distributions With Seaborn
    # Seaborn is a library uses Matplotlib underneath to plot graphs. It will be used to visualize random distribution

    # Distplots
    # Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array
    sns.distplot([0, 1, 2, 3, 4, 5])
    plt.show()
    # plotting a Displot Without the Histogram
    sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
    plt.show()
# seabornModule();

# ----- Normal (Gaussian) Distribution
def normalDistribution():
    # The Normal Distribution is one of the most important distributions
    # It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
    # Use the random.normal() method to get a Normal Data Distribution

    # --- Generate a random normal distribution of size 2x100
    x = random.normal(size = (2, 100))
    print(x)
    x = x.reshape(-1)
    # sns.distplot(x)
    # plt.show()
    
    # --- Generate a random normal distribution of size 2x100 with mean at 100 and standard deviation of 2
    x = random.normal(loc = 100, scale = 2, size = (2, 100))
    sns.distplot(x)
    plt.show()
# normalDistribution();

# ----- Binomial Distribution
def binomialDistribution():
    # Binomial Distribution is a Discrete Distribution
    # It describes the outcome of binary scenarios, e.g. toss of coin, it will either be head or tails
    # It has three parameters:
    # 1. n - number of trials
    # 2. p - probability of occurence of each trial or success rate (e.g. for toss of a coin 0.5 each)
    # 3. size - The shape of the returned array
    x = random.binomial(n=100, p=0.5, size=100)
    # print(x)

    # Quesion1: Jessica meakes 60% of her free-throw attempts. If she shoots 6 free throws, what is the probability that she makes exactly 4?
    x = random.binomial(n=6, p=0.6, size=1000)
    # print(x)
    x = np.where(x == 4)
    print("The probability that she makes exactly 4 is {}".format(x[0].shape[0]/1000))

    # Visualization of Bionomial Distribution
    # sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
    # plt.show()

    # Difference Between Normal and Binomial Distribution
    # The main difference is that normal distribution is continuous whereas binomial is discrete, but if there are enough data points it will be quite similar to normal distribution with certain loc and scale
    sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
    sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
    plt.show()
    x = random.binomial(n=100, p=0.5, size=1000) # p is the success rate of event A, so the succes rate of  event B is 1-p which is equal to the failuer rate of event A
    x = np.where(x == 50)
    print("The probability that occurs exactly 50 occurences is {}".format(x[0].shape[0]/1000))
# binomialDistribution();

# ----- Poisson Distribution
def poissonDistribution():
    # Pisson Distribution is a Discrete Distribution
    # It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what  is probability he will eat  thrice?
    # It has two parameters
    # 1. lam - rate of known number of occurences e.g. 2 for above problem
    # 2. size - The shape of the returned array
    x = random.poisson(lam=2, size=1000)
    # print(x)
    # sns.distplot(x, hist=True, kde=False)
    # plt.show()

    # --- Difference Between Normal and Poisson Distribution
    # Normal distribution is continuous whereas poisson is discrete
    # But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean
    sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
    sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')
    plt.show()

    # --- Difference Between Poisson and Binomial Distribution
    # The difference is very subtle is that, binomial distribution is for discrete trials, whereas poisson distribution is for continuous trials
    # But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam
    x1 = random.binomial(n=1000, p=0.01, size=1000)
    x2 = random.poisson(lam=10, size=1000)
    sns.distplot(x1, hist=False, label='binomial')
    sns.distplot(x2, hist=False, label='poisson')
    plt.show()
# poissonDistribution();

# ----- Uniform Distribution
def uniformDistribution():
    # Use to describe probability where every event has equal chances of occuring
    # E.g. Generation of random numbers
    # It has three parameters
    # 1. a - lower bound - default 0.0
    # 2. b - upper bound - default 1.0
    # 3. size - The shape of the returned array
    x = random.uniform(1, 6, size=100000)
    sns.distplot(x, hist=False)
    plt.show()
# uniformDistribution();

# ----- Logistic Distribution
def logisticsDistribution():
    # Logistic Distribution is used to describe growth
    # Used extensively in machine learning in logistic regression, neural networks etc.
    # It has three parameters
    # 1. loc - mean, where the peak is. Default 0
    # 2. scale - standard deviation, the flatness of distribution. Default 1
    # 3. size - The shape of the returned array
    x = random.logistic(loc=1, scale=2, size=(2, 3))
    print(x)
    # sns.distplot(random.logistic(size=1000), hist=False)
    # plt.show()
    
    # Difference between logistics and normal distribution
    # Both distributions are near identical, but logistic distribution has more area under the tails. 
    # It representage more possibility of occurence of an events further away from mean
    sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
    sns.distplot(random.logistic(size=1000), hist=False, label='logistics')
    plt.show()
# logisticsDistribution();

# ----- Multinomial Distribution
def multinomialDistribution():
    # Multinomial distribution is a generalization of binomial distribution
    # It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two
    # It has three parameters
    # 1. n - number of possible outcomes (e.g. 6 for dice roll)
    # 2. pvals - list of probabilities of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll)
    # 3. size - The shape of the returned array
    x = random.multinomial(n=10, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size = 10)
    print(x)
    result = np.sum(x, axis=0)
    print(result)
# multinomialDistribution();

# ----- Exponential Distribution
def exponentialDistribution():
    # Exponential distribution is used for describing time till next event e.g. failure/success etc.
    # It has two parameters
    # 1. scale - inverse of rate (see lam in poisson distribution) defaults to 1.0
    # 2. size - The shape of the returned array

    # Example -> a man take a food twice a day (24 hours) -> a man take a food every 12 hours (lamda = 2/24 time/hour, scale = 24/2 hour/time)
    x = random.exponential(scale=0.5, size=100)
    sns.distplot(x)
    plt.show()

    # Relation Between Poisson and Exponential Distribution
    # Poisson distribution deals with number of occurences of an event in a time period whereas exponential distribution deals with the time between these events
# exponentialDistribution();

# ----- Chi Square Distribution
def chiSquareDistribution():
    # Chi Square distribution is used as a basis to verify the hypothesis
    # It has two parameters
    # 1. df - (degree of freedom)
    # 2. size - The shape of the returned array

    sns.distplot(random.chisquare(df=1, size=1000), hist=False, label='df=1')
    sns.distplot(random.chisquare(df=2, size=1000), hist=False, label='df=2')
    sns.distplot(random.chisquare(df=3, size=1000), hist=False, label='df=3')
    # plt.show()
# chiSquareDistribution();

# ----- Rayleigh Distribution
def rayleighDistribution():
    # Rayleigh distribution is used in signal processing
    # It has two parameters
    # 1. scale - (standard deviation) decides how flat the distribution will be (default 1.0)
    # 2. size - The shape of the returned array
    x = random.rayleigh(scale=2, size=(2, 3))
    print(x)
    sns.distplot(random.rayleigh(size=1000), hist=False)
    plt.show()
# rayleighDistribution();

# ----- Pareto Distribution
def paretoDistribution():
    # A distribution following Pareto's law i.e. 80-20 distribution(20% factors cause 80% outcome)
    # It has two parameters
    # 1. a - shape parameter
    # 2. size - The shape of the returned array

    x = random.pareto(a=2, size=(2, 3))
    print(x)
    sns.distplot(random.pareto(a=1000, size=100), kde=False)
    plt.show()
paretoDistribution();