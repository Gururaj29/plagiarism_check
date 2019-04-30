from src import type_zero
from src import type_one
from src import type_two
from src import type_three

file_one  = "sample_one.c"
file_two = "sample_two.c"

print(type_zero.compare_files(file_one, file_two ))
print(type_one.compare_files(file_one, file_two))
print(type_two.compare_files(file_one, file_two))
print(type_three.compare_files(file_one, file_two))