### Autotests and framework for 'Save Search' and 'Update Search' feature of the Planet Explorer.

### Setup

 1. Cloning the repository:

    ```shell
    git clone https://github.com/spektormixa/planet_test.git
    ```

2. Installing all the dependencies:

    ```shell
    cd path/to/selenium_python_tests
    pip install -r requirements.txt
    ```

3.  Optional: Installing all the dependencies separately:

    ```shell
    Install python 3.x
    https://www.python.org/downloads/
    
    Install Selenium WebDriver
    pip install selenium
    
    Download and add Chromedriver. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.
    For this implementation chromedriver located in /resources directory
    https://chromedriver.chromium.org/downloads
    
    Install PyTest
    pip install -U pytest
    
    Install Pytest-Check (used for soft-assertions)
    pip install -U pytest-check 2.1.2
    ```


Usage
=

 - cd properties
 - add your username, password and base URL to the configuration file
 - cd tests
 - pytest


Environment
=
- Python 3.9.6
- ChromeDriver 109.0.5414.74
- Selenium WebDriver version 4.8.0
- pytest version 7.2.1
- pytest-check 2.1.2
