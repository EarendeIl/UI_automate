# UI_automate Python+Pytest+Allure
this is a UI_automate
# 一、配置环境
# 1、安装 Pytest：可以使用 pip 命令进行安装：pip install pytest
# 2、安装 Allure-Pytest 插件：使用 pip 命令进行安装：pip install allure-pytest
# 3、allure需要依赖Java环境，因此需要先安装Java环境  https://www.oracle.com/java/technologies/downloads/
# 4、allure下载，配置环境变量，将allure的bin目录地址放到环境变量的path值里面 https://github.com/allure-framework/allure2/releases
# 5、安装环境后需要配置java环境（系统变量）
# 新建变量名：JAVA_HOME
# 变量值：C:\Program Files (x86)\Java\jdk1.8.0_91 // 要根据自己的实际路径配置
# 新建变量名：CLASSPATH
# 变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar; //记得前面有个"."
# 变量名：Path
# 变量值：%JAVA_HOME%\bin  %JAVA_HOME%\jre\bin;
#  验证JAVA环境是否配置成功，cmd输入JAVA和JAVAC         

# 二、编写用例规则
# 函数命名规则：Pytest 默认将以 "test_" 开头的函数识别为测试用例。例如，**`test_function()`** 将被视为测试用例函数。
# 类命名规则：如果使用了类来组织测试用例，Pytest 默认将以 "Test" 开头的类识别为测试类，并且类中的以 "test_" 开头的方法被识别为测试用例。例如，**`class TestCalculator`** 中的 **`test_add()`** 方法将被视为测试用例。
# 文件命名规则：以 "test_" 开头或以 "_test" 结尾的 Python 文件被认为是测试用例文件。例如，**`test_example.py`** 或 **`example_test.py`**。
