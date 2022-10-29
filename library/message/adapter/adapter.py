import yaml
import os

class Adapter(object):
    config: dict = {}
    conn: object = None

    def load_config(self):
        with open('library/message/adapter/' + type(self).__name__ + '/config.yaml', "r") as stream:
            try:
                self.config = yaml.safe_load(stream)
            except FileExistsError | FileNotFoundError:
                return None

    def get_contents(self):
        pass
        # print("Adapter.get_contents")

    def return_status(self):
        pass
        # print("Adapter.return_status")
