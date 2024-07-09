import pytest
import os

if __name__ == '__main__':
    pytest.main(["--alluredir=./allure_result", "--clean-alluredir"])
    os.system("allure generate ./allure_result -o ./allure_report --clean")
