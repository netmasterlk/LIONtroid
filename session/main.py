from telethon.sync import TelegramClient
import traceback
from telethon.sessions import StringSession
print ("An online StringSession generator Made With ReplRun By \n\nhttps://t.me/LIONtroid\n\n\n\n")
print ("The lionUltroid Userbot\n\n")
print ("
print ("╔┓╔┓╔━━╦╦━━━━╗
║┃║┃║X X║┗━╗╔━┛
║┗╣┃║╰╯║┏┓║║┏━┓┏━┓┏━┓
╚━╩╩╩━━╩╝╚╩╩╩━╩╩━╩╩━╝\n\n")

try:
  API_KEY = input("Enter API_ID: ")
  API_HASH = input("Enter API_HASH: ")
  with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("")
    session = client.session.save()
    ok = client.send_message("me", f"`{session}`")
    ok.reply("Here is Your Telegram String Session\nKeep it safe\n\n@LIONtroid")
    print("You telegram String session successfully stored in your telegram, please check your Telegram Saved Messages\n\n")
    print("Store it safe !! Don't share with anyone.. Regards..\n\n@LIONtroid")
except:
  traceback.print_exc()
  print("")
  print("Wrong phone number \n make sure its with correct  country code\n\nRestart Me Now")