@ECHO OFF
start /min Node1.bat
ping 127.0.0.1 -n 1 > nul
start /min Node2.bat
ping 127.0.0.1 -n 1 > nul
start /min Node3.bat
ping 127.0.0.1 -n 1 > nul
start /min Node4.bat
ping 127.0.0.1 -n 1 > nul
start /min Server1.bat
