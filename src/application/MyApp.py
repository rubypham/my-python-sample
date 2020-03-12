'''
Created on 12 Mar 2020

@author: User
'''

from library.StringUtils import StringUtils
from library import CommonConstant


def main():
    util = StringUtils()
    
    print("Hello")
    print(CommonConstant.ROOT_DIR)
    print("Hello from " + util.convert_string_to_date(" value"))


if __name__ == '__main__':
    main()

