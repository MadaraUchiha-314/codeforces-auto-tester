# codeforces-auto-tester

A simple tool to help you save time during a codeforces contest.

Given a contest number it fetches all the testcases and expected output for it. For each problem a new folder is created with sub-folders input/ and output/ which contain the example inputs and outputs respectively.

Ask it to test and it will run the program on the sample inputs and check whether your output matches the expected output.

**NOTE : You can add your own test cases into the folders and that will also be tested happily.**

**Bonus :** Keep your template code as `template.cpp` in the same folder as `main.py` and it will automatically populate your template for every problem.

## See it work
- Download or Clone this repository
- Identify a codeforeces contest number (Need not be a current contest) Ex. 703
- To fetch testcases type : `python main.py fetch 703`
- To test your code for a problem (say A)  : `python main.py test A`

## Dependencies
- [Beautiful Soup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## TODO
- [x] Create basic POC for C/C++ code
- [ ] Add support for Java and Python
- [ ] Create a command line tool for Mac and Linux
