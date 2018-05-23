#yyyy-mm-dd hh:mm:ss
def isdue(due):
	dateNtime = due.split(' ')
	if len(dateNtime) != 2:
		return False
	date = dateNtime[0].split('-')
	time = dateNtime[1].split(':')
	if len(dateNtime) != 2 or len(date) != 3 or len(time) != 3:
		return False
	for key in date:
		if key.isdigit() == 0 :
			return False
	for key in time:
		if key.isdigit() == 0:
			return False
	return (1000<=int(date[0]) and int(date[0])<=9999) and (1<=int(date[1]) and int(date[1])<=12) and (1<=int(date[2]) and int(date[2])<=31) and (0<=int(time[0]) and int(time[0])<=24) and (0<=int(time[1]) and int(time[1])<=60) and (0<=int(time[2]) and int(time[2])<=60)
