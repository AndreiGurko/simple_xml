from base_tag import *


class XmlStringBuilder:
    def build_tags(self, tags_data_list):
        tags_storage = Stack()
        root_upper_strings = []
        for tag_data in tags_data_list:
            if tag_data.startswith(ROOT_UPPER_TAG_BEGIN) and tag_data.endswith(ROOT_UPPER_TAG_END):
                root_upper_strings.append(tag_data)
                continue
            if tag_data.startswith(BEGIN_CLOSED_TAG):
                previous_tag = tags_storage.pop()
                if not tags_storage.get_peak():
                    previous_tag.add_root_upper_string(root_upper_strings)
                    print(f'complete. Base Tag {previous_tag}')
                    return previous_tag
                else:
                    peak = tags_storage.get_peak()
                    peak.add_new_nested_tag(previous_tag)
            elif tag_data.startswith(BEGIN_TAG) and not tag_data.endswith(END_CLOSED_TAG):
                # extract tag name
                tag_name = tag_data.split('>')[0][1:].split(' ')[0]
                tag_content = tag_data.split('>')[1]
                tag_attrs = self._build_tag_attrs(tag_data)
                tags_storage.push(BaseTag(name=tag_name, content=tag_content, attrs=tag_attrs))
            elif tag_data.startswith(BEGIN_TAG) and tag_data.endswith(END_CLOSED_TAG):
                # extract tag name
                tag_name = tag_data.split('>')[0][1:].split(' ')[0]
                tag_content = tag_data.split('>')[1]
                tag_attrs = self._build_tag_attrs(tag_data)
                parent_tag = tags_storage.get_peak()
                parent_tag.add_new_nested_tag(BaseTag(name=tag_name, content=tag_content, attrs=tag_attrs))

    def _extract_tag_attrs(self, tag_data):
        #TODO: need fix bugs
        attrs = []
        start_attr = False
        check_attr_value = False
        attr_value_string = False
        attr_value_number = False
        # if attr value is string we should check type of quote. e.g: 'Yaroslavl' and "Yaroslavl'"
        quote_mark = None
        attr = ''
        for item in tag_data:
            if item == ">":
                if attr:
                    if attr[-1] == '/':
                        attr = attr[:-1]
                    attrs.append(attr)
            if item == ' ' and not start_attr:
                start_attr = True
                continue
            if start_attr:
                if attr_value_number and item == ' ':
                    attrs.append(attr)
                    attr = ''
                    attr_value_number = False
                    continue
                if attr_value_string and item == "'" or attr_value_string and item == "\"":
                    if quote_mark == item:
                        attr += item
                        attrs.append(attr)
                        attr_value_string = False
                        attr = ''
                        start_attr = False
                        continue
                    else:
                        attr += item
                        continue

                if check_attr_value:
                    if item == "'" or item == "\"":
                        check_attr_value = False
                        attr_value_string = True
                        quote_mark = item
                        attr += item
                        continue
                    elif not item.isalpha():
                        attr_value_number = True
                        attr += item
                        continue

                if item == '=':
                    attr += item
                    check_attr_value = True
                    continue
                attr += item
        return attrs

    def _build_tag_attrs(self, tag_data):
        tag_attrs = []
        extracted_tag_attrs = self._extract_tag_attrs(tag_data)
        for tag_attr in extracted_tag_attrs:
            attr_name, attr_value = self._split_tag_attr_by_name_and_value(tag_attr)
            tag_attr_object = self._create_tag_attr_obj(attr_name, attr_value)
            if tag_attr_object:
                tag_attrs.append(tag_attr_object)
        return tag_attrs

    def _split_tag_attr_by_name_and_value(self, tag_attr):
        attr_name, attr_value = '', ''
        if tag_attr:
            try:
                attr_name, attr_value = tag_attr.split('=')
            except Exception:
                pass
        return attr_name, attr_value

    def _create_tag_attr_obj(self, attr_name, attr_value):
        tag_attr_obj = None
        # TODO: should attr_value be with value all time?
        if attr_name:
            tag_attr_obj = TagAttribute(name=attr_name, value=attr_value)
        return tag_attr_obj


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
        return item

    def pop(self):
        item = None
        try:
            item = self._storage.pop(-1)
        except IndexError:
            pass
        return item
