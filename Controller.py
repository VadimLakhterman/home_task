#!/usr/bin/env python3

# File Name:    Controller.py
# Created by:   Vadim Lakhterman
# Date:         24.5.20
# Last Update:  25.5.20

import re
import os
import mmap
import json
import Pattern
import Report
import time
import threading 
from Pattern import *
from Report import *

ZERO_LEAD_EXP = b'(\x00)([0-9a-fA-F]+)(?:--)?'

class Controller:
    found = []
    
    def __init__(self):
        self.report = Report()
        self.lock = threading.RLock()
        

    def find_expressions(self, path, espressions, name=None):
        '''
    Input:          Path, dictionary of expressions, optional name
    Output:         None
    Description:    Search for all expressions in file when name is None, 
    otherwise search expression that match the name.
    '''
        search_pattern = None
        if( not os.path.exists(path)):
            print("Error: File does not exists!")
            return

        if(not espressions):
            print("Error: Expressions list empty!")
            return

        self.report.write_new_test_results(self.find_expressions.__name__)
        if(name):
            for exp , pattern_name in espressions.items():
                if pattern_name == name:
                    search_pattern = exp
                    break
            if search_pattern:
                regex = re.compile(bytes.fromhex(search_pattern))
            else:
                print("Error, name does not exists in dictionary")
                return
            search_tread = threading.Thread(target=self.search, args=(path, regex, name))
            write_tread = threading.Thread(target=self.write, args=(self.found,))
            search_tread.start()
            time.sleep(1)
            write_tread.start()
            search_tread.join()
        else:
            for expression in espressions:
                exp_name = espressions.get(expression)
                regex = re.compile(bytes.fromhex(expression)) # Returns object
                search_tread = threading.Thread(target=self.search, args=(path, regex, exp_name))
                write_tread = threading.Thread(target=self.write, args=(self.found,))
                search_tread.start()
                time.sleep(1)
                write_tread.start()
                search_tread.join()
                write_tread.join()
        self.report.close_test_results()
            

    def find_zero_leading(self, path):
        '''
    Input:          File path
    Output:         None
    Description:    This method searches for all 0x00XXXXXX patterns.
    '''
        if( not os.path.exists(path)):
            print("Error: File does not exists!")
            return

        global ZERO_LEAD_EXP 
        self.report.write_new_test_results(self.find_zero_leading.__name__)
        regex = re.compile(ZERO_LEAD_EXP) # Returns object
        search_tread = threading.Thread(target=self.search, args=(path, regex))
        write_tread = threading.Thread(target=self.write, args=(self.found,))
        search_tread.start()
        time.sleep(1)
        write_tread.start()
        search_tread.join()
        write_tread.join()
        self.report.close_test_results()
               

    def search(self, path, expression, expression_name = None):
        '''
        Input: Path and expression, expression_name is optional
        Output:None
        Description: Method search for expression in file using mmap module instead of load whole file to the memory, this allows to deal with large files.
        '''
        start=time.time()
        with open(path, 'rb') as file:
            mapped_file = mmap.mmap(file.fileno(), 0, access = mmap.ACCESS_READ)
            items = expression.finditer(mapped_file)
            if(items):
                for match in items:
                    if (not expression_name):
                        pattern = Pattern(str(match.group()), str(match.group()), hex(match.start()), hex(match.end()))
                    else:
                        pattern = Pattern(expression_name, str(match.group()), hex(match.start()), hex(match.end()))
                    with self.lock:
                        self.found.append(pattern)
        end = time.time()
        duration = end-start
        print ("Search duration in seconds: " + str(duration))


    def finish(self):
        self.report.finish()


    def write(self, data):
        while data:
            with self.lock:
                item = data.pop()
                self.report.write_result(item)
        print("Wtire finished")