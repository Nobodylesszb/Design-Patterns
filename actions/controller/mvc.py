#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
@author: bo
@file: mvc.py
@version:
@time: 2019/09/05
@function： mvc模式
"""

quotes = (' a man is not complete until he is married then he is finished',
          'as i said before,i never repeat myself',
          'behind a successful man is an exhausted women',
          'black holes really sucks')


class QuoteMddel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as e:
            value = 'NOT FOUND'
        return value


class QuoteTerminalView:
    def show(self, quote):
        print('and the quota is "{}"'.format(quote))

    def error(self, msg):
        print('error:{}'.format(msg))

    def select_quote(self):
        return input('which quote number would you like to see')


class QuoteTerminalController:
    def __int__(self):
        self.model = QuoteMddel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error('incorrect index "{}" '.format(n))
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
