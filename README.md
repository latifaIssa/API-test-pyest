# API-test-pyest
### To run and generate report use this command: 
```
pytest --html=report.html --self-contained-html --fromTerminal="from_terminal" --alluredir=allure-report/.
```
### To run and generate allure report use these commands: 

```
pytest --fromTerminal="from_terminal" --alluredir=allure-report/.
```
then 
```commandline
allure serve allure-report/.
```