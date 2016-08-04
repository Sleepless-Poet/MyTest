#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
This module is used to translate the dict into str
'''
def _post2str(post_data={}):
    result = ''
    if len(post_data) == 0:
        return result
    for key in post_data:
        #print dict0[key], type(dict0[key]), '\n'
        result += key + ':'
        if type(post_data[key]) is int:
            result += str(post_data[key]) + ', '
        elif type(post_data[key]) is float:
            result += str(post_data[key]) + ', '
        else:
            if post_data[key] is None:
                continue
            else:
                result += post_data[key].decode('utf-8') + ', '

    return result

def _any2str(anytype):
    if type(anytype) is dict:
        return _d2str(anytype)
    else:
        return _l2str(anytype)

def _d2str(dict0={}):
    result = ''
    if len(dict0) == 0:
        return result
    for key in dict0:
        #print dict0[key], type(dict0[key]), '\n'
        result += key + ':'
        if type(dict0[key]) is int:
            result += str(dict0[key]) + ', '
        elif type(dict0[key]) is float:
            result += str(dict0[key]) + ', '
        elif type(dict0[key]) is dict:
            result += '{' + _d2str(dict0[key]) + '}, '
        elif type(dict0[key]) is list:
            result += '[' + _l2str(list0=dict0[key]) + '], '
        else:
            if dict0[key] is None:
                continue
            else:
                result += dict0[key] + ', '

    return result

def _l2str(list0=[]):
    result = ''
    if len(list0) == 0:
        return result
    for item in list0:
        if type(item) is dict:
            result += '{' + _d2str(item) + '}, '
        elif type(item) is int:
            result += str(item) + ', '
        elif type(item) is float:
            result += str(item) + ', '
        elif type(item) is list:
            result += '[' + _l2str(item) + '], '
        else:
            if item is None:
                continue
            else:
                result += item # .decode('utf-8').encode('raw_unicode_escape') + ', '

    return result


if __name__ == '__main__':
    d = {
    "category": "3",
    "describe": "衣服类型",
    "pic_src": [
      "http://159.99.93.181:8099/static/thumb/14659709237134.gif",
      "http://159.99.93.181:8099/static/thumb/14660572898529.png"
    ],
    "stock_avg_price": 2.3,
    "standard_price": 1100,
    "number": 10980,
    "vip_price": 900,
    "sale_total_number": 152,
    "stock_quantity": -35,
    "pic_hd_src": [
      "http://159.99.93.181:8099/static/upload/14659709237134.gif",
      "http://159.99.93.181:8099/static/upload/14660572898529.png"
    ],
    "product_name": "nike",
    "unit": "箱"
    }

    d1 = {
    "last_update_time": 1467082346.692103,
    "next_page": "false,最后一页true还有下一页",
    "product_list": [
      {
        "category": "裤子",
        "sale_number": 2,
        "name": "adidas",
        "standard_price": 1100,
        "stock_price": 88,
        "vip_price": 900,
        "avg_price": 1100,
        "last_sale_time": "2016-06-28 10:52:26.692103",
        "pic_src": "",
        "product_code": "43333113332233",
        "quantity": 9
      }
    ],
    "deleted_list":[
      {
        "category": "裤子",
        "sale_number": 2,
        "name": "adidas",
        "standard_price": 1100,
        "stock_price": 88,
        "vip_price": 900,
        "avg_price": 1100,
        "last_sale_time": "2016-06-28 10:52:26.692103",
        "pic_src": "",
        "product_code": "43333113332233",
        "quantity": 9
      }
    ]
    }

