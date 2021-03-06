#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from kotodama import kotodama
from pyknp import Juman

class TestKotodama(unittest.TestCase):

    def test_type(self):
        
        # str + set
        self.assertEqual(kotodama.transformVerb("過ごす",{"過去"}), '過ごした')

        # non-str + set
        with self.assertRaises(TypeError):
            message = kotodama.transformVerb(1,{"過去"})

        # str + non-set
        with self.assertRaises(TypeError):
            message = kotodama.transformVerb("過ごす",None)

        # str + list
        self.assertEqual(kotodama.transformVerb("過ごす",["過去"]), '過ごした')


    def test_argument(self):
        # first argument
        with self.assertRaises(KeyError):
            message = kotodama.transformVerb("ほげほげ",{"過去"})

        # second argument
        self.assertEqual(kotodama.transformVerb("過ごす",set()), '過ごす')

        with self.assertWarns(UserWarning):
        	self.assertEqual(kotodama.transformVerb("過ごす",{"ふがふが"}), '過ごす')

    def test_algorithm(self):

        # verb
        self.assertEqual(kotodama.transformVerb("過ごす",{"過去"}), '過ごした')
        
        # adjective
        self.assertEqual(kotodama.transformVerb("楽しい",{"過去"}), '楽しかった')

    def test_unknown_word(self):

        # disable_error実行前はエラーが発生する
        with self.assertRaises(KeyError):
            message = kotodama.transformVerb("嫌いだ",{"過去"})

        kotodama.disableError(Juman())

        # print(kotodama.transformVerb("嫌いだ",set()))
        self.assertEqual(kotodama.transformVerb("嫌いだ",set("過去")), '嫌いだ')




if __name__ == '__main__':
    unittest.main()