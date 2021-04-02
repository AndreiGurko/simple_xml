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
                # TODO: add extract tag attrs
                tags_storage.push(BaseTag(name=tag_name, content=tag_content))
            elif tag_data.startswith(BEGIN_TAG) and tag_data.endswith(END_CLOSED_TAG):
                # extract tag name
                tag_name = tag_data.split('>')[0][1:].split(' ')[0]
                tag_content = tag_data.split('>')[1]
                # TODO: add extract tag attrs
                parent_tag = tags_storage.get_peak()
                parent_tag.add_new_nested_tag(BaseTag(name=tag_name, content=tag_content))


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
