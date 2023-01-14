def get_digit(a_digits, i):
    if i > len(a_digits):
        return None
    return a_digits[len(a_digits) - i]

def add2(a, b):
    # 两个个位数相加
    c = '' + str(int(a) + int(b))
    if len(c) == 1:
        c = '0' + c
    return c[0], c[1]

def add3(a, b, c):
    # 三个个位数相加
    d = '' + str(int(a) + int(b) + int(c))
    if len(d) == 1:
        d = '0' + d
    return d[0], d[1]

def add(a, b):
    a_digits = list(a)
    b_digits = list(b)
    i = 1
    jinwei = 0
    stack = []
    while True:
        cur_a = get_digit(a_digits, i)
        cur_b = get_digit(b_digits, i)
        
        # when to stop
        if cur_a is None and cur_b is None:
            break

        if cur_b is None:
            res = add2(cur_a, jinwei)
        elif cur_a is None:
            res = add2(cur_b, jinwei)
        else:
            res = add3(cur_a, cur_b, jinwei)

        jinwei, digit = res
        
        stack.append(digit)
        i += 1
    stack.reverse()
    return ''.join(stack)
        
ret = add('455465564658779796258746521465749754586856447875461473885411447863556845956752123', '45789611122233456278994579840485003519731434516778946859123495643194613462031003164979465558164325')
print(ret)

'''
                   455465564658779796258746521465749754586856447875461473885411447863556845956752123
+ 45789611122233456278994579840485003519731434516778946859123495643194613462031003164979465558164325
----------------------------------------------------------------------------------------------------
  45789611122233456734460144499264799778477955982528701445979943518656087347442451028536311514916448
'''