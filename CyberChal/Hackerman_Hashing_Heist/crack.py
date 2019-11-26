from hashing import pass_hash
import password

b= open("bad_passwords.txt",'r')
for i in b.readlines():
    password(pass_hash(i));

