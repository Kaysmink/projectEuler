# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:35:00 2021

@author: kaysm
"""

numbers = [number for number in range(2, 1000000000) if str(number) == str(number)[::-1]]
