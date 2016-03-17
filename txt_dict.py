# -*- encoding: utf-8 -*-

def load_dict_from_file(filepath):
    _dict = {}
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split(':')
                _dict[key] = value
        return _dict
    except IOError as ioerr:
        print u"文件 %s 不存在" % (filepath)

    return _dict

def save_dict_to_file(_dict, filepath):
    try:
        with open(filepath, 'w') as dict_file:
            for (key,value) in _dict.items():
                dict_file.write('%s:%s\n' % (key, value))
    except IOError as ioerr:
        print u"文件 %s 无法创建" % (filepath)

if __name__ == '__main__' :
    print u'从txt中获取的字典'
    _dict = load_dict_from_file ('D:\\dic.txt')
    print _dict