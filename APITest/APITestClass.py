# -*- coding:utf-8 -*-

import requests
import unittest
import json
from Dict2Str import _any2str, _post2str

class CallAPITest():
    '''
    A api test class, that finishs the test of 'get' and 'post' method requests
    '''
    def __int__(self):
        pass

    def apicall(self, method='', url='', getparams='', postparams={}, expect_code=0):
        result = ''
        resultLog = url + '+*+'
        testPass = 0    # 0 represent the test case is pass, 1 is cannot pass, 2 is undetermined, 3 is url wrong
        if method == 'GET':
            if getparams != '':
                result = requests.get(url, getparams)
            else:
                result = requests.get(url)
            resultLog += str(getparams) + '+*+'

        elif method == 'POST' or 'post':
            if postparams != {}:
                result = requests.post(url, json=postparams)
            else:
                result = requests.post(url)
            resultLog += _post2str(postparams) + '+*+'

        elif method == 'SQL' or 'sql':
            if getparams != {}:
                url += '?'
                for item in getparams:
                    url += item + '=' + getparams[item] + '&'
                url = url[:-1]
            result = requests.get(url)
            resultLog += _post2str(getparams) + '+*+'

        else:
            pass

        # this if-block used to solve the url wrong
        if result.status_code == 404:
            testPass = 3
            resultLog += str(result.status_code) + '+*+' + str(result.reason) + '+*+' + str(testPass)
            return resultLog

        jsdata = json.loads(result.text)

        # The expected message of response result is 'success', so it's as a checking benchmark
        if jsdata['retcode'] == expect_code:
            print 'Testcase: ', postparams, ' --------------------- OK!'
        elif jsdata['retcode'] != expect_code and expect_code == 0 :
            if jsdata['retcode'] == 4000:
                testPass = 1
                print 'Testcase: ', postparams, '-------------------- Failure!'
            else:
                testPass = 2
                print 'The test result cannot judge, because the current test case is auto produce!'
        else:
            testPass = 1
            print 'Testcase: ', postparams, '-------------------- Failure!'

        if jsdata['message'] == 'success':
            resultLog += str(jsdata['retcode']) + '+*+' + _any2str(jsdata['retbody']) + '+*+' + str(testPass)
        else:
            resultLog += str(jsdata['retcode']) + '+*+' + str(jsdata['message']) + '+*+' + str(testPass)
        return resultLog


