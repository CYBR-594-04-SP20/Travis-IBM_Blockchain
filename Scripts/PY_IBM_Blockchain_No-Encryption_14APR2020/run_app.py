from app import app
import socket

host_name = socket.gethostname() #Grabbing hostname from machine.

app.run(host='{}'.format(host_name), debug=True)
