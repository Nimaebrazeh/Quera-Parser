#!/usr/bin/env python
# -*- coding: utf-8 -*-

from QParser import QParser
import sys

PY_VER = sys.version_info[0]

if __name__ == '__main__':

#### Enter complete url of problem. e.g. https://quera.ir/problemset/contest/3537/ 

	if PY_VER > 2:
		link = input("Enter complete url of problem : ")
	else:
		link = raw_input("Enter complete url of problem : ")

#### Create an object of QParser class

	parser = QParser(link)

#### Get html data from quera

    # data = parser.get_html_data()


#### Get problem name of specefic link

    # data = parser.get_problem_name()


#### Get sample inputs of problem

    # data = parser.get_sample_input()


#### Get sample outputs

    # data = parser.get_sample_output()


#### Save sample inputs & outputs to .txt file

	parser.save_to_file()
