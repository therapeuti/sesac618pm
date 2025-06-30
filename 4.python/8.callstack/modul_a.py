def function_a1():
    print('module_a의 function_a1 호출 ')
    function_a2()

def function_a2():
    print('module_a의 function_a2 호출 ')
    function_a3()

def function_a3():
    print('module_a의 function_a3 호출 ')
    test_1234()


def test_1234():
    print('module_a의 test_1234 호출 ')
    deep_call1()

def deep_call1():
    print('호출 ')
    raise RuntimeError('의도적으로 발생한 나의 예외')


def call_test():
    print('나 modul_a 실행됨')


# call_test()

if __name__=='__main__':
    call_test()