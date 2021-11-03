# jssp-ga

Implementation of a genetic algorithm designed to solve the Job Shop Scheduling Problem. Also included is a Web application prototype to use the GA from a Web browser.

## Tech/framework used

Built with `web.py`, `Vue.js`, and `axios`.

## Requirements

* Python 3.9 and `pipenv` should be installed in your system (preferred), or `web.py` should be installed in your Python environment.

## Dependencies

This project only uses `web.py` as its third-party dependency. `web.py` is used to run the Web app prototype as is lightweight and can be used to create Web applications in short time.

## Installation

1. Clone the repository
2. (If you don't have `web.py` installed) Browse into the root folder of the project and setup a Python enviroment running `pipenv install`

## Use

To run the Web app prototype, login into your virtual environment (`pipenv shell`) and run `python app.py` and point your Web browser to `YOUR_IP:8080`. If you want to run instances from the benchmark instances provided, please run `python jssp_ga_command.py`. This terminal script can be run with `PyPy` in order to be magnitudes of order faster than the CPython interpreter.

## License
This project is released under the [MIT license](https://choosealicense.com/licenses/mit/).
