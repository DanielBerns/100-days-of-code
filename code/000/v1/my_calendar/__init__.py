# If I execute 
#     python -m unittest test_01.py
# then this code fails to run 
# import .mycalendar
# import .calapp
# import .calfs
# import .locale_example
# import .formatyear
#
# With this traceback
# Traceback (most recent call last):
#   File "/usr/lib64/python3.8/runpy.py", line 194, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "/usr/lib64/python3.8/runpy.py", line 87, in _run_code
#     exec(code, run_globals)
#   File "/usr/lib64/python3.8/unittest/__main__.py", line 18, in <module>
#     main(module=None)
#   File "/usr/lib64/python3.8/unittest/main.py", line 100, in __init__
#     self.parseArgs(argv)
#   File "/usr/lib64/python3.8/unittest/main.py", line 147, in parseArgs
#     self.createTests()
#   File "/usr/lib64/python3.8/unittest/main.py", line 158, in createTests
#     self.test = self.testLoader.loadTestsFromNames(self.testNames,
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in loadTestsFromNames
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in <listcomp>
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
#   File "./100-days-of-code/code/000/v1/tests_with_unittest/test_01.py", line 1, in <module>
#     from context import my_calendar
#   File "./100-days-of-code/code/000/v1/tests_with_unittest/context.py", line 8, in <module>
#     import my_calendar
#   File "./100-days-of-code/code/000/v1/my_calendar/__init__.py", line 2
#     import .mycalendar
#            ^
# SyntaxError: invalid syntax

# If I execute
#    $ python -m unittest test_01.py
# this code runs, and the test fails to run properly  
# import my_calendar.mycalendar
# import my_calendar.calapp
# import my_calendar.calfs
# import my_calendar.locale_example
# import my_calendar.formatyear
#
# With this traceback
# Traceback (most recent call last):
#   File "/usr/lib64/python3.8/runpy.py", line 194, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "/usr/lib64/python3.8/runpy.py", line 87, in _run_code
#     exec(code, run_globals)
#   File "/usr/lib64/python3.8/unittest/__main__.py", line 18, in <module>
#     main(module=None)
#   File "/usr/lib64/python3.8/unittest/main.py", line 100, in __init__
#     self.parseArgs(argv)
#   File "/usr/lib64/python3.8/unittest/main.py", line 147, in parseArgs
#     self.createTests()
#   File "/usr/lib64/python3.8/unittest/main.py", line 158, in createTests
#     self.test = self.testLoader.loadTestsFromNames(self.testNames,
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in loadTestsFromNames
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in <listcomp>
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
#   File "./100-days-of-code/code/000/v1/tests_with_unittest/test_01.py", line 1, in <module>
#     from context import my_calendar
#   File "./100-days-of-code/code/000/v1/tests_with_unittest/context.py", line 8, in <module>
#     import my_calendar
#   File "./100-days-of-code/code/000/v1/my_calendar/__init__.py", line 17, in <module>
#     import my_calendar.calfs
#   File "./100-days-of-code/code/000/v1/my_calendar/calfs.py", line 40, in <module>
#     year = int(sys.argv[1])
# ValueError: invalid literal for int() with base 10: 'test_01.py'

# If I execute
# $ python -m unittest test_01.py
# this code runs, and the test fails to run properly  
from .mycalendar import *
from .calapp import *
from .calfs import *
from .locale_example import *
from .formatyear import *
# With this traceback
# Traceback (most recent call last):
#   File "/usr/lib64/python3.8/runpy.py", line 194, in _run_module_as_main
#     return _run_code(code, main_globals, None,
#   File "/usr/lib64/python3.8/runpy.py", line 87, in _run_code
#     exec(code, run_globals)
#   File "/usr/lib64/python3.8/unittest/__main__.py", line 18, in <module>
#     main(module=None)
#   File "/usr/lib64/python3.8/unittest/main.py", line 100, in __init__
#     self.parseArgs(argv)
#   File "/usr/lib64/python3.8/unittest/main.py", line 147, in parseArgs
#     self.createTests()
#   File "/usr/lib64/python3.8/unittest/main.py", line 158, in createTests
#     self.test = self.testLoader.loadTestsFromNames(self.testNames,
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in loadTestsFromNames
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 220, in <listcomp>
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "/usr/lib64/python3.8/unittest/loader.py", line 154, in loadTestsFromName
#     module = __import__(module_name)
#   File "/home/dberns/Code/github/DanielBerns/100-days-of-code/code/000/v1/tests_with_unittest/test_01.py", line 1, in <module>
#     from context import my_calendar
#   File "/home/dberns/Code/github/DanielBerns/100-days-of-code/code/000/v1/tests_with_unittest/context.py", line 8, in <module>
#     import my_calendar
#   File "/home/dberns/Code/github/DanielBerns/100-days-of-code/code/000/v1/my_calendar/__init__.py", line 76, in <module>
#     from .calfs import *
#   File "/home/dberns/Code/github/DanielBerns/100-days-of-code/code/000/v1/my_calendar/calfs.py", line 8, in <module>
#     year = int(sys.argv[1])
# ValueError: invalid literal for int() with base 10: 'test_01.py'

# If I execute
# $ python -m unittest test_01.py 2022
# then I get
# What year?
# So the test fails to run properly
# So, ***Go to ../v2***
