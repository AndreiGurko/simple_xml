from typing import Optional, List


class BaseTag:
    def __init__(self, name: str = 'tag', attrs: list = None, nested_tags: list = None):
        self._name = name
        self._root = False
        self._attrs = attrs if attrs else []
        self._nested_tags = nested_tags if nested_tags else []

    def change_name(self, new_name: str):
        self._name = new_name

    def change_attr_name(self, old_attr_name: str, new_attr_name: str):
        for attr in self._attrs:
            # TODO: create a separate method
            if attr.get_attribute_name() == old_attr_name:
                attr.set_attribute_name(new_attr_name)

    def change_attr_value(self, attr_name: str, attr_value: str):
        for attr in self._attrs:
            if attr.get_attribute_name() == attr_name:
                attr.set_attribute_value(attr_value)

    def add_new_attr(self, attr_name, attr_value):
        self._attrs.append(TagAttribute(attr_name, attr_value))

    def del_attr(self, attr_name):
        index = None
        for index, attr in enumerate(self._attrs, 0):
            if attr.get_attribute_name() == attr_name:
                break
        if index:
            del self._attrs[index]


class TagAttribute:
    def __init__(self, name='', value=''):
        self._name = name
        self._value = value

    def get_attribute_name(self):
        return self._name

    def get_attribute_value(self):
        return self._value

    def set_attribute_name(self, new_name):
        self._name = new_name

    def set_attribute_value(self, new_value):
        self._value = new_value
