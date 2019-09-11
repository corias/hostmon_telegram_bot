## TELEGRAM BOT CONFIGURATION FILE
## FOR USE WITH HOSTMONITOR TO TELGRAM ALERT BOT
################################
## EDIT SETTINGS BELOW THIS LINE TO SETUP YOUR BOT
## BOT TOKEN
tg_token = ''
## CHAT ID
tg_chatid = ''
## VERBOSITY
verbosity = True


##Validate settings
def validate():
	valid = True
	if tg_token == '':
		valid = False
	if tg_chatid == '':
		valid = False
	return valid