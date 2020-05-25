#!/usr/bin/env python3

# File Name:    Pattern.py
# Created by:   Vadim Lakhterman
# Date:         24.5.20
# Last Update:  25.5.20

from json import JSONEncoder
import json

class Pattern:
    def __init__(self, name, expression, start, end):
        self.name = name
        self.expression = expression
        self.start = start
        self.end = end

    def toDict(self):
        return self.__dict__


class PatternEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Pattern):
            return obj.__dict__