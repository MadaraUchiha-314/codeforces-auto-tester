import fetch_contest_testcases
import test_problem
import sys

if __name__ == "__main__" :

	arg = sys.argv

	if len (arg) < 2 :
		print "Enter arguments like fetch or test"
		sys.exit()
	else :
		if len (arg) == 3 and arg[1] == "fetch" :
			fetch_contest_testcases.fetch_contest_testcases (arg[2])

		elif len (arg) == 3 and arg[1] == "test" :
			test_problem.test_problem (arg[2])

		elif len (arg) == 4 and arg[1] == "test" and arg[3] == "multiple" :
			test_problem.test_problem(arg[2],"cpp","multiple-answers")
			
		else :
			print "Could not parse"
			sys.exit()
			