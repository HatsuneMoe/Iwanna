# encoding=utf-8
import re
import os
import time
import json
import urllib.parse
import urllib.request


base_path = ""


def rm_it(func):
    def dec(*args):
        if os.path.exists(base_path + name + '.json'):
            os.remove(base_path + name + '.json')
        result = func(*args)
        return result
    return dec


@rm_it
def main(_name):
    main_loop(_name)(1)


def main_loop(_name):
    def main_loop_curry(num):
        return main_loop(_name)(num+1) if not_end(process_pages(fetch_html(_name)(num)))(_name) else print('complete!')
    return main_loop_curry


def not_end(_list):
    def not_end_curry(_name):
        print(_list)

        def save_json():
            def write_json(_ori_list=_list):
                with open(base_path+_name + '.json', 'w+') as _f:
                    _f.write(json.dumps(_ori_list, ensure_ascii=False, indent=2))

            def exists():
                os.rename(base_path+_name+'.json', base_path+_name+'.bak.json')
                with open(base_path+_name + '.bak.json', 'r+') as _r:
                    write_json(json.loads(_r.read()) + _list)
                    os.remove(base_path + _name + '.bak.json')

            return exists if os.path.exists(base_path+_name+'.json') else write_json
        save_json()()
        print(os.path.exists(base_path + _name + '.json'))
        time.sleep(5)
        return True if len(_list) > 1 else False
    return not_end_curry


def process_pages(_list):
    return list(map(lambda item: {'title': item[0],
                                  'content': item[1],
                                  'tieba': item[2],
                                  'time': item[3],
                                  }, _list))


def fetch_html(_name):
    def encode_name(_n): return urllib.parse.quote_plus('' if _n is None else str(_n).encode('GB2312'))

    def gen_url(_enn, _p): return "http://tieba.baidu.com/f/search/ures?kw=&qw=&rn=10&un=" + \
                                  encode_name(_enn) + "&only_thread=&sm=0&sd=&ed=&pn=" + str(_p)

    def get_resp(_url): return urllib.request.urlopen(_url).read().decode('GBK')

    def match_result(_html):
        _restr = r'<div class=\"s_post\"><span class=\"p_title\"><a.*?>' \
                 r'(.*?)</a></span>.*?<div class=\"p_content\">([\s\S]*?)' \
                 r'</div>.*?<font class=\"p_violet\">(.+?)</font>.*?<font ' \
                 r'class=\"p_green p_date\">(.+?)</font>.*?</div>'
        return re.findall(re.compile(_restr), _html)

    def fetch_html_curry(p):
        print(gen_url(_name, p))
        return match_result(get_resp(gen_url(_name, p)))

    return fetch_html_curry


if __name__ == "__main__":
    name = ''
    main(name)
