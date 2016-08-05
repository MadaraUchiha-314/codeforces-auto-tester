# codeforces-auto-tester

A simple tool to help you save time during a codeforces contest.

Given a contest number it fetches all the testcases and expected output for it. For each problem a new folder is created with sub-folders input/ and output/ which contain the example inputs and outputs respectively.

Ask it to test and it will run the program on the sample inputs and check whether your output matches the expected output.

**NOTE : You can add your own test cases into the folders and that will also be tested happily.**

**Bonus :** Keep your template code as `template.cpp` in the same place as your CWD and it will automatically populate your template for every problem.

## See it work
- Download or Clone this repository
- Install Codeforces Auto Tester (cfat) by typing `python setup.py install` (Good to have [pip] (https://pip.pypa.io/en/stable/installing/) install before)
- Identify a codeforeces contest number (Need not be a current contest) **Eg. 703 (Codeforces Round #365 (Div. 2))**
- To fetch testcases type : `cfat fetch 703`
- To test your code for a problem (say A)  : `cfat test A`
- If multiple answers are possible : `cfat test A multiple`

## Dependencies
- [Beautiful Soup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## TODO
- [x] Create basic POC for C/C++ code
- [x] Added support for multiple answers
- [x] Create a command line tool for Mac and Linux
- [ ] Add support for Java and Python
- [ ] Add support for approximate answers (Eg. floating point)
