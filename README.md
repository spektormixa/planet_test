### Autotests and framework for the Planet Explorer.

### Setup

 1. Cloning the repository:

    ```shell
    git clone https://github.com/spektormixa/planet_test.git
    ```

## Setup work environment using IDE PyCharm
* clone the code
* open with Pycharm
* venv and dependencies will automatically setup and installed with notified pop-ups


2. Optional: Installing all the dependencies all at once:

    ```shell
    cd path/to/tests
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


### Usage
```shell
 - cd properties
 - add your username, password and base URL to the configuration file
 - cd tests
 - pytest
 ```


### Environment

- Python 3.9.6
- ChromeDriver 109.0.5414.74
- Selenium WebDriver version 4.8.0
- pytest version 7.2.1
- pytest-check 2.1.2
