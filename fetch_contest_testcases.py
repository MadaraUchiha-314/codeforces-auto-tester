from bs4 import BeautifulSoup
import urllib
import string
import retrive_test_cases

def fetch_contest_testcases (contest_number) :

	contest_url = "http://codeforces.com/contest/"+contest_number

	response = urllib.urlopen (contest_url)
	html = response.read ()

	soup = BeautifulSoup(html, 'html.parser')

	problems = soup.findAll ("select",{"name":"submittedProblemIndex"})

	number_of_problems = 0
	for ele in problems[0] :
		if ele != '\n' :
			number_of_problems += 1

	number_of_problems -= 1

	problem_names = list(string.ascii_uppercase)

	for i in xrange(number_of_problems) :
		retrive_test_cases.retrive_test_cases(contest_url+"/problem/"+str(problem_names[i]))
