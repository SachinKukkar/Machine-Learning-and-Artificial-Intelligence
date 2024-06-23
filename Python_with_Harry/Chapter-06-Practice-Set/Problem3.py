p1 = "Make a lot of Money"

p2 = "Buy Now"

p3 = "Subscribe this"

p4 = "Click this"

message = input("Enter your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("It is a Spam , please don't go forward with this message ")

else:
    print("This message is not a spam")    