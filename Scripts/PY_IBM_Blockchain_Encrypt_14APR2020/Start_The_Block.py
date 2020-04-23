"""Interface for IMB Python Blockchain App @
https://github.com/satwikkansal/python_blockchain_app/tree/ibm_blockchain_post
Created by Travis Beckwith for USD Class 504"""

"""Prior to running script, perform pip install -r requirements.txt"""

import requests
import urllib3
from subprocess import Popen
import time
from tkinter import Tk, Label, Button, W, E
import webbrowser
import re
import socket
#import create_cert_x509

#Initializing variables for environment.
dump = "tmp_data_dump.txt" #Dump contents into a temporary file.
#log = "project_log.txt" #Future add.
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning) #Required to disable subjectAltName for certificates.
host_name = socket.gethostname() # Grabbing machines local name.
webbrowser.register('firefox',
                    None,
                    webbrowser.BackgroundBrowser(
                        "C://Program Files//Mozilla Firefox//firefox.exe")) #Registering Firefox!

time.sleep(2) #Adding delay.

#Starting batch files for external server use
print("Deploying all nodes and decentralized server!")
#Created deploy batch for all other batch files. All CMD prompts are minimized automatically.
p = Popen("Deploy.bat")
stdout, stderr = p.communicate()

time.sleep(2) #Adding delay.

#Linking server nodes with initial node localhost:8000.
"""The following is the equivelent of command curl:
curl -X POST \
  https://localhost:8001/register_with \
  -H 'Content-Type: application/json' \
  -d '{"node_address": "https://localhost:8000"}'"""
headers = {
    'Content-Type': 'application/json',
}
insert_host_name = '"https://{}:8000"'.format(host_name) #Establishing a variable for following chain nodes.
data = '"node_address"'":" + insert_host_name #Combining dictionary name with variable of host name of machine.
data = "{"+data+"}" #Had to modify the result in order for the json to read correctly.
cert = 'cert.crt' #Importing cert for current dictory.
#Assigning variables for links.
requests.post('https://{}:8001/register_with'.format(host_name), headers=headers, data=data, verify=cert)
requests.post('https://{}:8002/register_with'.format(host_name), headers=headers, data=data, verify=cert)
requests.post('https://{}:8003/register_with'.format(host_name), headers=headers, data=data, verify=cert)

