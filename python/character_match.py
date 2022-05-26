# Don't forget to run your tests!

from operator import truediv


def is_character_match(string1, string2):
	srtdStr1="".join(sorted(string1.lower()))
	srtdStr2="".join(sorted(string2.lower()))
	
	if srtdStr1.strip()==srtdStr2.strip():
		return True
	else:
		return False	

