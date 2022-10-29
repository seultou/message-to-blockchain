from library.message.adapter.adapter import Adapter

class ftp(Adapter):
    def __init__(self):
        print('rmq::__init__')

    def connect(self):
        print('rmq::connect')

    def get_contents(self):
        print('rmq::get_contents')

