from xml_string_parser import *
from collections import deque


class XmlStringBuilder:
    def build_tags(self, tags_data_list):
        tag_stack = deque()
        root_upper_strings = []
        for tag_data in tags_data_list:
            if tag_data.startwith(ROOT_UPPER_TAG_BEGIN) and tag_data.endwith(ROOT_UPPER_TAG_END):
                root_upper_strings.append(tag_data)
                continue
            for index, symbol in enumerate(tag_data, 0):
                pass


class Stack:
    def __init__(self):
        self._storage = []

    def push(self, item):
        self._storage.append(item)

    def get_peak(self):
        item = None
        try:
            item = self._storage[-1]
        except IndexError:
            pass
        return None

    def pop(self):
        item = None
        try:
            item = self._storage.pop(-1)
        except IndexError:
            pass
        return item
