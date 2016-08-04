# -*- coding:utf-8 -*-

'''
This module is the automation interface testing frame
'''

import unittest
from TestcaseAuto import _autotestcase
from APITestClass import CallAPITest
from RwData import TestcaseLoader, TestLog
import Global_list


class ExecuteAPItest(unittest.TestCase):
    '''
    This class is execute the specific test case, in our test scenario, we only have a API test
    '''
    def setUp(self):
        # initialize some basic parameter for test runner, load the test cases and produce some cases
        self.serverAddr = 'http://' + Global_list.serverAddr
        self.result = self.serverAddr + '\n\n\n'    # the result form is: result = 'serverAddr\n\n\n testcaseID+*+url+*+postgrams+*+retcode+*+message+*+testPass'
        self.record = 0     # record the number of test case
        self.testCases = Global_list.testCases      # input the data from excel testCases = [{url:[{data0: xxx, data1: xxx, ....}, method,code]}, {}, {}]
        self.newCases = []              # produce the new test cases randomly
        for tc in self.testCases:
            #print 'tc.values[0][0]', type(tc), tc
            tempResult = _autotestcase(tc.values()[0][0])
            for tempdict in tempResult:
                new_item = {}
                new_item[tc.keys()[0]] = []
                new_item[tc.keys()[0]].append(tempdict)
                new_item[tc.keys()[0]].append(tc.values()[0][1])
                self.newCases.append(new_item)

    def test_API(self):
        # call the specific function to execute the test runner
        call = CallAPITest()
        for item in self.testCases:
            self.record += 1
            self.result += str(self.record) + '+*+' + call.apicall(method=item.values()[0][1], url=self.serverAddr+item.keys()[0], postparams=item.values()[0][0], expect_code=item.values()[0][2]) + '\n\t\n'
        for newItem in self.newCases:
            self.record += 1
            self.result += str(self.record) + '+*+' + call.apicall(method=newItem.values()[0][1], url=self.serverAddr + newItem.keys()[0], postparams=newItem.values()[0][0])
            self.result += '\n\t\n'
        TestLog(self.result).store_result()    # store the result into the logInfo file


if __name__ == '__main__':
    unittest.main()


