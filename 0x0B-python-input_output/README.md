# Python - Input/Output

In this project, I practiced file handling in Python. I used the builtin `with`,
`open`, and `read` functions with the `json` module to read and write files and
serialize and deserialize objects with JSON.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `7-add_item.py` | `` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `9-student.py` | `def __init__(self, first_name, last_name, age):` |
| `10-student.py` | `def __init__(self, first_name, last_name, age):` |
| `11-student.py` | `` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |
| `101-stats.py` | `` |


## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text
  file to standard output.

* **1. Number of lines**
  * [1-write_file.py](./1-write_file.py):Write a function that writes a string to a text file `(UTF8)` and returns the number of characters written:

  Prototype: `def write_file(filename="", text=""):`
  You must use the with statement
  You don’t need to manage file permission exceptions.
  Your function should create the file if doesn’t exist.
  Your function should overwrite the content of the file if it already exists.
  You are not allowed to import any module

* **2. Read n lines**
  * [2-append_write.py](./2-append_write.py): Write a function that appends a string at the end of a text file `(UTF8)` and returns the number of characters    added:

  Prototype: `def append_write(filename="", text=""):`
  If the file doesn’t exist, it should be created
  You must use the with statement
  You don’t need to manage file permission or file doesn't exist exceptions.
  You are not allowed to import any module

* **3. Write to a file**
  * [3-to_json_string.py](./3-to_json_string.py): Write a function that returns the JSON representation of an object (string):

  Prototype: `def to_json_string(my_obj):`
  You don’t need to manage exceptions if the object can’t be serialized.

* **4. Append to a file**
  * [4-from_json_string.py](./4-from_json_string.py): Write a function that returns an object (Python data structure) represented by a JSON string:

  Prototype: `def from_json_string(my_str):`
  You don’t need to manage exceptions if the JSON string doesn’t represent an object.

* **5. To JSON string**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Write a function that writes an Object to a text file, using a JSON representation:

  Prototype: `def save_to_json_file(my_obj, filename):`
  You must use the with statement
  You don’t need to manage exceptions if the object can’t be serialized.
  You don’t need to manage file permission exceptions.
  
* **6. From JSON string to Object**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): Write a function that creates an Object from a “JSON file”:

  Prototype: `def load_from_json_file(filename):`
  You must use the with statement
  You don’t need to manage exceptions if the JSON string doesn’t represent an object.
  You don’t need to manage file permissions / exceptions.
  
* **7. Save Object to a file**
  * [7-add_item.py](./7-add_item.py): Write a script that adds all arguments to a Python list, and then save them to a file:

 You must use your function `save_to_json_file` from `5-save_to_json_file.py`
 You must use your function `load_from_json_file` from `6-load_from_json_file.py`
 The list must be saved as a JSON representation in a file named add_item.json
 If the file doesn’t exist, it should be created
 You don’t need to manage file permissions / exceptions.

* **8. Create object from a JSON file**
  * [8-class_to_json.py](./8-class_to_json.py): Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

  Prototype: `def class_to_json(obj):`
  obj is an instance of a Class
  All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
  You are not allowed to import any module

* **9. Load, add, save**
  * [9-student.py](./9-student.py): Write a class Student that defines a student by:

  Public instance attributes:
  `first_name`
  `last_name`
  `age`
  Instantiation with `first_name`, `ast_name` and `age:` `def __init__(self, first_name, last_name, age):`
  Public method `def to_json(self):` that retrieves a dictionary representation of a Student instance `(same as 8-class_to_json.py)`
  You are not allowed to import any module

* **10. Class to JSON**
  * [10-student.py](./10-student.py): Write a class Student that defines a student by: (based on 9-student.py)

   Public instance attributes:
   `first_name`
   `last_name`
   `age`
   Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
   Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance `(same as 8-class_to_json.py):`
   If attrs is a list of strings, only attribute names contained in this list must be retrieved.
   Otherwise, all attributes must be retrieved
   You are not allowed to import any module

* **11. Student to JSON**
  * [11-student.py](./11-student.py): Write a class Student that defines a student by: (based on 10-student.py)

   Public instance attributes:
   `first_name
   last_name
   age`
   Instantiation with `first_name, last_name and age: def __init__(self, first_name, last_name, age):`
   Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
   If attrs is a list of strings, only attributes name contain in this list must be retrieved.
   Otherwise, all attributes must be retrieved
   Public method `def reload_from_json(self, json):` that replaces all attributes of the Student instance:
   You can assume json will always be a dictionary
   A dictionary key will be the public attribute name
   A dictionary value will be the value of the public attribute
   You are not allowed to import any module

* **12. Student to JSON with filter**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): Technical interview preparation:

   You are not allowed to google anything
   Whiteboard first
   Create a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:
   
   Returns an empty list if `n <= 0`
   You can assume` n `will be always an integer
   You are not allowed to import any module
  
* **13. Student to disk and reload**
  * [100-append_after.py](./100-append_after.py): Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

  Prototype: `def append_after(filename=""`, `search_string=""`, `new_string=""):`
  You must use the with statement
  You don’t need to manage file permission or file doesn't exist exceptions.
  You are not allowed to import any module

* **14. Pascal's Triangle**
  * [101-stats.py](./101-stats.py): Write a script that reads stdin line by line and computes metrics:

   Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
   Each 10 lines and after a keyboard interruption `(CTRL + C),` prints those statistics since the beginning:
   Total file size: File size: `<total size>`
   where is the sum of all previous (see input format above)
   Number of lines by status code:
   possible status code: `200, 301, 400, 401, 403, 404, 405 and 500`
   if a status code doesn’t appear, don’t print anything for this status code
   format: `<status code>: <number>`
   status codes should be printed in ascending order


