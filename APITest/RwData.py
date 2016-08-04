# -*- coding:utf-8 -*-

'''
This module read data test cases from excel, and write the test result into the other excel
'''

import os
import xlrd
import xlwt as ExcelWrite


# the color of excel, to differ the result of test
styleRedBkg = ExcelWrite.easyxf('pattern: pattern solid, fore_colour red; font: bold on;')
styleBlueBkg = ExcelWrite.easyxf('pattern: pattern solid, fore_colour blue; font: bold on;')
styleLBlueBkg = ExcelWrite.easyxf('pattern: pattern solid, fore_colour light_blue; font: bold on;')
styleYellowBkg = ExcelWrite.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on;')
styleGrayBkg = ExcelWrite.easyxf('pattern: pattern solid, fore_colour gray25; font: bold on;')

class TestcaseLoader():
    # TODO
    def __init__(self, filename):
        try:
            os.path.exists(filename)
            self.data = xlrd.open_workbook(filename)
        except Exception, e:
            print Exception, ":", e

    def load_test_case(self):
        # TODO
        table = self.data.sheets()[0]
        nrows = table.nrows
        test_cases = []         # test_cases = [{url:[{post_data}, expect_code]},{},...]

        serverAddress = table.row_values(0)[1]
        for i in range(2, nrows):
            singlecase = {}
            key = table.row_values(i)[0].encode('raw_unicode_escape')  # row_values(i) is get the data of i'th row
            if key == 'END':
                break
            singlecase[key] = []
            # this try-except is used throw the bad-form of post body.
            try:
                temp_dict = eval('{'+ table.row_values(i)[2] +'}') # put the data store in the dict
                singlecase[key].append(temp_dict)
                singlecase[key].append(table.row_values(i)[1].encode('raw_unicode_escape'))
                singlecase[key].append(int(table.row_values(i)[3]))
                test_cases.append(singlecase)
            except Exception, e:
                print '\nThe %dth row form of post data is wrong, please modify your test case Excel!\n' % i
                print Exception, ":", e

        return serverAddress, test_cases



class TestLog():


    # TODO
    def __init__(self, result):

        self.xls = ExcelWrite.Workbook()
        self.sheet = self.xls.add_sheet("Sheet1")
        self.sheet.write(0, 0, 'Server Address', styleYellowBkg)
        self.sheet.write(1, 0, 'TestcaseID', styleLBlueBkg)
        self.sheet.write(1, 1, 'URL', styleLBlueBkg)
        self.sheet.write(1, 2, 'Post Data', styleLBlueBkg)
        self.sheet.write(1, 3, 'retcode', styleLBlueBkg)
        self.sheet.write(1, 4, 'Response Message', styleLBlueBkg)
        self.sheet.write(1, 5, 'Test Result Information', styleLBlueBkg)
        self.result = result

    def store_result(self):
        import Global_list
        # tempResult = 'serverAddr\n\n\ntestcaseID+*+url+*+post data+*+rect_code+*+response message+*+checkingResult\n\t\n ...'
        tempResult = self.result.split('\n\n\n')
        self.sheet.write(0,1,tempResult[0])
        i = 0
        tempResult = tempResult[1].split('\n\t\n')
        for item in tempResult:
            # A test case result, according the result add the respond color
            itemResult = item.split('+*+')
            #print itemResult, '\n\n'
            for rest in itemResult:
                rest = rest.encode('raw_unicode_escape')
                if i%6 == 5 and rest == '0':
                    self.sheet.write(i/6+2, i%6, 'This test is pass')
                elif i%6 == 5 and rest == '1':
                    self.sheet.write(i/6+2, i%6, 'This test is cannot pass', styleRedBkg)
                elif i%6 == 5 and rest == '2':
                    self.sheet.write(i/6+2, i%6, 'This test is auto produce, so cannot determined ', styleGrayBkg)
                elif i%6 == 5 and rest == '3':
                    pass
                else:
                    self.sheet.write(i/6+2, i%6, rest.encode('raw_unicode_escape'))
                i += 1

        self.xls.save(Global_list.Logfilename)



if __name__ == '__main__':
    readFile = TestcaseLoader('testcases.xls')
    print readFile.load_test_case()
    #result = "159.99.93.113:8199\n\n\n1+*+/reg/empolyee/login+*+{'password': '123', 'employee_id': '1233', 'company_id': '136'}+*+4000+*+unsuccess+*+1\n\t\n1+*+/reg/empolyee/login+*+{'password': '123', 'employee_id': '1233', 'company_id': '136'}+*+200+*+success+*+0\n\t\n"
    #store_excel = TestcaseLoader(result)
    #store_excel.store_result()