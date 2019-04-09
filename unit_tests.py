from tests import type_zero_test
import sys
import os
import config

test_command = config.TEST_COMMAND

#Type zero
print( "-"*10 + "Executing unit tests for type_zero" + "-"*10)
os.system(test_command + "tests/type_zero_test.py")

#Type one
print( "-"*10 + "Executing unit tests for type_one" + "-"*10)
os.system(test_command + "tests/type_one_test.py")