@ECHO OFF
set FLASK_APP=node_server.py
echo set FLASK_APP=node_server.py
flask run --host=0.0.0.0 --cert cert.crt --key private.key --port 8002