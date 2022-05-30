#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, result):
        return False

    def __ne__(self, result):
        return True
