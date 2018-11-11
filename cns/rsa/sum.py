import math
import random
global prime, root
print "Alice and Bob agree the prime"
prime = input("enter the agreed prime number by both")
print "The prime is ",prime, "\n"
print "Alice and Bob agree the primitive root to use"
root = input("enter the agreed primitive root")
print "The root is",root, "\n"
print "At this stage, Alice, Bob & Eve all know the prime and the root", "\n"
alicesecret =input("ENTER ALICE SECRET NUMBER")
print "Alice chooses a secret number",alicesecret
bobsecret =input("ENTER BOB SECRET NUMBER")
print "Bob chooses a secret number", bobsecret, "\n"
print "Alice calculates her public key as A = root ^ alicesecret mod prime"
alicepublic = (root ** alicesecret) % prime
print "Alice's public key is",alicepublic, "\n"
print "Bob calculates his public key as B = root ^ bobsecret mod prime"
bobpublic = (root ** bobsecret) % prime
print "Bob's public key is", bobpublic, "\n"
print "Alice and Bob exchange their public keys"
print "Eve now knows Alice and Bob's public keys", "\n"
print "Alice calculates the shared key as K = B ^ alicesecret mod prime"
alicekey = (bobpublic ** alicesecret) % prime
print "Bob calculates the shared key as K = A ^ bobsecret mod prime"
bobkey = (alicepublic ** bobsecret) % prime
print "Alice calculates the shared key and gets", alicekey
print "Bob calculates the shared key and gets", bobkey, "\n"
print "Eve does not know the shared private key that Alice & Bob can now use"
print "\n"
print ("encrypting the account number using shared key ")
print("\n")
acc_no=input("enter the account number")
print("\n")
print(acc_no)
print("\n")
acc_no=str(acc_no)
res=""
for i in acc_no:
	i=int(i)
	i=i+bobkey
	if (i>=10):
		i=i%10
	i=str(i)
	res+=i
print("the account number is encrypted by the shared key")
print("\n")
print("the encrypted account is")
print("\n")
print(res)
