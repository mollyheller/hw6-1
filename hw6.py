import re
import unittest

def sumNums(fileName):
    data= open(fileName, 'r')
    data= data.read()
    nums = re.findall("(?<!\d|-)\d+(?!\d|-)", data)
    total=0
    for x in nums:
        total += int(x)

    return total

def countWord(fileName, word):
    data= open(fileName, 'r')
    data= data.read()
    word_list = re.findall('(?i)' + str(word) + '(?!\w+)', data)

    return len(word_list)

def listURLs(fileName):
    data = open(fileName, 'r')
    data = data.read()
    urls = re.findall("\S+\.{1}\S+\.{1}\w+", data)
    return urls

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
       """ test count word on the first file """
       self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)
# run the tests
unittest.main(verbosity=2)
