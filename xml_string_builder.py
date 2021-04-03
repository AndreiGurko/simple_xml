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
                # TODO: create Attr instance
                tag_attrs = self._extract_tag_atts(tag_data)
                tags_storage.push(BaseTag(name=tag_name, content=tag_content))
            elif tag_data.startswith(BEGIN_TAG) and tag_data.endswith(END_CLOSED_TAG):
                # extract tag name
                tag_name = tag_data.split('>')[0][1:].split(' ')[0]
                tag_content = tag_data.split('>')[1]
                tag_attrs = self._extract_tag_atts(tag_data)
                # TODO: create Attr instance
                parent_tag = tags_storage.get_peak()
                parent_tag.add_new_nested_tag(BaseTag(name=tag_name, content=tag_content))

    def _extract_tag_atts(self, tag_data):
        attrs = []
        start_attr = False
        check_attr_value = False
        attr_value_string = False
        attr_value_number = False
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
                if attr_value_string and item == "'" or item == "\"":
                    attr += item
                    attrs.append(attr)
                    attr_value_string = False
                    attr = ''
                    start_attr = False
                    continue

                if check_attr_value:
                    if item == "'" or item == "\"":
                        check_attr_value = False
                        attr_value_string = True
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
