# codeforces-auto-tester

A simple tool to help you save time during a codeforces contest.

Given a contest number it fetches all the testcases and expected output for it. For each problem a new folder is created with sub-folders input/ and output/ which contain the example inputs and outputs respectively.

Ask it to test and it will run the program on the sample inputs and check whether your output matches the expected output.

**NOTE : You can add your own test cases into the folders and that will also be tested happily.**

## Dependencies
- [Beautiful Soup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## TODO
- [x] Create basic POC for C/C++ code
- [ ] Add support for Java and Python
- [ ] Create a command line tool for Mac and Linux
