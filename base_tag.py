from typing import Optional, List

ROOT_UPPER_TAG_BEGIN = "<?"
ROOT_UPPER_TAG_END = "?>"
BEGIN_TAG = "<"
END_TAG = ">"
END_CLOSED_TAG = "/>"
BEGIN_CLOSED_TAG = "</"


class BaseTag:
    def __init__(self, name: str = 'tag', attrs: list = None, content='', nested_tags: list = None):
        self._name = name
        self._root = False
        self._attrs = attrs if attrs else []
        self._content = ''
        self._nested_tags = nested_tags if nested_tags else []
        self._root_upper_string = []

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

    def set_content(self, new_content):
        self._content = new_content

    def get_content(self):
        return self._content

    def add_new_nested_tag(self, nested_tag):
        # TODO: think about order tags
        self._nested_tags.append(nested_tag)

    def add_root_upper_string(self, upper_strings):
        self._root_upper_string.extend(upper_strings)


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
