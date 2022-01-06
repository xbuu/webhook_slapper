from dhooks import Webhook, Embed
import os

os.system("title Webhook_Slapper")
webhook = input("Webhook Link > ")
hook = Webhook(webhook)
print("Got webhook, send a chat! :) - dex#1337")

def chat():
    userchat = input(f"Send2Hook> ")
    hook.send(userchat)
    chat()

chat()