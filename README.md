# API automation tests

This project is used to run the Api test cases and generate the test result.

## Installation

Use the package manager [pip](https://pip.pypa.ffio/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Used technologies
- Python
- Allure

## How to run
### To run and generate report use this command: 
```
pytest --html=report.html --self-contained-html --fromTerminal="from_terminal"
```
### To run and generate allure report use these commands:
<a href="https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/" target="_blank">Click here</a>
to download last version from allure then add the bin path to the environment variable

Execute the test:
```
pytest --fromTerminal="from_terminal" --alluredir=allure-report/.
```
then open the allure report
```commandline
allure serve allure-report/.
```