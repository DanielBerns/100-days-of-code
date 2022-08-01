# What is this?

## Code presentation
Some time ago, I have read [this article about the calendar module in PyMOTW](https://pymotw.com/3/calendar/) and its [python docs](https://docs.python.org/3.8/library/calendar.html). Then I copied some snippets, and wrote some scripts you can found [here](./my_calendar), without any tests. Moreover, I made some quick and dirty hacks. For example, in the [script](./my_calendar/mycalendar.py)

I used this snippet for reading one parameter from the command line
    
    ...
    try:                             # Line 16
        year = int(sys.argv[-1])     # Line 17
    except ValueError:               # Line 18
        year = 2020                  # Line 19
    ...
    
Output files are generated in the same directory of the code.

    ...
    with open(f'calendar-{year:d}.html', 'w') as target:    # Line 23
        ...
        
The structure of the HTML output is embedded in the code

    target.write('<html>')                                       # Line 24
    target.write('<head>')                                       # Line 25
    target.write('<link rel="stylesheet" href="calendar.css">')  # Line 26
    target.write('</head>')                                      # Line 27
    target.write('<body>')                                       # Line 28
    target.write(c.formatyear(year))                             # Line 29
    target.write('</body>')                                      # Line 30
    target.write('</html>')                                      # Line 31


## What I want

First, I want to test the code, following ArjanCodes video [How To Write Unit Tests For Existing Python Code // Part 1 of 2](https://www.youtube.com/watch?v=ULxMQ57engo).

Note that ArjanCodes uses [pytest](https://docs.pytest.org/en/7.1.x/). Today, I am going to use [unittest](https://docs.python.org/3.8/library/unittest.html) and [pytest](https://docs.pytest.org/en/7.1.x/).

## What I do

### First attempt

Now, I am going to follow [docs.python-guide.org/writing/structure/](https://docs.python-guide.org/writing/structure/).
The first step is to add [````__init__.py````](./my_calendar/__init__.py) file in the directory [my_calendar](./my_calendar) because we need that to transform that bunch of scripts into a python package. Doing so, we can write the tests in separate directories [test_with_unittest](./tests_with_unittest) and [test_with_pyttest](./tests_with_pytest).


Now, I write some code in [````./my_calender/__init__.py````](./my_calender/__init__.py)
    
    import .mycalendar
    import .calapp
    import .calfs
    import .locale_example
    import .formatyear
    
Next, I go to the directory [tests_with_unittest/](./tests test_with_unittest). 
Include an empty file named [````__init__.py````](./tests test_with_unittest/__init__.py) and the [very important file context.py, imho](./tests_with_unittest/context.py).

Then, I go to the command line into the tests_with_unittest directory, execute python, and write the following

    >>> from context import my_calendar
    >>> dir(my_calendar)
    
I get this

    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
    
Nothing to call, nothing to instantiate :-(, because these scripts in my_calendar directory are demos, not to be fully tested.


***Please, go to [../v2/](../v2/).***
