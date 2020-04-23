#Created for USD 504 - Travis Beckwith

@ECHO OFF
start /min Node1.bat
ping localhost -n 1 > nul
start /min Node2.bat
ping localhost -n 1 > nul
start /min Node3.bat
ping localhost -n 1 > nul
start /min Node4.bat
ping localhost -n 1> nul
start /min Server1.bat
