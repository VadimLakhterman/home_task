#!/usr/bin/env python3

# File Name:    Report.py
# Created by:   Vadim Lakhterman
# Date:         24.5.20
# Last Update:  25.5.20

import time
import os
import os.path
import Pattern
from Pattern import *

RESULTS_FOLDER = 'Results'
RESULTS_FILENAME = RESULTS_FOLDER + '/' + 'results'
TIME = time.strftime("%d%m%y_%H%M%S")
FORMAT = '.json'

class Report:

    def __init__(self):
        if (not os.path.exists(RESULTS_FOLDER)):
            os.mkdir(RESULTS_FOLDER)
        with open(RESULTS_FILENAME + '_' + TIME + FORMAT, 'w+') as self.file:
            self.file.write("{\n\"Results\": [\n")

    def write_new_test_results(self, name):
        with open(RESULTS_FILENAME + '_' + TIME + FORMAT, 'a+') as self.file:
            self.file.write("{\n\"" + name + "\": [\n")

    def close_test_results(self):
        with open(RESULTS_FILENAME + '_' + TIME + FORMAT, 'a+') as self.file:
            self.file.write("]\n}\n")

    def write_result(self, data):
        results = data.toDict()
        with open(RESULTS_FILENAME + '_' + TIME + FORMAT, 'a+') as self.file:
           self.file.write(json.dumps({"found " : results}, indent=4, cls=PatternEncoder))

    def finish(self):
        with open(RESULTS_FILENAME + '_' + TIME + FORMAT, 'a+') as self.file:
            self.file.write("]\n}\n")