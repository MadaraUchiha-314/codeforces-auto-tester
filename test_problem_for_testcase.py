from subprocess import Popen,PIPE
import filecmp
import os
import sys

def test_problem_for_testcase (problem_name,lang,test_case_no,typ="normal") :

	test_file_name = "in"+test_case_no
	output_file_name = "out"+test_case_no
	base_path = problem_name+"/"

	ac = False

	if lang == "cpp" :

		r = os.system ("g++ -std=c++11 -w "+base_path+problem_name+"."+lang)

		if r != 0 :
			print "--------- Compilation Error ---------"
			sys.exit()
			

		s = os.system ("./a.out <"+base_path+"input/"+test_file_name+" >temp_output")

		if s != 0 :
			print "--------- Runtime Error ---------"
			sys.exit()
			

		# ac = filecmp.cmp(base_path+"output/out"+test_case_no,"temp_output")

		# Above Line to be used for strict comparision
		# Below line to be used for non-strict comparision

		with open (base_path+"output/out"+test_case_no,'r') as out_file :
			with open ("temp_output",'r') as temp_output_file :

				actual_output = out_file.read()
				your_output = temp_output_file.read()

				p = ''.join(actual_output.split())
				q = ''.join(your_output.split())

				if p == q :
					ac = True

		if ac :
			print "AC for test case : " + test_case_no
			
		elif typ == "multiple-answers" :
			print "--------- Input ---------"

			with open (base_path+"input/"+test_file_name,'r') as inp :
				print inp.read()

			print "--------- Your Output ---------"

			with open ("temp_output",'r') as your_output :
				print your_output.read()

			print "--------- Sample Output ---------"

			with open (base_path+"output/"+output_file_name,'r') as out :
				print out.read()

		else :
			print "WA for test case : " + test_case_no
			print "--------- Input ---------"

			with open (base_path+"input/"+test_file_name,'r') as inp :
				print inp.read()

			print "--------- Your Output ---------"

			with open ("temp_output",'r') as your_output :
				print your_output.read()

			print "--------- Expected Output ---------"

			with open (base_path+"output/"+output_file_name,'r') as out :
				print out.read()

		if os.path.exists("temp_output") :
				os.remove("temp_output")

		if os.path.exists("a.out") :
			os.remove("a.out")
