'''
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
Versiono: 0.1
Author: Dezi
Date: 2019-11-12
'''
import random

def generate_code(code_len=4):
    '''
    生成指定长度的验证码
    :param code_len:验证码的长度
    :return:大小写字母和数字构成的验证码
    '''
    all_chars = '0123456789abcdefghilgklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_post = len(all_chars)-1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_post)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    print(generate_code())