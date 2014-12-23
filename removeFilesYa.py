import os
import sys

for i in os.listdir(os.getcwd()):
    if i.endswith('.csv') or i.endswith('.txt'):
        os.remove(i)
    
