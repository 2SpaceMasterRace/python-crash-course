# Single line comments

"""Multiline comments"""

###################################
# Primitive datatypes and operaters
###################################

# numbers
number = 4096

# math operators
addition = 1 + 1
subraction = 1 - 1
multiplication = 1 * 1

modulo = 5 % 2
# i%j has the same sign as j
modulo_negative = -5 % 3

# result of division is always a float
division = 10.0 / 3

exponent = 2**3
precedence = (1 * 3) + 5

# floor divison rounds towards negative infinity
floor_division = 5 // 3
floor_division_negative = -5 // 3
float_floor_division = 5.0 // 3.0
float_floor_division_negative = -5.0 // 3.0

# boolean values
booleanTrue = True
booleanFalse = False
negateBoolean = not True

# boolean operators, and/or are case sensitive
boolean_and = True and False
boolean_or = True or False

# True and False are 1 and 0 with different keywords
addition_boolean = True + True
comparision_boolean = True < 0
equality_boolean = True == 2
equality_negative_boolean = False > -5


# All values eval to True except for 0, None, empty strings, lists, dicts, tuples, sets

eval_number = bool(number)
eval_negative_number = bool(-number)
eval_zero = bool(0)
eval_none = bool(None)
eval_empty_string = bool("")
eval_lists = bool([])
eval_dicts = bool({})
eval_tuples = bool(())
eval_set = bool(set())

# boolean logical operators on int casts them to booleans and returns non-cast value
bool_cast = bool(0)  # returns False
bool_operator = 0 and 1  # returns 0

equality = 1 == 1
inequality = 2 != 1

compare_left = 1 < 10
compare_right = 10 > 5
compare_equal_left = 1 <= 5
compare_equal_right = 5 >= 4

value_in_range = 1 < 3 and 3 < 6
comparision_chaining = 1 < 2 < 3

# is checks if two variables refer to the same object, == checks if the objects pointed to has the same variables
a = [1, 2, 3, 4, 5]
b = a

same_object = b is a
same_values = b == a

b = [1, 2, 3, 4, 5]
not_same_object = b is a
but_same_values = b == a

# create strings
string_one = "this is a string"
string_two = "this is also a string "

addition_of_string = "Hello" + " World"
"helloworld !"  # string literals (not variables) can be concateneated using the + operator

string_character_access = "Hello World"[0]
string_len = len("the length of this string is")

formatted_string_literals = f"the length of string is {string_len} characters long"

none_object = None
compare_objects = None is "etc"  # is checks for equality of object


############################################################################
# Variables and collection
############################################################################


print("python has a print function")
print(
    "modify optional argument end to change the end string instead of default newline",
    end="!",
)

input_data_from_console = input("Enter some data:")
if_expression = "yay" if 0 > 1 else "nay"


list_sequence = []
prefilled_list = [1, 2, 3, 4, 5]
append_list = list_sequence.append(1)
pop_list_from_end = prefilled_list.pop()

access_list = prefilled_list[0]
access_list_from_last = prefilled_list[-1]
index_error = prefilled_list[5]

# slice : [start, end)
# slice : [start:end:step]
slice_list = prefilled_list[1:3]  # returns from index 1 to index 3
slice_list_from_start_index = prefilled_list[
    2:
]  # returns list from second index to end
sliceList_from_index = prefilled_list[
    :3
]  # returns list from beginning to index 3 with it not being included
slice_step_ahead = prefilled_list[
    ::2
]  # return list selecting elements of step size of 2
reverse_list = prefilled_list[::-1]


deep_copy_list = prefilled_list[
    :
]  # values are the same but objects are not and will result in False
# delete_specific_element_from_list
del prefilled_list[2]

remove_first_occurence_of_value = prefilled_list.remove(2)
value_error = prefilled_list.remove(2)

insert_element_at_specific_index = prefilled_list.insert(2, 6)
get_index_of_first_element_from_argument = prefilled_list.index(1)

add_lists = list_sequence + prefilled_list
extend_list = list_sequence.extend(prefilled_list)

check_existence_of_element = 1 in prefilled_list
list_length = len(prefilled_list)
