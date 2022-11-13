import requests 
import feedparser
import sys
from time import sleep
from win10toast import ToastNotifier



def user_input():
	team = str(input("enter team name: "))
	return team

def loadrss(team_name):
	xml_score = feedparser.parse("https://static.cricinfo.com/rss/livescores.xml")
	for entry in xml_score.entries:
		if team_name not in entry.title:
			pass
		else:
			playing_team = entry.description
			return playing_team
			

if __name__ == '__main__':
	
	user_in = user_input()
	get_rss = loadrss(user_in)
	if get_rss == None:
		result = ToastNotifier()
		result.show_toast("Cricket update",	"Team "+user_in.upper()+" Not playing", icon_path= 'Cricket.ico', duration = 10,threaded=True)
		
	
	else: 
		while True:
			get_rss = loadrss(user_in)
			message = ToastNotifier()
			message.show_toast("Cricket update",get_rss, icon_path= 'Cricket.ico', duration = 10,threaded=True)
			
			sleep(30)
	