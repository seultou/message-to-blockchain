import importlib
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    module = sys.argv[1:][0]
    adapter = getattr(
            importlib.import_module(
                'library.message.adapter.' + module + '.' + module
            ),
            module
        )()
    adapter.load_config()

    try:
        adapter.connect()
    except Exception as e:
        print(e)
        exit(0)

    adapter.get_contents()


