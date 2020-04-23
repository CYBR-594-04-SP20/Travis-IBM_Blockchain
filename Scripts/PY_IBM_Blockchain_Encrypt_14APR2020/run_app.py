"""Script modified by TB for 504 project"""

from app import app
import ssl
import socket

#Establishing host IP.
host_name = socket.gethostname()
print(host_name)

#Had to define host as shown below. Also had to enable ssl for flask via below -Travis
app.run(host='{}'.format(host_name), debug=True, ssl_context=('cert.crt', 'private.key'))
