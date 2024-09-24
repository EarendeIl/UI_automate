import time

import pytest
import os

if __name__ == '__main__':
    format_time = format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime()))
    pytest.main(["--alluredir=./report_json", "--clean-alluredir"])
    os.system("allure generate ./report_json -o ./report/{}".format(format_time))
