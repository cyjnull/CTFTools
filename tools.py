"""
整合加密解密工具在一个类中
"""

import string
import re

class CTFTools:
    '''
    集合了一些CTF的加密解密方法
    '''

    @staticmethod
    def caesar_cipher_list(text):
        ''' 展示出所有的凯撒密码可能的情况
        使用print打印出所有凯撒密码的组合

        :param text: 需要处理的字母字符串
        :return:
        '''

        for i in range(1,24):
            c = string.ascii_letters
            lc = [chr((j - 97) % 26 + 97) for j in range(97 + i, 123 + i)]
            uc = [chr((j - 65) % 26 + 65) for j in range(65 + i, 91 + i)]
            r = ''.join(lc) + ''.join(uc)
            print(str(i) + '：' +text.translate(text.maketrans(c, r)))

    @staticmethod
    def flashback(text,sep=''):
        ''' 逆序字符串
        :param text: 逆序的文本
        :param sep: 间隔符,''为无间隔符，' '为以空格为间隔单独倒叙
        :return:
        '''
        if sep == '':
            print(text[::-1])
        else :
            text = text.split(sep)
            for i,v in enumerate(text):
                text[i] = v[::-1]
            print(sep.join(text))

    @staticmethod
    def qwe_encrypt(text):
        ''' 调用qwe函数进行解密
        :param text: 操作的字符串
        :return:
        '''
        CTFTools.qwe(text,True)

    @staticmethod
    def qwe_decrypt(text):
        ''' 调用qwe函数进行解密
        :param text: 操作的字符串
        :return:
        '''
        CTFTools.qwe(text,False)

    @staticmethod
    def qwe(text,is_encrypt):
        ''' qwe加解密
        :param text: 操作的字符串
        :param is_encrypt: 判断是加密还是解密
        :return:
        '''
        str_encrypt = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        str_decrypt = string.ascii_letters
        if is_encrypt:
            print(text.translate(text.maketrans(str_decrypt, str_encrypt)))
        else:
            print(text.translate(text.maketrans(str_encrypt, str_decrypt)))

    @staticmethod
    def fence_cipher_encrypt(text,width):
        text = text.replace(' ','')
        if len(text) % width:
            print("宽度不是长度的因子")
        else:
            mat = []
            for x in range(width):
                for i in range(len(text)):
                    if ((i + x) % width == 0):
                        mat.append(text[i])
            print(''.join(mat))

    @staticmethod
    def fence_cipher_decrypt(text):
        text = text.replace(' ', '')
        elen = len(text)
        field = []
        for i in range(2, elen):
            if (elen % i == 0):
                field.append(i)
        for f in field:
            b = int(elen / f)
            result = {x: '' for x in range(b)}
            for i in range(elen):
                a = i % b;
                result.update({a: result[a] + text[i]})
            d = ''
            for i in range(b):
                d = d + result[i]
            print('分为 ' + str(f) + ' ' + '栏时，解密结果为：' + d)

    @staticmethod
    def rot13(text):
        string_temp = []
        text = text.lower()
        isnum = re.compile(r'\d')
        isalpha_am = re.compile(r'[a-m]')
        isalpha_nz = re.compile(r'[n-z]')
        for i in text:
            if (isnum.match(i)):
                string_temp.append()
            elif (isalpha_am.match(i)):
                i = chr(ord(i) + 13)
                string_temp.append(i)
            elif (isalpha_nz.match(i)):
                i = chr(ord(i) - 13)
                string_temp.append(i)
            elif (i == " "):
                string_temp.append(" ")
            else:
                print("error")
        print("经过ROT3解密后的字符串为：%s" % (''.join(string_temp)))

