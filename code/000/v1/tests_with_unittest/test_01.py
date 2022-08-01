from context import my_calendar

# This is the first attempt
# There is no tests here, because there is nothing to test

dir(my_calendar)

# We have access to some things (paths)
# However, we want other things (callables and classes)
loader = my_calendar.__loader__
for l in loader.contents():
    print(str(l))
    
