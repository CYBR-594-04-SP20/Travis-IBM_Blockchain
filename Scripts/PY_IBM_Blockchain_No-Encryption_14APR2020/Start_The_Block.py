"""Interface for IMB Python Blockchain App @
https://github.com/satwikkansal/python_blockchain_app/tree/ibm_blockchain_post
Created by Travis Beckwith for USD Class 504"""

"""Prior to running script, perform pip install -r requirements.txt"""

import requests
import socket
from subprocess import Popen
import time
from tkinter import Tk, Label, Button, W, E
import webbrowser
import re

#Initializing variables for environment.
#Dump contents into a temporary file for writing and reading in order to view on GUI.
dump = "tmp_data_dump.txt"
#log = "project_log.txt" -Future add.
host_name = socket.gethostname() #Grabbing hostname from machine.

#Starting batch files for external server use
print("Deploying all nodes and decentralized server!")
#Created deploy batch for all other batch files. All CMD prompts are minimized automatically.
p = Popen("Deploy.bat")
stdout, stderr = p.communicate()

#Adding delay inbetween start times.
time.sleep(3)

#Linking server nodes with initial node localhost:8000.
"""The following is the equivelent of command curl:
curl -X POST \
  http://0.0.0.0:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "http://host_name:8000"}'"""
headers = {
    'Content-Type': 'application/json',
}
insert_host_name = '"https://{}:8000"'.format(host_name) #Establishing a variable for following chain nodes.
data = '"node_address"'":" + insert_host_name #Combining dictionary name with variable of host name of machine.
data = "{"+data+"}" #Had to modify the result in order for the json to read correctly.
cert = 'cert.crt' #Importing cert for current dictory.
#Assigning variables for links.
#Assigning variables for links.
requests.post('http://{}:8001/register_with'.format(host_name), headers=headers, data=data)
requests.post('http://{}:8002/register_with'.format(host_name), headers=headers, data=data)
requests.post('http://{}:8003/register_with'.format(host_name), headers=headers, data=data)

#Start of GUI
print("Deploying GUI")
#Defining GUI Class
class Harvester:

    #Defining init function and commands
    def __init__(self, master):
        self.master = master
        master.title("Harvester")
        master.geometry('1350x450')

        self.label = Label(master, text="Local Servers:")
        self.label.grid(row=0, column=0, columnspan=1)

        server1 = Button(master, text="Decentralized Server", fg="blue", command=lambda: self.callback("server1"))
        node1 = Button(master, text="Node #1 Miner", fg="blue", command=lambda: self.callback("node1"))
        node2 = Button(master, text="Node #2 Miner", fg="blue", command=lambda: self.callback("node2"))
        node3 = Button(master, text="Node #3 Miner", fg="blue", command=lambda: self.callback("node3"))
        node4 = Button(master, text="Node #4 Miner", fg="blue", command=lambda: self.callback("node4"))

        server1.grid(row=0, column=1, sticky=W+E)
        node1.grid(row=0, column=2, sticky=W+E)
        node2.grid(row=0, column=3, sticky=W+E)
        node3.grid(row=0, column=4, sticky=W+E)
        node4.grid(row=0, column=5, sticky=W+E)


        self.label = Label(master, text="Nodes:")
        self.label.grid(row=2, column=0, columnspan=1)

        self.hash_0_button = Button(master, text="#1", command=lambda: self.update("hash_0"))
        self.hash_1_button = Button(master, text="#2", command=lambda: self.update("hash_1"))
        self.hash_2_button = Button(master, text="#3", command=lambda: self.update("hash_2"))
        self.hash_3_button = Button(master, text="#4", command=lambda: self.update("hash_3"))

        self.hash_0_button.grid(row=3, column=0, rowspan=3, sticky=W+E)
        self.hash_1_button.grid(row=6, column=0, rowspan=3, sticky=W+E)
        self.hash_2_button.grid(row=9, column=0, rowspan=3, sticky=W+E)
        self.hash_3_button.grid(row=12, column=0, rowspan=3, sticky=W+E)

        self.hash_0_result = Label(master, text="<-------------------- Update Node 1 {}:8000! --------------------".format(host_name))
        self.hash_1_result = Label(master, text="<-------------------- Update Node 2 {}:8001! --------------------".format(host_name))
        self.hash_2_result = Label(master, text="<-------------------- Update Node 3 {}:8002! --------------------".format(host_name))
        self.hash_3_result = Label(master, text="<-------------------- Update Node 4 {}:8003! --------------------".format(host_name))

        self.hash_0_result.grid(row=3, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_1_result.grid(row=6, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_2_result.grid(row=9, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_3_result.grid(row=12, column=1, columnspan=5, rowspan=3, sticky=W)

    #The below is establishing my nodes for the GUI.
    def update(self, method):
        if method == "hash_0":
            #Opening the dump file and then writting it.
            filename = open(dump, 'w')
            url_0 = requests.get('http://{}:8000/chain'.format(host_name))
            url_0 = (str(url_0.text))
            # The following command allows a next line, so it's not a run on line.
            url_0 = (re.sub("(.{200})", "\\1\n", url_0, 0, re.DOTALL))
            filename.write(url_0)
            filename.close
            filename = open(dump, 'r')
            contents = filename.read()
            # THe following command removes/replaces all the extra characters with spaces.
            removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
            self.hash_0_result.configure(text=removed)
            filename.close
        elif method == "hash_1":
            filename = open(dump, 'w')
            url_1 = requests.get('http://{}:8001/chain'.format(host_name))
            url_1 = (str(url_1.text))
            url_1 = (re.sub("(.{200})", "\\1\n", url_1, 0, re.DOTALL))
            filename.write(url_1)
            filename.close
            filename = open(dump, 'r')
            contents = filename.read()
            removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
            self.hash_1_result.configure(text=removed)
            filename.close
        elif method == "hash_2":
            filename = open(dump, 'w')
            url_2 = requests.get('http://{}:8002/chain'.format(host_name))
            url_2 = (str(url_2.text))
            url_2 = (re.sub("(.{200})", "\\1\n", url_2, 0, re.DOTALL))
            filename.write(url_2)
            filename.close
            filename = open(dump, 'r')
            contents = filename.read()
            removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
            self.hash_2_result.configure(text=removed)
            filename.close
        elif method == "hash_3":
            filename = open(dump, 'w')
            url_3 = requests.get('http://{}:8003/chain'.format(host_name))
            url_3 = (str(url_3.text))
            url_3 = (re.sub("(.{200})", "\\1\n", url_3, 0, re.DOTALL))
            filename.write(url_3)
            filename.close
            filename = open(dump, 'r')
            contents = filename.read()
            removed = (contents.replace('{','').replace('}','').replace('[','').replace(']','').replace('"',''))
            self.hash_3_result.configure(text=removed)
            filename.close
        else:
            exit(99)
    #The below definition is for opening the GUI hyperlinks.
    def callback(self, select):
        if select == "server1":
           webbrowser.open_new('http://{}:5000'.format(host_name))
        elif select == "node1":
            webbrowser.open_new("http://{}:8000/mine".format(host_name))
        elif select == "node2":
            webbrowser.open_new("http://{}:8001/mine".format(host_name))
        elif select == "node3":
            webbrowser.open_new("http://{}:8002/mine".format(host_name))
        elif select == "node4":
            webbrowser.open_new("http://{}:8003/mine".format(host_name))
        else:
            exit(99)

root = Tk()
my_gui = Harvester(root)
root.mainloop()
