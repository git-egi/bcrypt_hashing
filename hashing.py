import bcrypt
import time

def main():
    givenpass=input("\nType pass : ")
    givenpass=givenpass.encode('utf-8')
    timestart=time.time()
    salt_used=bcrypt.gensalt(rounds=15)
    hashed=bcrypt.hashpw(givenpass,salt_used)
    timeend=time.time()
    print("\n---------------------------------------")
    print("\nSalt Used: ",salt_used)
    print("\nHashed Pass: ",hashed)
    print("\n---------------------------------------")
    print("\nTime Passed: ",timeend-timestart)
    print("\n---------------------------------------")
    verifypass=input("Verify Pass : ")
    verifypass=verifypass.encode('utf-8')
    if bcrypt.checkpw(verifypass,hashed):
        print("\nVerification Complete!")
    else:
        print("\nWrong Password!")
    print("\n")

if __name__ == "__main__":
    main()
