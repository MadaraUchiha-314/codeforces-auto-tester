import os
from .test_problem_for_testcase import test_problem_for_testcase


def test_problem (problem_name,lang="cpp",typ="normal"):
	number_of_tests = len([name for name in os.listdir(problem_name+"/input") if os.path.isfile(problem_name+"/input/"+name)])

	for i in xrange (number_of_tests):
		test_problem_for_testcase(problem_name,lang,str(i),typ)
