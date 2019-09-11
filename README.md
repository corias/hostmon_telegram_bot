# hostmon_telegram_bot
Telegram bot to use with KS-Hostmonitor

HOW TO USE IT:
1. Register your bot with BotFather
2. Add it to desired group or channel
3. Install python, python-pip and requests
4. Add python folder to PATH
5. Place telegram_alert_bot.py and tg_bot_settings.py in the same folder on your Hostmonitor machine
   Hostmonitor user should have read and execute access to it
6. Edit tg_bot_settings.py as descripted below:
   Replace '' in tg_token with your actual token given by BotFather
   Replace '' in tg_chatid with your actual Chat ID
7. Create or modify Action Profile in Hostmonitor. Add a 'bad' action with following parameters:
   Action type - Run external program
   Command line - py hostmon_alert_bot.py -n "%TestName%" -s "%Status%" -m "%TestMethod%" -r "%Reply%" -f "%Folder%
   Arguments -m -r -f are optional
   Working directory - script folder
   Window mode - SW_HIDDEN
8. If needed, add a 'good' action with same parameters as in step above

ALTERNATE USAGE:
You may use this script with command-line arguments from any other caller, it's just optimized for hostmonitor
Syntax is: py hostmon_alert_bot.py -n "<TestName>" -s "<Status>" [-m "<Method>" -r "<Reply>" -f "<Folder>"]
