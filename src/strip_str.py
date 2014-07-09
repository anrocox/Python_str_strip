#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

In python how to remove one or more characters leading and trailing of a
string?

En python ¿como remover uno o varios caracteres del inicio y fin del string?
'''

#create a str
s = '__hello world__'
print(s)

#generates a copy of the string with the leading and trailing characters
#removed.
s_new = s.strip('_')
print(s_new)

#create a str
s = '    hello world     '
print(s)

#if the character is not defined by defaults to removing whitespace ( \t\n\r)
s_new = s.strip()
print(s_new)
