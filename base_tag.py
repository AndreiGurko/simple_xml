class BaseTag:
    def __init__(self, name: str = 'tag', attrs: dict = None, nested_tags: list = None):
        self._name = name
        self._attrs = attrs if attrs else {}
        self._nested_tags = nested_tags if nested_tags else []

    def change_name(self, new_name: str):
        self._name = new_name

    def change_attr_name(self, old_attr_name: str, new_attr_name: str):
        if old_attr_name in self._attrs:
            attr_value = self._attrs.pop(old_attr_name)
            self._attrs[new_attr_name] = attr_value

    def add_new_attr(self, attr_name, attr_value):
        self._attrs[attr_name] = attr_value

    def del_attr(self, attr_name):
        del self._attrs[attr_name]
