# jssp-ga

Implementation of a genetic algorithm designed to solve the Job Shop Scheduling Problem. Also included is a Web application prototype to use the GA from a Web browser. This is the final project for my undergraduate thesis at Universidad Nacional de Colombia.

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
This project is released under the [MIT License](https://choosealicense.com/licenses/mit/).

## References

[1] J. W. Herrmann, «A History of Production Scheduling», in _Handbook of Production 
Scheduling_, J. W. Herrmann, Ed. Boston, MA: Springer US, 2006, pp. 1-22. doi: 10.1007/0-387-
33117-4_1.  
[2] M. R. Garey, D. S. Johnson, y R. Sethi, «The Complexity of Flowshop and Jobshop 
Scheduling», _Math. Oper. Res._, vol. 1, n.o 2, pp. 117-129, may 1976, doi: 10.1287/moor.1.2.117.  
[3] B. Çaliş y S. Bulkan, «A research survey: review of AI solution strategies of job shop 
scheduling problem», _J. Intell. Manuf._, vol. 26, n.o 5, pp. 961-973, oct. 2015, doi: 
10.1007/s10845-013-0837-8.  
[4] E. Taillard, «Benchmarks for basic scheduling problems», _Eur. J. Oper. Res._, vol. 64, n.o
2, pp. 278-285, ene. 1993, doi: 10.1016/0377-2217(93)90182-M.  
[5] «Flexible Job Shop Problem». https://people.idsia.ch//~monaldo/fjsp.html (accessed 
sep. 06, 2021).  
[6] «OR-LIBRARY». http://people.brunel.ac.uk/~mastjjb/jeb/info.html (accessed sep. 08, 
2021).  
[7] M. Mastrolilli y L. M. Gambardella, «Effective neighbourhood functions for the flexible 
job shop problem», _J. Sched._, vol. 3, n.o 1, pp. 3-20, 2000, doi: 10.1002/(SICI)1099-
1425(200001/02)3:1<3::AID-JOS32>3.0.CO;2-Y.  
[8] D. L. Poole _et al._, _Computational Intelligence: A Logical Approach_. Oxford University 
Press, 1998.  
[9] G. Tejada Muñoz, «Controlador PID con algoritmos genéticos de números reales», _Ind. 
Data_, vol. 22, n.o 2, 2019, Accessed: sep. 07, 2021. [Online]. Available: 
https://www.redalyc.org/journal/816/81662532017/  
[10] «OR-Tools | Google Developers». https://developers.google.com/optimization 
(accessed sep. 07, 2021).  
[11] «LEKIN -- Scheduling System». https://web-static.stern.nyu.edu/om/software/lekin/ 
(accessed sep. 07, 2021).  
[12] «JobBOSS2», _Shoptech The E2 Shop System_. https://www.shoptech.com/jobboss2/ 
(accessed sep. 07, 2021).  
[13] R. Nakano y T. Yamada, «Conventional Genetic Algorithm for Job Shop Problems.», in 
_Proceedings of the 4th International Conference on Genetic Algorithms_, San Diego, 1991, vol. 91, 
pp. 474-479.
[14] B. M. Ombuki y M. Ventresca, «Local Search Genetic Algorithms for the Job Shop 
Scheduling Problem», _Appl. Intell._, vol. 21, n.o 1, pp. 99-109, jul. 2004, doi: 
10.1023/B:APIN.0000027769.48098.91.  
[15] T. Yamada y R. Nakano, «Job shop scheduling», _IEE Control Eng. Ser._, pp. 134-134, 
1997.  
[16] M. S. Viana, O. Morandin Junior, y R. C. Contreras, «A Modified Genetic Algorithm with 
Local Search Strategies and Multi-Crossover Operator for Job Shop Scheduling Problem», 
_Sensors_, vol. 20, n.o 18, p. 5440, sep. 2020, doi: 10.3390/s20185440.  
[17] «The Python Standard Library — Python 3.9.7 documentation». 
https://docs.python.org/3/library/index.html (accessed sep. 08, 2021).
