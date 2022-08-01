# What is this?

In the directory [../v1](../v1), I found some troubles developing some tests. Here, I found what parts of the code are truly testables. So, I realize how to modify my old code.

## Code presentation (repeated)
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

### Second attempt to develop some tests

I modify [````__init__.py````](./my_calendar/__init__.py)

    from .calapp import (build_filesystem, 
                         generate_year)
    from .mycalendar import CustomHTMLCalendar
    
Then, I go to the command line into the tests_with_unittest directory, execute python, and write the following

    >>> from context import my_calendar
    >>> dir(my_calendar)
    
Now, I get this

    ['CustomHTMLCalendar', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', \
     '__name__', '__package__', '__path__', '__spec__', 'build_filesystem', 'calapp', \
     'generate_year', 'mycalendar']

Them I write [tests_with_unittest/test_01.py]

