from tests import type_zero_test
import sys
import os
import config

test_command = config.TEST_COMMAND

os.system(test_command + "tests/type_zero_test.py")