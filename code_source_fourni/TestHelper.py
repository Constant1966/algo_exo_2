# class TestHelper:
#     RED = "\u001B[31m"
#     GREEN = "\u001B[32m"
#     WHITE = "\u001B[37m"

#     @staticmethod
#     def printHeader(header):
#         print(TestHelper.WHITE + header)

#     @staticmethod
#     def printError(content):
#         print(TestHelper.RED + content)

#     @staticmethod
#     def printTest(is_good):
#         method_name = inspect.stack()[1].function
#         print((TestHelper.GREEN if is_good else TestHelper.RED) + " > " + method_name)


import sys

class TestHelper:
    RED = "\u001B[31m"
    GREEN = "\u001B[32m"
    WHITE = "\u001B[37m"

    @staticmethod
    def printHeader(header):
        print(TestHelper.WHITE + header)

    @staticmethod
    def printError(content):
        print(TestHelper.RED + content)

    @staticmethod
    def printTest(is_good):
        method_name = sys._getframe(1).f_code.co_name
        print((TestHelper.GREEN if is_good else TestHelper.RED) + " > " + method_name)
