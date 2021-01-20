#!user/bin/python

import re
import os
import sys
import subprocess
from termcolor import colored

file_path = raw_input("please enter file path : ")


# command execution

print colored("Sink that can lead to command execution","red")

pattern = re.compile("exec|system|shell_exec|popen")
for i, line in enumerate(open(file)):
		for match in re.finditer(pattern, line):

			print 'found on line %s: %s' % (i+1, match.group())

# Code execution

print colored("Sink that can lead to code execution","red")

pattern1 = re.compile("eval|assert|preg_replace('/.*/e')|create_function|include|include_once|require|require_once")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern1, line):

                print 'found on line %s: %s' % (i+1, match.group())
#Call Back Function

print colored("Call back Functions- Another way to execute functions","red")

pattern2 = re.compile("ob_start|array_diff_uassoc|array_diff_ukey|array_filter|array_intersect_uassoc|array_intersect_ukey|array_map|array_reduce|array_udiff_assoc|array_udiff_uassoc|array_udiff|array_uintersect_assoc|array_uintersect_uassoc|array_walk_recursive|array_walk|set_error_handler")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern2, line):
                print 'found on line %s: %s' % (i+1, match.group())


# Information Disclosure

print colored("These function may lead to information disclosure","red")

pattern3 = re.compile("phpinfo|posix_mkfifo|posix_getlogin|posix_ttyname|getenv|disk_total_space|disk_free_space|getmygid|getmyinode|getmyuid")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern3, line):
                print 'found on line %s: %s' % (i+1, match.group())



#FileSystem Functions

print colored("filesystems function may lead to vulns","red")

pattern4 = re.compile("fopen|tmpfile|bzopen|gzopen|chgrp|chmod|chown|ftp_get|readfile|readlink|hash_hmac_file")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern4, line):
                print 'found on line %s: %s' % (i+1, match.group())


# Miscellaneous

print colored("Some other function which doesnt falls in any category but may lead to vulns","red")

pattern5 = re.compile("extract|parse_str|proc_nice|proc_terminate|fsockopen|posix")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern5, line):
                print 'found on line %s: %s' % (i+1, match.group())



# Check for secure and httponly flag and password hash

print colored("To check for httponly flag and algorithm for password hashing","red")

pattern6 = re.compile("setcookie|password_hash|hmac")

for i, line in enumerate(open(file_path)):
        for match in re.finditer(pattern6, line):
                print 'found on line %s: %s' % (i+1, match.group())



#-------------------------------END
