How to perform unittesting in python:
-------------------------------------

- module name: unittest (predefine in python)
- class name: TestCase
- instance methods: contains 3 instance method

1. setUp() -->open browser , database connectivity
2. test()
3. tearDown() --> close connection,close browser

4. ### setUpClass(cls)
   - for all test method setUPClass will execute only one

5. ### tearDownClass(cls)
    - tearDownClass(cls) will execute only once
    - these two method are class level methods

### manual testing --- 
    - google search functionality (manually use application and after that use Excel shell )
    - test no , testing steps, expected Result, original result, status
### Automation Testing ---
    - Selenium(automation), QTP(these day gone ), Load Runner( performance automation),epl,self
    - python/java/ruby script program to perform these activities automatically

### selenium
> pip install selenium
> selenium: package
> webdriver: module 
> webdriver -> which can used to test web-application functionality
> webdriver module contains several classes and functions to test functionality of web application

***website : seleniumhq.org***
https://www.selenium.dev/documentation/webdriver/

1. driver.get() --> to open specified url
2. driver.maximize_window()
3. driver.current_url
4. driver.title
5. driver.refresh() / driver.get(driver.current_url) -> both are for refresh
6. driver.back() --> Goes one step backward in the browser history
7. driver.forward() --> Hoes one step forward in the browser history
8. driver.close() --> To close current window
9. driver.quit() --> to close associated windows

search bar,button link all are call web element

Q. How to locate web elements:
-----------------------------
`driver.find_element(By.ID,'id')
driver.find_element(By.NAME,'name')
driver.find_element(By.XPATH,xpath)
driver.find_element(By.LINK_TEXT,'txt') //to find element between a tage <a>abc</a>
driver.find_element(By.CSS_SELECTOR,'css')`
etc

Unit testing api
----------------

module: unittesting
class: TestCase
instance methods:
   setUp() --> Before every test method
   test_method()
   tearDown() --> After every test method
class methods:
   setUpClass() --> before executing all test method of a TestCase Class
   tearDownClass() --> after executing all test method of a TestCase class

- TestSuite --> Collection of testcases
  - By using unittest framework we can execute a group of test cases which nothing test suite.

- compulsory all test class method will execute in alphabetical order
- it the biggest limitation is that it is not follow top to bottom approach

Limitation Of unittesting:
--------------------------
1. Test result will be display to console only and it is not possible to generate reports
2. unittest framework always execute test methods in alphabetical order only, and it is not possible to customize execution order
3. As the part of batch execution(TestSuite), all test methods from the specified TestCase classes will be executed, and it is not possible to specify particular methods.
4. In unittesting only limited setUp and tearDown methods are available.
5. If we want to perform any activity before executing testsuite and after executing testsuite, unittest framework does not define any methods.


> To overcome more advance framework which is pytest 

PyTest Framework:
-----------------
Advanced version of unittest framework
built on top of unittest framework

> pip install pytest

Pytest Naming Rules:
---------------------------
1. File Name should start or end with 'test'
   - test_google_search.py
   - google_search_test.py
2. Class Name should start with 'Test'
   - TestGoogleSearch.py
   - TestCaseDemo
3. test method name should start with 'test_'
   - test_method1()
   - test_method2()

Q. How to run test scripts
> py.test
> it execute all those scripts prest in the folder
> to run a particular test script py.test filename

By default, pytest won't test and won't display print statement on console
`-s ` to display print statement in other languages like java `-v` used for verbose output
`py.test -s filename` -> pretreatment out we can see
`py.test -s -v filename` -> every detail will show 

-s ==> meant for print statement output
-v ==> meant for verbose

pytest: there are no setUp(), tearDown(), setUpClass() and tearDownClass()

Q How to implement setUp() method in pytest:
----------------------------------------------

By using some decorator

@pytest.fixture() -> to implement setup machina
we can implement setUp() by using `@pytest.fixture()`
decorator 

How to implement teatDown() machanism
-------------------------------------
@pytest.fixture() ==> meant for setUp mechanism
@pytest.yield_fixture() ==> meant for both setUp and tearDown
`
@pytest.yield_fixture()
def ma():
   setUp activity
   yield
   tearDown activity`

@pytest.yield_fixture() is deprecated use @pytest.fixture() instead with yield

How to implement setUpClass() and tearDownClass() in pytest:
--------------------------------------------------------------
@pytest.yield_fixture(scope='module')

How to implement setUp,tearDown and setUpClass,tearDownClass functionality simultaneously in pytest:
----------------------------------------------------------------------------------------------------
>link

conftest.py
-----------
code re-usability
common setUp and tearDown activities, we have to define in this file 
automatically available for all test scripts

Various possible ways to run pytest scripts:
--------------------------------------------
1. py.test -v -s
   - to run all methods present in all test scripts of current working directory
2. py.test -v -s test.py
   - to run all test methods of a particular test scripts
3. py.test -v -s test.py test1.py
   - to run multiple test scripts
4. py.test -v -s test.py test1.py::test_method
   - To run a particular test method

it will follow top to down approach

How to customize order of tests in pytest
-----------------------------------------
we have to install module pytest-ordering

`@pytest.mark.run(order=n)`
in unittesting this type of facility not define

How to genrate test results in html form:
-----------------------------------------

pip install pytest-html

pytest -v -s test9.py --html=result.html









