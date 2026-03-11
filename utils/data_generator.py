import time

def generate_email():
    return f"user{int(time.time()*1000)}@user.com"

def generate_mobile():
    return f"9{str(int(time.time()*1000))[-9:]}"