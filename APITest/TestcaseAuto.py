import random

def _autotestcase(para_body={}):
    if para_body == {}:
        return
    random_test_cases = []
    for i in range(len(para_body)):
        random_test_cases.append({})

    for item in para_body:
        for j in range(len(random_test_cases)):

            ran = random.randint(0, 3)
            if ran == 0:
                random_test_cases[j][item] = para_body[item]
            elif ran == 1:
                random_test_cases[j][item] = ''
            elif ran == 2:
                random_test_cases[j][item] = str(para_body[item]) + '*#@'
            elif ran == 3:
                random_test_cases[j][item] = random.uniform(-1000, 1000)
                # print j, random_test_cases[j]

    return random_test_cases

