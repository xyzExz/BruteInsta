import os
try:os.mkdir('Data');os.mkdir('result')
except:pass
try:
    __import__("BruteInsta").LoginKey().Run()
except Exception as e:
    exit(str(e).title())