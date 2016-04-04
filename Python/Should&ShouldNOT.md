Source: 
* http://safehammad.com/downloads/python-idioms-2014-01-16.pdf
* http://images.immobilien.de/expose/00/04/04/36/0004043615/etc248188603/writing_idiomatic_python_3.pdf
* 
* [Writing Idiomatic Python Video Two -Jeff Knupp](https://www.youtube.com/watch?v=wym71aDDMyo)
* [Zero to Hero with Python](https://www.youtube.com/watch?v=9uq3w6JJS00)
* [Python performance](https://www.youtube.com/watch?v=7eeEf_rAJds) 


1. Enumerate
------
 
* **Don't Write This:**
```python 
my_container = ['Larry', 'Moe', 'Curly']
index = 0
for element in my_container:
    print ('{} {}'.format(index, element))
    index += 1
```
* **Write This:**
```python
my_container = ['Larry', 'Moe', 'Curly']
for index, element in enumerate(my_container):
    print ('{} {}'.format(index, element))
```
2. Test for *`True`* and *`False`* values
------
* **Don't Write This:**
```python
if name != '' and len(pets) > 0 and owners != {}:
    print('We have pets!')

```
* **Write This:**
```python
 name = 'Safe'
 pets = ['Dog', 'Cat', 'Hamster']
 owners = {'Safe': 'Cat', 'George': 'Dog'}
 if name and pets and owners:
    print('We have pets!')
```
3. Use `in` where possible
------
* **Don't Write This:**
```python
 name = 'Safe Hammad'
 if name.find('H') != -1:
    print('This name has an H in it!')
```
* **Write This:**
```python
 name = 'Safe Hammad'
 if 'H' in name:
    print('This name has an H in it!')
```
4. Use `in` where possible
------
* **Don't Write This:**
```python
 pets = ['Dog', 'Cat', 'Hamster']
 i = 0
 while i < len(pets):
    print('A', pets[i], 'can be very cute!')
    i += 1
```
* **Write This:**
```python
 pets = ['Dog', 'Cat', 'Hamster']
 for pet in pets:
    print('A', pet, 'can be very cute!')
```
5. Swap values without `temp` variable
------
* **Don't Write This:**
```python
 a, b = 5, 6
 print(a, b) # 5, 6

 temp = a
 a = b
 b = temp
 print(a, b) # 6, 5

```
* **Write This:**
```python
 a, b = 5, 6
 print(a, b) # 5, 6
 a, b = b, a
 print(a, b) # 6, 5

```
6. Build strings using sequence
------
* **Don't Write This:**
```python
 chars = ['S', 'a', 'f', 'e']
 name = ''
 for char in chars:
    name += char
    print(name) # Safe

```
* **Write This:**
```python
 chars = ['S', 'a', 'f', 'e']
 name = ''.join(chars)
 print(name) # Safe

```
7. `Try...exception` is better than check for specific type
------
* **Don't Write This:**
```python
 d = {'x': '5'}
 if 'x' in d and isinstance(d['x'], str) and \
 d['x'].isdigit():
    value = int(d['x'])
 else:
    value = None
```
* **Write This:**
```python
 d = {'x': '5'}
 try:
    value = int(d['x'])
 except (KeyError, TypeError, ValueError):
    value = None
```
8. Build lists using list comprehensions (except the second form can be clearer)
------
* **Don't Write This:**
```python
 data = [7, 20, 3, 15, 11]
 result = []
 for i in data:
    if i > 10:
        result.append(i * 3)
 print(result) # [60, 45, 33]

```
* **Write This:**
```python
 data = [7, 20, 3, 15, 11]
 result = [i * 3 for i in data if i > 10]
 print(result) # [60, 45, 33]

```
9. Create dict from keys and values using `zip`
------
* **Don't Write This:**
```python
 keys = ['Safe', 'Bob', 'Thomas']
 values = ['Hammad', 'Builder', 'Engine']
 d = {}
 for i, key in enumerate(keys):
    d[keys] = values[i]
 print(d) # {'Bob': 'Builder',
            'Safe': 'Hammad',
            'Thomas': 'Engine'}
```
* **Write This:**
```python
 keys = ['Safe', 'Bob', 'Thomas']
 values = ['Hammad', 'Builder', 'Engine']
 d = dict(zip(keys, values))
 print(d) # {'Bob': 'Builder',
            'Safe': 'Hammad',
            'Thomas': 'Engine'}
```
10. Avoid repeating variable `name` in compound `if` statement
------
* **Don't Write This:**
```python
is_generic_name = False
name = 'Tom'
if name == 'Tom' or name == 'Dick' or name == 'Harry':
    is_generic_name = True
```
* **Write This:**
```python
name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
```
11. Use `else` to execute code after a `for` loop concludes
------
* **Don't Write This:**
```python
for user in get_all_users():
    has_malformed_email_address = False
    print ('Checking {}'.format(user))
    for email_address in user.get_all_email_addresses():
        if email_is_malformed(email_address):
            has_malformed_email_address = True
            print ('Has a malformed email address!')
            break
    if not has_malformed_email_address:
        print ('All email addresses are valid!')

```
* **Write This:**
```python
for user in get_all_users():
    print ('Checking {}'.format(user))
    for email_address in user.get_all_email_addresses():
        if email_is_malformed(email_address):
            print ('Has a malformed email address!')
            break
    else:
        print ('All email addresses are valid!')
```

13. Use `*args` and `**kwargs` to accept arbitrary arguments
--------------------
* **Don't Write This:**
```python
def make_api_call(foo, bar, baz):
	if baz in ('Unicorn', 'Oven', 'New York'):
		return foo(bar)
	else:
		return bar(foo)
# I need to add another parameter to `make_api_call`
# without breaking everyone's existing code.
# I have two options...
def so_many_options():
 # I can tack on new parameters, but only if I make
 # all of them optional...
def make_api_call(foo, bar, baz, qux=None, foo_polarity=None,
                 baz_coefficient=None, quux_capacitor=None,
                 bar_has_hopped=None, true=None, false=None,
                 file_not_found=None):
	# ... and so on ad infinitum
 	return file_not_found
def version_graveyard():
# ... or I can create a new function each time the signature
# changes.
	def make_api_call_v2(foo, bar, baz, qux):
		return make_api_call(foo, bar, baz) - qux
	def make_api_call_v3(foo, bar, baz, qux, foo_polarity):
		if foo_polarity != 'reversed':
			return make_api_call_v2(foo, bar, baz, qux)
		return None
	def make_api_call_v4(foo, bar, baz, qux, foo_polarity, baz_coefficient):
		return make_api_call_v3(foo, bar, baz, qux, foo_polarity) * baz_coefficient
	def make_api_call_v5(foo, bar, baz, qux, foo_polarity, baz_coefficient, quux_capacitor):
		# I don't need 'foo', 'bar', or 'baz' anymore, but I have to
		# keep supporting them...
		return baz_coefficient * quux_capacitor
```
* **Write This:**
```python
def make_api_call(foo, bar, baz):
	if baz in ('Unicorn', 'Oven', 'New York'):
		return foo(bar)
	else:
		return bar(foo)
# I need to add another parameter to `make_api_call`
# without breaking everyone's existing code.
# Easy...
def new_hotness():
	def make_api_call(foo, bar, baz, *args, **kwargs):
		# Now I can accept any type and number of arguments
		# without worrying about breaking existing code.
		baz_coefficient = kwargs['the_baz']
		# I can even forward my args to a different function without
		# knowing their contents!
		return baz_coefficient in new_function(args)
```
14. Use the `*` operator to represent the “rest, middle, head” of a list
--------------------
* **Don't Write This:**
```python
some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, rest) = some_list[0], some_list[1], some_list[2:]
print(rest)
(first, middle, last) = some_list[0], some_list[1:-1], some_list[-1]
print(middle)
(head, penultimate, last) = some_list[:-2], some_list[-2], some_list[-1]
print(head)

```
* **Write This:**
```python
some_list = ['a', 'b', 'c', 'd', 'e']
(first, second, *rest) = some_list
print(rest)
(first, *middle, last) = some_list
print(middle)
(*head, penultimate, last) = some_list
print(head)
```
15. `dict.get` to provide default values
--------------------
* **Don't Write This:**
```python
log_severity = None
if 'severity' in configuration:
	log_severity = configuration['severity']
else:
	log_severity = 'Info'

```
* **Write This:**
```python
log_severity = configuration.get('severity', 'Info')
```
16. Use a `dict comprehension` to build a `dict` clearly and efficiently
--------------------
* **Don't Write This:**
```python
user_email = {}
for user in users_list:
	if user.email:
		user_email[user.name] = user.email

```
* **Write This:**
```python
user_email = {user.name: user.email for user in users_list if user.email}	
```
17. Prefer the `format` function for formatting strings
--------------------
* **Don't Write This:**
```python
def get_formatted_user_info_worst(user):
	# Tedious to type and prone to conversion errors
	return 'Name: ' + user.name + ', Age: ' + str(user.age) + ', Sex: ' + user.sex
def get_formatted_user_info_slightly_better(user):
	# No visible connection between the format string placeholders
	# and values to use. Also, why do I have to know the type?
	# Don't these types all have __str__ functions?
	return 'Name: %s, Age: %i, Sex: %c' % (user.name, user.age, user.sex)

```
* **Write This:**
```python
def get_formatted_user_info(user):
# Clear and concise. At a glance I can tell exactly what
# the output should be. Note: this string could be returned
# directly, but the string itself is too long to fit on the
# page.
	output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format(user=user)
	return output
```
18. Chain `string` functions to make a simple series of transformations more clear
--------------------
* **Don't Write This:**
```python
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip()
formatted_book_info = formatted_book_info.upper()
formatted_book_info = formatted_book_info.replace(':', ' by')

```
* **Write This:**
```python
book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')
```
19. Define `__str__` in a class to show a human-readable representation
--------------------
* **Don't Write This:**
```python
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
p = Point(1, 2)
print (p)
# Prints '<__main__.Point object at 0x91ebd0>'
```
* **Write This:**
```python
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return '{0}, {1}'.format(self.x, self.y)
p = Point(1, 2)
print (p)
# Prints '1, 2'
```
20. Use `sets` to eliminate duplicate entries from `Iterable` containers
--------------------
* **Don't Write This:**
```python
unique_surnames = []
for surname in employee_surnames:
	if surname not in unique_surnames:
		unique_surnames.append(surname)
def display(elements, output_format='html'):
	if output_format == 'std_out':
		for element in elements:
			print(element)
	elif output_format == 'html':
		as_html = '<ul>'
		for element in elements:
			as_html += '<li>{}</li>'.format(element)
		return as_html + '</ul>'
	else:
		raise RuntimeError('Unknown format {}'.format(output_format))
```
* **Write This:**
```python
unique_surnames = set(employee_surnames)
def display(elements, output_format='html'):
	if output_format == 'std_out':
		for element in elements:
			print(element)
	elif output_format == 'html':
		as_html = '<ul>'
		for element in elements:
			as_html += '<li>{}</li>'.format(element)
		return as_html + '</ul>'
	else:
		raise RuntimeError('Unknown format {}'.format(output_format))
```
21. Use a `set comprehension` to generate sets concisely
--------------------
* **Don't Write This:**
```python
users_first_names = set()
for user in users:
	users_first_names.add(user.first_name)

```
* **Write This:**
```python
users_first_names = {user.first_name for user in users}
```
22. Understand and use the mathematical `set` operations
--------------------
* **Union** The set of elements in A, B, or both A and B (written A | B in Python).
* **Intersection** The set of elements in both A and B (written A & B in Python).
* **Difference* The set of elements in A but not B (written A - B in Python).
	* Note: order matters here. A - B is not necessarily the same as B - A.
* **Symmetric Difference** The set of elements in either A or B, but not both A and B (written A ˆ B in Python).

* **Don't Write This:**
```python
def get_both_popular_and_active_users():
	# Assume the following two functions each return a
	# list of user names
	most_popular_users = get_list_of_most_popular_users()
	most_active_users = get_list_of_most_active_users()
	popular_and_active_users = []
	for user in most_active_users:
		if user in most_popular_users:
			popular_and_active_users.append(user)
	return popular_and_active_users
```
* **Write This:**
```python
def get_both_popular_and_active_users():
	# Assume the following two functions each return a
	# list of user names
	return(set(get_list_of_most_active_users()) & set(get_list_of_most_popular_users()))
```
23. Use a `generator` to lazily load infinite sequences
--------------------
* **Don't Write This:**
```python
def get_twitter_stream_for_keyword(keyword):
	"""Get's the 'live stream', but only at the moment the function is initially called. To get more entries,
	the client code needs to keep calling 'get_twitter_livestream_for_user'. Not ideal.
	"""
	imaginary_twitter_api = ImaginaryTwitterAPI()
	if imaginary_twitter_api.can_get_stream_data(keyword):
		return imaginary_twitter_api.get_stream(keyword)
	current_stream = get_twitter_stream_for_keyword('#jeffknupp')
	for tweet in current_stream:
		process_tweet(tweet)
# Uh, I want to keep showing tweets until the program is quit.
# What do I do now? Just keep calling
# get_twitter_stream_for_keyword? That seems stupid.
def get_list_of_incredibly_complex_calculation_results(data):
	return [first_incredibly_long_calculation(data),
	second_incredibly_long_calculation(data),
	third_incredibly_long_calculation(data),
	]

```
* **Write This:**
```python
def get_twitter_stream_for_keyword(keyword):
	"""Now, 'get_twitter_stream_for_keyword' is a generator and will continue to generate Iterable pieces of data
	one at a time until 'can_get_stream_data(user)' is False (which may be never).
	"""
	imaginary_twitter_api = ImaginaryTwitterAPI()
	while imaginary_twitter_api.can_get_stream_data(keyword):
		yield imaginary_twitter_api.get_stream(keyword)
# Because it's a generator, I can sit in this loop until
# the client wants to break out
for tweet in get_twitter_stream_for_keyword('#jeffknupp'):
	if got_stop_signal:
		break
	process_tweet(tweet)
def get_list_of_incredibly_complex_calculation_results(data):
	"""A simple example to be sure, but now when the client code iterates over the call to 'get_list_of_incredibly_complex_calculation_results', we only do as much work as necessary to generate the
	current item.
	"""
	yield first_incredibly_long_calculation(data)
	yield second_incredibly_long_calculation(data)
	yield third_incredibly_long_calculation(data)
```
24. Prefer a `generator` expression to a `list comprehension` for simple `iteration`
--------------------
* **Don't Write This:**
```python
for uppercase_name in [name.upper() for name in get_all_usernames()]:
	process_normalized_username(uppercase_name)
```
* **Write This:**
```python
for uppercase_name in (name.upper() for name in get_all_usernames()):
	process_normalized_username(uppercase_name)
```
25. Use a `context manager` to ensure resources are properly managed
--------------------
* **Don't Write This:**
```python
file_handle = open(path_to_file, 'r')
for line in file_handle.readlines():
	if raise_exception(line):
		print('No! An Exception!')

```
* **Write This:**
```python
with open(path_to_file, 'r') as file_handle:
	for line in file_handle:
		if raise_exception(line):
			print('No! An Exception!')
```

26. Use `tuples` to unpack data
--------------------
* **Don't Write This:**
```python
list_from_comma_separated_value_file = ['dog', 'Fido', 10]
animal = list_from_comma_separated_value_file[0]
name = list_from_comma_separated_value_file[1]
age = list_from_comma_separated_value_file[2]
output = ('{name} the {animal} is {age} years old'.format(
animal=animal, name=name, age=age))
```
* **Write This:**
```python
list_from_comma_separated_value_file = ['dog', 'Fido', 10]
(animal, name, age) = list_from_comma_separated_value_file
output = ('{name} the {animal} is {age} years old'.format(
animal=animal, name=name, age=age))
```
27. Use `_` as a placeholder for data in a tuple that should be ignored
--------------------
* **Don't Write This:**
```python
(name, age, temp, temp2) = get_user_info(user)
if age > 21:
	output = '{name} can drink!'.format(name=name)
# "Wait, where are temp and temp2 being used?"

```
* **Write This:**
```python
(name, age, _, _) = get_user_info(user)
if age > 21:
	output = '{name} can drink!'.format(name=name)
# "Clearly, only name and age are interesting"
```

28. Use all `capital letters` when declaring `global constant` values
--------------------
* **Don't Write This:**
```python
seconds_in_a_day = 60 * 60 * 24
# ...
def display_uptime(uptime_in_seconds):
	percentage_run_time = (uptime_in_seconds/seconds_in_a_day) * 100
	# "Huh!? Where did seconds_in_a_day come from?"
	return 'The process was up {percent} percent of the day'.format(percent=int(percentage_run_time))
# ...
uptime_in_seconds = 60 * 60 * 24
display_uptime(uptime_in_seconds)

```
* **Write This:**
```python
SECONDS_IN_A_DAY = 60 * 60 * 24
# ...
def display_uptime(uptime_in_seconds):
	percentage_run_time = (uptime_in_seconds/SECONDS_IN_A_DAY) * 100
	# "Clearly SECONDS_IN_A_DAY is a constant defined
	# elsewhere in this module."
	return 'The process was up {percent} percent of the day'.format(percent=int(percentage_run_time))
# ...
uptime_in_seconds = 60 * 60 * 24
display_uptime(uptime_in_seconds)
```
29. Avoid placing multiple statements on a single line
--------------------
* **Don't Write This:**
```python
if this_is_bad_code: rewrite_code(); make_it_more_readable();
```
* **Write This:**
```python
if this_is_bad_code:
	rewrite_code()
	make_it_more_readable()
```
30. Use `sys.exit` in your script to return proper error codes
--------------------
* **Don't Write This:**
```python
do_stuff_with_result(result)
	# Optional, since the return value without this return
	# statment would default to None, which sys.exit treats
	# as 'exit with 0'
	return 0
if __name__ == '__main__':
	import sys
	# What happens if no argument is passed on the
	# command line?
	if len(sys.argv) > 1:
		argument = sys.argv[1]
		result = do_stuff(argument)
	# Again, what if this is False? How would other programs know?
	if result:
		do_stuff_with_result(result)

```
* **Write This:**
```python
def main():
	import sys
	if len(sys.argv) < 2:
		# Calling sys.exit with a string automatically
		# prints the string to stderr and exits with
		# a value of '1' (error)
		sys.exit('You forgot to pass an argument')
		argument = sys.argv[1]
		result = do_stuff(argument)
	if not result:
		sys.exit(1)
	# We can also exit with just the return code

# The three lines below are the canonical script entry
# point lines. You'll see them often in other Python scripts
if __name__ == '__main__':
	sys.exit(main())
```
31. Use the `if __name__ == '__main__'` pattern to allow a file to be both imported and run directly
--------------------
* **Don't Write This:**
```python
import sys
import os
FIRST_NUMBER = float(sys.argv[1])
SECOND_NUMBER = float(sys.argv[2])
def divide(a, b):
	return a/b
# I can't import this file (for the super
# useful 'divide' function) without the following
# code being executed.
if SECOND_NUMBER != 0:
	print(divide(FIRST_NUMBER, SECOND_NUMBER))

```
* **Write This:**
```python
import sys
import os
def divide(a, b):
	return a/b
# Will only run if script is executed directly,
# not when the file is imported as a module
if __name__ == '__main__':
	first_number = float(sys.argv[1])
	second_number = float(sys.argv[2])
	if second_number != 0:
		print(divide(first_number, second_number))
```
32. Prefer `absolute imports` to `relative imports`
--------------------
* **Don't Write This:**
```python
# My location is package.sub_package.module
# and I want to import package.other_module.
# The following should be avoided:
from ...package import other_module

```
* **Write This:**
```python
# My location is package.sub_package.another_sub_package.module
# and I want to import package.other_module.
# Either of the following are acceptable:
import package.other_module
import package.other_module as other
```
33. Do not use `from foo import *` to import the contents of a module.
--------------------
* **Don't Write This:**
```python
from foo import *

```
* **Write This:**
```python
from foo import (bar, baz, qux, quux, quuux)
# or even better...
import foo
```
34. Arrange your `import` statements in a standard order
--------------------
* **Don't Write This:**
```python
import os.path
# Some function and class definitions,
# one of which uses os.path
# ....
import concurrent.futures
from flask import render_template
# Stuff using futures and Flask's render_template
# ....
from flask import (Flask, request, session, g,
redirect, url_for, abort,
render_template, flash, _app_ctx_stack)
import requests
# Code using flask and requests
# ....
if __name__ == '__main__':
	# Imports when imported as a module are not so
	# costly that they need to be relegated to inside
	# an 'if __name__ == '__main__'' block...
	import this_project.utilities.sentient_network as skynet
	import this_project.widgets
	import sys
```
* **Write This:**
```python
import concurrent.futures
import os.path
import sys
from flask import (Flask, request, session, g,
redirect, url_for, abort,
render_template, flash, _app_ctx_stack)
import requests
import this_project.utilities.sentient_network as skynet
import this_project.widgets
```
35. Use functions in the os.path module when working with directory paths
--------------------
* **Don't Write This:**
```python
from datetime import date
import os
filename_to_archive = 'test.txt'
new_filename = 'test.bak'
target_directory = './archives'
today = date.today()
os.mkdir('./archives/' + str(today))
os.rename(filename_to_archive, target_directory + '/' + str(today) + '/' + new_filename, today + '/' + new_filename)

```
* **Write This:**
```python
from datetime import date
import os
current_directory = os.getcwd()
filename_to_archive = 'test.txt'
new_filename = os.path.splitext(filename_to_archive)[0] + '.bak'
target_directory = os.path.join(current_directory, 'archives')
today = date.today()
new_path = os.path.join(target_directory, str(today))
if (os.path.isdir(target_directory)):
	if not os.path.exists(new_path):
		os.mkdir(new_path)
		os.rename(os.path.join(current_directory, filename_to_archive), os.path.join(new_path, new_filename))
```

36. 
------
* **Write This:**
```python
 while True:
  break # This will spark discussion!!!
```  
* Generators and generator expressions.
* Avoid from module import *
 Prefer: import numpy as np; import pandas as pd
* Use _ for “throwaway” variables e.g.:
for k, _ in [('a', 1), ('b', 2), ('c', 3)]
* dict.get() and dict.setdefault()
* collections.defaultdict
* Sort lists using l.sort(key=key_func)
* Avoid comparing directly to True, False, or None 

Identifier| Type | Format Example
---------- | ----- | ---------------
Class | Camel case | class StringManipulator():
Variable | Words joined by _ | joined_by_underscore = True
Function | Words joined by _ | def multi_word_name(words):
Constant | All uppercase | SECRET_KEY = 42






