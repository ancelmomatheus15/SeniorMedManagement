import logging
import os
import threading

import pyzenbo

host = '192.168.0.214'
logging.basicConfig(level=logging.INFO)


def file_transfer_test():
    with pyzenbo.connect(host) as sdk:
        event = threading.Event()

        def job(target_file):
            print('target_file', target_file)
            print('file_transmission', sdk.media.file_transmission(target_file))
            event.set()

        def file_transfer_test_on_result(**kwargs):
            print('on_result', kwargs)
            if kwargs.get('cmd') == 786433 and kwargs.get('result') is not None:
                file = kwargs.get('result').get('file')
                t = threading.Thread(target=job, args=(os.path.basename(file),))
                t.start()

        sdk.on_result_callback = file_transfer_test_on_result
        sdk.media.take_picture()
        event.wait(20)


if __name__ == '__main__':
    file_transfer_test()
