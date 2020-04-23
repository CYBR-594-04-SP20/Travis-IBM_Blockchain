@ECHO OFF
CD C:\Windows\System32
curl -X GET http://localhost:8001/chain
echo curl -X GET http://localhost:8001/chain
curl -X GET http://localhost:8002/chain
echo curl -X GET http://localhost:8002/chain
curl -X GET http://localhost:8003/chain
echo curl -X GET http://localhost:8003/chain