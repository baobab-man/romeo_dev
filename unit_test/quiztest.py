#-*- coding: utf-8 -*-
import unittest
import impl # from . 삭제


class PythonTest(unittest.TestCase):

    def test_table_to_dict_list(self):
        table = [
            ['월', '일', '품명', '수량', '단가', '공급가액', '부가세', '코드', '거래처명'],
            ['01', '01', '어헤드', '', '', '10,364', '1,036', '00140', '흑자스토어'],
            ['01', '01', '어헤드', '', '', '10,999', '1,101', '00406', '서울스토어'],
            ['01', '01', '어헤드', '', '', '1,818', '182', '00237', '핏펫스토어']
        ]

        dict_list = impl.table_to_dict_list(table)
        self.assertEqual('10,364', dict_list[0]['공급가액'])
        self.assertEqual('서울스토어', dict_list[1]['거래처명'])

    def test_filter_list(self):  # 반복문을 사용시 데이터가 존재하지 않음에도 무의미한 반복을 진행할 때 등장 : TypeError: 'NoneType' object is not iterable
        data = range(0, 100)

        filtered = impl.multiple_of_three(data)

        for number in filtered:
            self.assertEqual(number % 3, 0)

    def test_json(self):
        data = '''{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}'''

        self.assertEqual('Standard Generalized Markup Language', impl.pick_gloss_term(data, 'GlossTerm'))

    def test_sorted_distinct_list(self):  # 리스트를 셋으로 변환후 중복제거하고 다시 리스트로 정
        data = [1, 5, 8, 10, 4, 9, 11, 10, 8, 14, 3, 4]

        self.assertEqual([1, 3, 4, 5, 8, 9, 10, 11, 14], impl.sort_and_distinct(data))

    def test_custom_sort(self):
        class Voucher:
            def __init__(self, trader, amount):
                self.trader = trader
                self.amount = amount

            def __getitem__(self, amount):  # getitem 메소드추가
                return self.amount


        data = [
            Voucher('잇쮸', 125000),
            Voucher('어헤드', 8500),
            Voucher('플라고', 288000),
            Voucher('잇츄', 80000),
        ]

        vouchers = impl.sort_by_amount(data)
        self.assertEqual('플라고', vouchers[0].trader)
        self.assertEqual('어헤드', vouchers[-1].trader)

    def test_dispatch_by_string(self): # 조건문으로 사칙연산 정의
        self.assertEqual(18, impl.calc('multiply', 6, 3))
        self.assertEqual(2, impl.calc('divide', 6, 3))
        self.assertEqual(9, impl.calc('add', 6, 3))
        self.assertEqual(3, impl.calc('subtract', 6, 3))

    def test_traverse(self):
        unix_tree = {
            'Unix': {
                'PWB/Unix': {
                    'System III': {
                        'HP-UX': None
                    },
                    'System V': {
                        'UnixWare': None,
                        'Solaris': {
                            'OpenSolaris': None
                        }
                    }
                },
                'BSD': {
                    'Unix 9': None,
                    'FreeBSD': None,
                    'NetBSD': None,
                    'MacOS': None
                },
                'Xenix': {
                    'Sco Unix': {
                        'OpenServer': None
                    },
                    'AIX': None,
                },
            },
            'Linux': {
                'Debian': {
                    'Ubuntu': None,
                    'Linux Mint': None
                },
                'Redhat': {
                    'CentOS': None,
                    'Fedora': None
                },
                'Gentoo': None
            }
        }

        self.assertEqual('OpenSolaris', impl.find_deepest_child(unix_tree))
        self.assertSetEqual({'Unix', 'BSD', 'Linux'}, impl.find_nodes_that_contains_more_than_three_children(unix_tree))
        self.assertEqual(7, impl.count_of_all_distributions_of_linux(unix_tree))

    def test_polymorphism(self):
        messages = [
            impl.Notice('Welcome to chat'),
            impl.Message(userid=1, content='Hello World'),
            impl.Message(userid=2, content='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
            impl.Message(userid=3, content='안녕하세요.'),
            impl.Message(userid=2, content='ありがとうございます。'),
        ]

        self.assertEqual('''<li class="notice">Welcome to chat</li>
<li class="left">
    <img class="profile" src="${user_image(1)}">
    <div class="message-content">Hello World</div>
</li>
<li class="right">
    <img class="profile" src="${user_image(2)}">
    <div class="message-content">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
</li>
<li class="left">
    <img class="profile" src="${user_image(3)}">
    <div class="message-content">안녕하세요.</div>
</li>
<li class="right">
    <img class="profile" src="${user_image(2)}">
    <div class="message-content">ありがとうございます。</div>
</li>''', impl.render_messages(messages, current_userid=2))



if __name__ == '__main__':
    unittest.main()
