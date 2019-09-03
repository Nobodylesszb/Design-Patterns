import json
import xml.etree.ElementTree as etree
class JsonConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parse_data(self):
        return self.data


class XmlConnector:
    def __init__(self,filepath):
        self.tree = etree.parse(filepath)

    @property
    def parse_data(self):
        return self.tree


def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JsonConnector

    elif filepath.endswith('xml'):
        connector = XmlConnector

    else:
        raise ValueError('conot connect to {}'.format(filepath))

    return connector(filepath)