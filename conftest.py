import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'Helpers'))

def pytest_addoption(parser):
    parser.addoption("--fromTerminal", action="store", default="")

def pytest_configure(config):
    os.environ['fromTerminal'] = config.getoption('--fromTerminal')
