import os
try:os.mkdir('Data')
except:pass
try:
    __import__("BruteInsta").EXAL()
except Exception as e:
    exit(str(e).title())
