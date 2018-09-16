import os
import json
from operator import itemgetter
import xml.etree.ElementTree as ET

file_json = 'newsafr.json'
file_xml = 'newsafr.xml'

path_to_file_json = os.path.join('files', file_json)
path_to_file_xml = os.path.join('files', file_xml)

class CalculatorWords:

    def __init__(self):
        self.dict_long_words = {}
        self.result = []

    def find_long_words(self, list_words):
        if list_words:
            for word in list_words:
                if len(word) > 6:
                    self.__calc_count_word(word)

    def __calc_count_word(self, word):
        if word not in self.dict_long_words.keys():
            self.dict_long_words[word] = 1
        else:
            self.dict_long_words[word] += 1

    def show_top_ten_words(self):
        # что такое itemgetter(1) неизвестно, но ведь работает, спасибо stackoverflow
        result_sort = sorted(self.dict_long_words.items(), key=itemgetter(1), reverse=True)
        index_word = 1
        for k,v in result_sort[:10]:
            print(f'word \'{k}\' - {v} times')
            index_word += 1

print('\njson file: ', path_to_file_json, '\n' )

calculator_json = CalculatorWords()

with open(path_to_file_json, 'r', encoding='UTF-8') as f:
    json_data = json.load(f)
    for item in json_data['rss']['channel']['items']:
        words = item['description'].split(' ')
        calculator_json.find_long_words(words)

calculator_json.show_top_ten_words()


print('\nxml file: ', path_to_file_xml, '\n' )

tree_xml = ET.parse(path_to_file_xml)

xml_items = tree_xml.findall('channel/item')

calculator_xml = CalculatorWords()

for item in xml_items:
    description = item.find('description').text
    words = description.split(' ')
    calculator_xml.find_long_words(words)

calculator_xml.show_top_ten_words()

