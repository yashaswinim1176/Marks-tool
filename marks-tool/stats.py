"""Statistics helpers"""

def average(marks):
	return sum(marks) / len(marks)
def highest(marks):
	return max(marks)
def lowest(marks):
	return min(marks)

def pass_count(marks, pass_mark):
# TODO: read pass_mark from .env instead of the caller
	return len([mark for mark in marks if mark >= pass_mark])
	
