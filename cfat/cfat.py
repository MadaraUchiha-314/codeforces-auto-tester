from .fetch_contest_testcases import fetch_contest_testcases
from .test_problem import test_problem
import sys

__version__ = "0.1.0"

def main () :

	arg = sys.argv

	if len (arg) < 2 :
		print "Enter arguments like fetch or test"
		sys.exit()
	else :
		if len (arg) == 3 and arg[1] == "fetch" :
			fetch_contest_testcases (arg[2])

		elif len (arg) == 3 and arg[1] == "test" :
			test_problem (arg[2])

		elif len (arg) == 4 and arg[1] == "test" and arg[3] == "multiple" :
			test_problem(arg[2],"cpp","multiple-answers")
			
		else :
			print "Could not parse"
			sys.exit()
			