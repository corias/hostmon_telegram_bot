## HOSTMONITOR TO TELEGRAM ALERT BOT V0.37
## BY KIRILL NIKITIN TGID @CORIAS
## FOR THOSE WHO DO NOT WANT TO BUY 11.99
#######################################
## HOW TO USE IT:
## 1. REGISTER YOUR BOT WITH BOTFATHER
## 2. ADD IT TO THE DESIRED GROUP OR CHANNEL
## 3. INSTALL PYTHON, PYTHON-PIP AND REQUESTS
## 4. ADD PYTHON FOLDER TO PATH
## 5. UNZIP THIS FILE AND tg_bot_settings.py TO FOLDER ON YOUR HOSTMONITOR MACHINE
##    HOSMONITOR USER SHOULD HAVE READ ACCESS TO IT
## 6. EDIT tg_bot_settings.py AS DESCRIPTED IN IT
## 7. ADD ACTION PROFILE TO HOSTMONITOR CONTAINING FOLLOWING:
##    ACTION TYPE - Run external program
##    COMMAND LINE - py hostmon_alert_bot.py -n "%TestName%" -s "%Status%" -m "%TestMethod%" -r "%Reply%" -f "%Folder%"
##    KEYS -m -r -f ARE OPTIONAL
##    WORKING DIRECTORY - script folder
##    WINDOW MODE - SW_HIDDEN

import sys, getopt
import requests

## TELEGRAM SETTINGS HERE, EDIT FILE TO USE
#######################################
import tg_bot_settings as settings


## MAIN CLASS THAT WILL DO ALl DIRTY WORK
class HostmonAlert:
    #INITIALIZE
    def __init__ (self, name, status):
        self.name = name
        self.status = status
        self.folder = ''
        self.method = ''
        self.reply = 'Y0lln3v3rG=TSu(hR3plY'
        ## I'VE HAD TO USE SOME WEIRD STRING WHICH HOSTMONITOR WILL NEVER GENERATE TO SHOW BLANK REPLIES

    #GET COMMAND LINE ARGUMENTS
    def GetCmdLine(self, argv):
        try:
            opts, args = getopt.getopt(argv,"hn:s:f:m:r:",["name=","status=","folder=","method=","reply="])
        except getopt.GetoptError:
            print("Malformed arguments, use key -h to get help")
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('Usage: hostmon_alert_bot.py -n <Name> -s <Status> [-f <Folder> -m <Method> -r <Reply>]')
                sys.exit
            elif opt in ("-n", "--name"):
                self.name = arg
            elif opt in ("-s", "--status"):
                self.status = arg
            elif opt in ("-f", "--folder"):
                self.folder = arg
            elif opt in ("-m", "--method"):
                self.method = arg
            elif opt in ("-r", "--reply"):
                self.reply = arg
                
    # FORMAT TEXT TO MARKDOWN STYLE
    def FormTelegramMessage(self):
            emoji = self.GenerateStatusEmoji()
            text = '*'
            text += self.name + ': ' + emoji + ' ' + self.status + '*\n'
            if self.method != '':
                text += '*Method:* ' + self.method + '\n'
            if self.reply != "Y0lln3v3rG=TSu(hR3plY":
                text += '*Reply:* ' + self.reply + '\n'
            if self.folder != '':
                text += '\n'
                text += '*Folder:* ' + self.folder + '\n'
            return text

    # ADD EMOJI CORRESPONDING TO TEST STATUS
    def GenerateStatusEmoji(self):
        emojicode = ''
        # 'GOOD' STATUSES
        if self.status == "Ok":
            emojicode = u'\U00002705' #GREEN CHECK MARK
        elif self.status == "Host is alive":
            emojicode = u'\U00002705'
        # 'BAD' STATUSES
        elif self.status == "Warning":
            emojicode = u'\U000026A0' #WARNING SIGN
        elif self.status == "Unknown":
            emojicode = u'\U00002753' #QUESTION SIGN
        elif self.status == "No answer":
            emojicode = u'\U0000274C' #CROSS SIGN
        elif self.status == "Bad":
            emojicode = u'\U0000274C'
        elif self.status == "Win32 Error":
            emojicode = u'\U0000274C'
        return emojicode
        
    #SEND MESSAGE
    def SendMessage (self, token, chat, text):
        message = text
        if (settings.verbosity):
            print('Message:\n') #DEBUG OUTPUT
            print(message + '\n') ##
        send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat + '&parse_mode=Markdown&text=' + message
        response = requests.get(send_text)
        if (settings.verbosity):
            print('Response: \n') #DEBUG
            print(response.json()) ##
        return response.json()

## INITIALIZE CLASS INSTANCE
Alert = HostmonAlert('idle', 'idle')

## POPULATE INSTANCE WITH ARGUMENTS FROM COMMAND LINE
if __name__ == "__main__":
   Alert.GetCmdLine(sys.argv[1:])

## FORMAT MESSAGE STRING THAT WILL BE SENT TO TELEGRAM
MsgText = Alert.FormTelegramMessage()

## SEND MESSAGE
Msg = Alert.SendMessage(settings.tg_token, settings.tg_chatid, MsgText)

## THAT'S ALL FOLKS
