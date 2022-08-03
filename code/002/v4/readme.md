# What is this?

In the directory [../v1](../v1), I found some troubles writing tests, because the python code I wrote are scripts, not modules. Here, I found what parts of the code are truly testables. So, I realize how to modify my old code. Now, the module [./v3/my_calendar/mycalendar.py](./v3/my_calendar/mycalendar.py), is testable: I can write tests that runs, succeding or failing.

## What I want

First, I want to test the code, following ArjanCodes video [How To Write Unit Tests For Existing Python Code // Part 1 of 2](https://www.youtube.com/watch?v=ULxMQ57engo).

Note that ArjanCodes uses [pytest](https://docs.pytest.org/en/7.1.x/). 

## What I do

### Fourth attempt to develop some tests

Today, I used unittest and pytest.
Note that the tests don't contain assertions so far.
I found a weird issue with pathlib.Path.expanduser()
This works

    p = Path('~).expanduser()
    
but this fails

    p = Path('~', 'Data').expanduser()
