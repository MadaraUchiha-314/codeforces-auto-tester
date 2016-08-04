from bs4 import BeautifulSoup
import urllib
import os

# Give an url this function retrives the testcases and expected output for the problem
# Creates a folder with problem name
# Creates sub-folders inputs/ and output/ and places the files there

def retrive_test_cases (problem_url) :

	response = urllib.urlopen (problem_url)

	folder_base = problem_url[-1]+"/"

	if not os.path.exists(folder_base):
		os.makedirs(folder_base)

	if not os.path.exists(folder_base+problem_url[-1]) :
		with open (folder_base+problem_url[-1]+".cpp",'w') as code :
			with open ("template.cpp",'r') as template:
				code.write (template.read())

	html = response.read ()

	soup = BeautifulSoup(html, 'html.parser')

	pre = soup.find_all ('pre')

	if not os.path.exists(folder_base+"input") :
		os.makedirs (folder_base+"input")

	if not os.path.exists(folder_base+"output") :	
		os.makedirs (folder_base+"output")

	i = 0
	for ele in pre :

		data = str(ele)
		data = data.replace ("</pre>","")
		data = data.replace ("<pre>","")
		data = data.replace ("<br/>","\n")

		if i%2 == 0 :
			file_name = folder_base+"input/in"+str(i/2)

			with open (file_name,'w') as inp_file :
				inp_file.write (data)
		else :
			file_name = folder_base+"output/out"+str(i/2)

			with open (file_name,'w') as inp_file :
				inp_file.write (data)

		i += 1
# retrive_test_cases ("http://codeforces.com/contest/700/problem/B")