#Start of GUI
print("Deploying GUI")
#Defining GUI Class
class Harvester:

    #Defining init function and commands.
    def __init__(self, master):
        self.master = master
        master.title("Harvester")
        master.geometry('1350x450')

        #Master label.
        self.label = Label(master, text="Local Servers:")
        self.label.grid(row=0, column=0, columnspan=1)

        #Hyperlinks to web servers and locations.
        server1 = Button(master, text="Decentralized Server", fg="blue", command=lambda: self.callback("server1"))
        server1.grid(row=0, column=1, sticky=W + E)
        node1 = Button(master, text="Node #1 Miner", fg="blue", command=lambda: self.callback("node1"))
        node1.grid(row=0, column=2, sticky=W + E)
        node2 = Button(master, text="Node #2 Miner", fg="blue", command=lambda: self.callback("node2"))
        node2.grid(row=0, column=3, sticky=W + E)
        node3 = Button(master, text="Node #3 Miner", fg="blue", command=lambda: self.callback("node3"))
        node3.grid(row=0, column=4, sticky=W + E)
        node4 = Button(master, text="Node #4 Miner", fg="blue", command=lambda: self.callback("node4"))

        #Category label and location.
        self.label = Label(master, text="Nodes:")
        self.label.grid(row=2, column=0, columnspan=1)

        #Node buttons and locations.
        self.hash_0_button = Button(master, text="#1", command=lambda: self.update("hash_0"))
        self.hash_0_button.grid(row=3, column=0, rowspan=3, sticky=W + E)
        self.hash_1_button = Button(master, text="#2", command=lambda: self.update("hash_1"))
        self.hash_1_button.grid(row=6, column=0, rowspan=3, sticky=W + E)
        self.hash_2_button = Button(master, text="#3", command=lambda: self.update("hash_2"))
        self.hash_2_button.grid(row=9, column=0, rowspan=3, sticky=W + E)
        self.hash_3_button = Button(master, text="#4", command=lambda: self.update("hash_3"))
        self.hash_3_button.grid(row=12, column=0, rowspan=3, sticky=W+E)

        #Comments and locations.
        self.hash_0_result = Label(master, text="<-------------------- Update Node 1 {}:8000! --------------------".format(host_name))
        self.hash_0_result.grid(row=3, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_1_result = Label(master, text="<-------------------- Update Node 2 {}:8001! --------------------".format(host_name))
        self.hash_1_result.grid(row=6, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_2_result = Label(master, text="<-------------------- Update Node 3 {}:8002! --------------------".format(host_name))
        self.hash_2_result.grid(row=9, column=1, columnspan=5, rowspan=3, sticky=W)
        self.hash_3_result = Label(master, text="<-------------------- Update Node 4 {}:8003! --------------------".format(host_name))
        self.hash_3_result.grid(row=12, column=1, columnspan=5, rowspan=3, sticky=W)

    #The below is establishing my nodes for the GUI.
    def update(self, method):
        if method == "hash_0":
            #Opening the dump file and then writting it.
            with open(dump, "wt") as f:
                url_0 = requests.get('https://{}:8000/chain'.format(host_name), verify='cert.crt') #Adding certs.
                url_0 = (str(url_0.text)) #Turning requests.get to strings.
                # The following command allows a next line, so it's not a run on line.
                url_0 = (re.sub("(.{200})", "\\1\n", url_0, 0, re.DOTALL))
                f.write(url_0) #Writing requests.get to tmp_dump_file for reading purposes.
                f.close #Closing file to save results.
            with open(dump, "r") as f: #Opening temp dump file.
                contents = f.read() #Reading file for second command.
                # The following command removes/replaces all the extra characters with spaces.
                removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
                self.hash_0_result.configure(text=removed) #Linking results to GUI.
                f.close #Saving file.
        #Following commands are repeated for each node.
        elif method == "hash_1":
            with open(dump, "wt") as f:
                url_1 = requests.get('https://{}:8001/chain'.format(host_name), verify='cert.crt')
                url_1 = (str(url_1.text))
                url_1 = (re.sub("(.{200})", "\\1\n", url_1, 0, re.DOTALL))
                f.write(url_1)
                f.close
            with open(dump, "r") as f:
                contents = f.read()
                removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
                self.hash_1_result.configure(text=removed)
                f.close
        elif method == "hash_2":
            with open(dump, "wt") as f:
                url_2 = requests.get('https://{}:8002/chain'.format(host_name), verify='cert.crt')
                url_2 = (str(url_2.text))
                url_2 = (re.sub("(.{200})", "\\1\n", url_2, 0, re.DOTALL))
                f.write(url_2)
                f.close
            with open(dump, "r") as f:
                contents = f.read()
                removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
                self.hash_2_result.configure(text=removed)
                f.close
        elif method == "hash_3":
            with open(dump, "wt") as f:
                url_3 = requests.get('https://{}:8003/chain'.format(host_name), verify='cert.crt')
                url_3 = (str(url_3.text))
                url_3 = (re.sub("(.{200})", "\\1\n", url_3, 0, re.DOTALL))
                f.write(url_3)
                f.close
            with open(dump, "r") as f:
                contents = f.read()
                removed = (contents.replace('{', '').replace('}', '').replace('[', '').replace(']', '').replace('"', ''))
                self.hash_3_result.configure(text=removed)
                f.close
        else:
            exit(99)
    #The below definition is for opening the GUI hyperlinks.
    def callback(self, select):
        if select == "server1":
            webbrowser.get('firefox').open('https://{}:5000'.format(host_name))
        elif select == "node1":
            webbrowser.get('firefox').open("https://{}:8000/mine".format(host_name))
        elif select == "node2":
            webbrowser.get('firefox').open("https://{}:8001/mine".format(host_name))
        elif select == "node3":
            webbrowser.get('firefox').open("https://{}:8002/mine".format(host_name))
        elif select == "node4":
            webbrowser.get('firefox').open("https://{}:8003/mine".format(host_name))
        else:
            exit(99)

root = Tk()
my_gui = Harvester(root)
root.mainloop()
