from RwData import TestcaseLoader

filename = './Log/testcases.xls'
readData = TestcaseLoader(filename=filename)
Logfilename = filename.split('.xls')[0] + '_log.xls'
serverAddr, testCases = readData.load_test_case()       # testcases = [{'url':[{'a':1}, 200]}], from the excel file