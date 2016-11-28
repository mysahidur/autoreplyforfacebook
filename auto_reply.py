import subprocess as ss
import fbchat
import time
import re
import getpass


resttime=9

def initialize():
	username = raw_input("enter username/email/phone no. : ")
	password = getpass.getpass("type password for '"+username+"' : ")
	client = fbchat.Client(username, password)
	return client


def match_question(question_from_fb):
	try:
		f=open("data.txt","r")
	except:
		print("data.txt file missing.")
		time.sleep(2)
	for line in f.readlines():
		if(line.startswith('#')):
			continue
		question_from_file=line.split(':')[0]
		answer_from_file=line.split(':')[1]
		if(re.match(question_from_file,question_from_fb)):
			return answer_from_file	
	return None



def system_exec(received_msg):
	try:
		cmdlist=[]
		command=received_msg.split()
		for i in range(2,len(command)):
			cmdlist.append(command[i])
		output=ss.check_output(cmdlist)
		return output
	except:
		return "unable to execute command. sorry for the inconvenience."


def is_msg_yours(msg):
    if msg.other_user_fbid in msg.author:
        return False
    return True



def reply(client,friend_uid,msg):
	sent = client.send(friend_uid, msg)
	if sent:
		print("Reply was successful.")
	time.sleep(resttime)


def receive(client,friend_uid,name):
	last_messages = client.getThreadInfo(friend_uid,0)
#	last_messages.reverse()  # messages come in reversed order


	if not is_msg_yours(last_messages[0]):
		received_msg=last_messages[0].body
		received_msg=received_msg.lower()
		ss.call(['clear'])
		print(received_msg)
		print("\n-------------- this message is sent by "+name+"\n\n")
		
		if(re.match(".capture",received_msg)):
			try:
				code=received_msg.split()[1]
				print(code)
			except:
				reply(client,friend_uid,"type in this format :    .capture <your password>")

			password_file=open("password.txt","r")
			if(password_file.read().strip('\n')==code):
				import capture
				capture.capture()
				client.sendLocalImage(friend_uid,message='You requested a picture from my laptop\'s webcam. Here it is.',image='captured_image.jpg')
				ss.call(['rm','captured_image.jpg'])
				time.sleep(resttime)
			else:
				reply(client,friend_uid,"capture restricted.")
			password_file.close()

		elif(received_msg==".getmanual"):
			try:
				man_file=open("manual.txt","r")
				replymsg=man_file.read()
				reply(client,friend_uid,replymsg)
				replymsg=None
				man_file.close()
			except:
				print("manual.txt file missing.")
				time.sleep(2)

		
		elif(re.match(".exec",received_msg)):
			try:
				code=received_msg.split()[1]
			except:
				reply(client,friend_uid,"type in this format :    .exec <your password> <shell command>")

			password_file=open("password.txt","r")
			if(password_file.read().strip('\n')==code):
				replymsg=system_exec(received_msg)
				reply(client,friend_uid,replymsg)
				replymsg=None
			else:
				reply(client,friend_uid,"execution restricted.")

			password_file.close()
				
			
		else:
			replymsg=match_question(received_msg)
			if(replymsg):
				reply(client,friend_uid,replymsg)		
			else:
				reply(client,friend_uid,"Automated message : I'm not active currently. Try sending me  .getmanual")	
				ss.call(['clear'])

	else:
		ss.call(['clear'])
		print("waiting for "+name+"'s message")
#		time.sleep(.02)
		


def main():
	try:
		client=initialize()
	except:
		print("Unable to connect to server. Try connecting to network.")
		exit()

	friend={}
	name=[]
	try:
		contact_file=open("contacts.txt","r")	
		for line in contact_file.readlines():
			line=line.strip('\n')
			name.append(line)
		contact_file.close()
	except:
		print("contacts.txt file missing.")
	resttime=int(input("add a sleep time (integer value, preferable between 6-10) : "))
	for i in range(len(name)):
		friends = client.getUsers(name[i])  # return a list of names
		friend[name[i]]=friends[0].uid		# adding in dictionary "friend"

	while True: 
		try:
			for i in range(len(name)):
				receive(client,friend.get(name[i]),name[i])
		except KeyboardInterrupt:
			exit(0)

		except:
			print('\nskipped contact : '+name[i])
			time.sleep(.1)
			pass


if __name__=="__main__":
	main()


