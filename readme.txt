this is a auto-reply program for facebook chat.
before running this program(auto_reply.py), install 2 python libraries :

1. fbchat		[pip install fbchat]
2. opencv-python	[pip install opencv-python]


be sure, that your folder has all the files, i.e

1. contacts.txt
2. data.txt
3. manual.txt
4. password.txt and 
5. the main program itself


***
change contacts.txt, data.txt,manual.txt and password.txt files as you wish.


***
write your contacts in contacts.txt file separated by newline.

***
data.txt file contains regular expressions. you may also write as normal text.
syntax is :

question:answer	

or

regular_expression_of_question:answer


***
change password in password.txt file, which is used to restrict .capture and .exec

***
in data.txt file, some replies are written in Bengali, change those as you wish.
