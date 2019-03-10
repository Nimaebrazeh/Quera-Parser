#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding: utf-8

import os
import sys
import requests

PY_VER = sys.version_info[0]

if PY_VER > 2:
    import urllib as urllib2
else:
    from urllib2 import urlopen

from bs4 import BeautifulSoup

class QParser:

    def __init__(self, link):

        self.link = link + "/"

        self.link = self.link.encode('ascii', 'ignore').decode('ascii')

        self.soup = None

        self.problem_name = None

        self.sample_input = dict()

        self.sample_output = dict()

        self.run()

    def run(self):

        self.check_link()

        self.set_html_data()

        self.set_problem_name()

        self.set_sample_input()

        self.set_sample_output()

    def check_link(self):

        r = requests.head(self.link)

        if r.status_code != 200:

            raise Exception("problem link is not valid!")

    def set_html_data(self):

        if sys.version_info[0] > 2:

            html_page = urllib2.request.urlopen(self.link)

        else:

            html_page = urlopen(self.link)

        self.soup = BeautifulSoup(html_page, 'html.parser')


    def get_html_data(self):

        return self.soup


    def set_problem_name(self):

        self.problem_name = self.soup.find('div', attrs = {'class' : 'ui center aligned fluid container'}).h1.get_text()


    def get_problem_name(self):

        return self.problem_name


    def create_dir(self, dir_name):

        if not os.path.exists(dir_name):

            os.mkdir(dir_name)
            

    def set_sample_input(self):

        data = str(self.soup)

        cnt = 1

        start = 0

        end = data.find("ورودی نمونه")

        while True:

            start = data.find("ورودی نمونه", end, -1)

            if start == -1:
                break

            start = data.find("`", start, -1)

            if start == -1:
                break

            start += 5

            end = data.find("`", start, -1)    

            self.sample_input[str(cnt)] = data[start:end]   

            end += 3

            cnt += 1


    def get_sample_input(self):

        return self.sample_input


    def set_sample_output(self):

        data = str(self.soup)

        cnt = 1

        start = 0

        end = data.find("خروجی نمونه")

        while True:

            start = data.find("خروجی نمونه", end, -1)

            if start == -1:
                break

            start = data.find("`", start, -1)

            if start == -1:
                break

            start += 5

            end = data.find("`", start, -1)

            self.sample_output[str(cnt)] = data[start:end]

            end += 3

            cnt += 1


    def get_sample_output(self):

        return self.sample_output


    def save_to_file(self):

        # Input

        if PY_VER > 2:
            dir_name = "ورودی_" + self.problem_name.replace(" ", "-")
        else:
            dir_name = "ورودی_".decode("utf-8")
            dir_name += self.problem_name.replace(" ", "-")

        self.create_dir(dir_name)

        for key, value in self.sample_input.items():

            file_name = "input" + key + ".txt"

            input_file = dir_name + "/" + file_name

            f = open(input_file, "w")

            f.write(value)

            f.close()

        # Output   

        if PY_VER > 2:
            dir_name = "خروجی_" + self.problem_name.replace(" ", "-")
        else:
            dir_name = "خروجی_".decode("utf-8")
            dir_name += self.problem_name.replace(" ", "-")

        self.create_dir(dir_name)

        for key, value in self.sample_output.items():

            file_name = "output" + key + ".txt"

            input_file = dir_name + "/" + file_name

            f = open(input_file, "w")

            f.write(value)

            f.close()

