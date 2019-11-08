import os
import argparse

parser = argparse.ArgumentParser(prog='setup.py',conflict_handler="resolve")
parser.add_argument("--restore",action="store_true",help="Restore to original")
args=parser.parse_args()


path = os.getcwd()+"/"
user = os.path.expanduser("~")+"/"
bashrc = user+".bashrc"
if not os.path.exists("{}.bashrc_copy".format(user)):
    os.system("cp {} {}".format(bashrc,user+".bashrc_copy"))

if args.restore:
    os.system("cp {}.bashrc_copy {}".format(user,bashrc))
    quit()


with open(bashrc,'a') as bash:
    for i in os.listdir(path):
        if os.path.isdir(i):
            program = path+i+"/"
            for a in os.listdir(program):
                l = program+a
                bash.write('alias {}="python {}"\n'.format(a[:-3],l))
bash.close()

print "Run this:"
print("\tsource {}".format(bashrc))

