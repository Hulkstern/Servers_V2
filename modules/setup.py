import os
import modules.ui as ui
cwd = os.getcwd()
serversDir = os.path.join(cwd,'servers')

def init():
    if not os.path.exists(serversDir):
        print("servers directory does not exist, creating...")
        os.mkdir(serversDir)
        print("server directory created, visit: "+ui.link("https://www.minecraft.net/en-us/download/server")+" to download the most recent server.jar to the sampleServer directory to get started")