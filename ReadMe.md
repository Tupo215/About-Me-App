# About ME APP
## Overview
### Note
This application was created in 2020 for a school project at the time.
### Summary
Let me start to say making this project was Fun and now I understand the excitement of coding. The project was to create a simple application that has three tabs one which is informative information about our self, one with four pictures of ourself and the last with contact information as well as a functioning call button. 
In this application, it was first created with Qt designer which makes life easy but adds too much unnecessary code to a simple app compared to created fully coded but for this purpose, it was not solely on the interface but more on how the application works it. Qt designer was used to creating:
        • Tabs
        • Add pictures
        • Create Buttons
        • Create the information Text
    1. To create a tab simply create a main window in Qt designer and add to       the already provided window with right-click on the tab and add two more and rename them. 
    The tabs are about, pictures, and contact information.
    2. To add pictures for all the tabs, it is required to create labels, and before adding the picture making sure they are in the same folder as that being used to create both the Qt designer and the python file as well as the application itself. Then add the pictures using pixmap which creates a qrc file to store all the photos which are used in Qt designer any additional photos can be added in python but will not be stored in the qrc file.
    3. To create a button simply add a push-button but it will not work until programmed in python.
    4. To create information text simply use the text edit even though it was learned that for secure programming it is wise to use plain text edit because it does not allow outside users to edit text. Then simply add information by double-clicking the created text edit.
Now to the interesting part. After creating the GUI in Qt designer now it needs to be converted to a python file(.py). This is called creating an environment where using command prompt and making sure you are in the same directory as the folder containing all the images and the Qt file (.ui). If you installed everything then simply write ‘pyqui5 -x name_of_file.ui – x new_name.py’ what it does is take the ui file and convert it to a python file. The python file is what will be used to create a fully functioning app.
Before editing the python file in my case, the IDE that I was using could not import the qrc file so there was a need to convert it to a python file. It should have been easily converted to .py with the command prompt using pyrcc5 command but for some reason, it could not so I had to use PyCharm where first I had to create a command in settings leading it to where exactly the pyrcc5 command was kept in the Anaconda file and give it an instruction to turn the qrc file to py using the pyrcc5 command. Once the file was converted, I could now start editing the file.
The about tab had nothing to edit. In the pictures tab, I decided to create two buttons that allow you to go next or previous of a photo. When labeling the buttons in qt designer I made sure to give them a name I could remember like ‘next’ and ‘prev’. Now I had to connect the buttons to the pictures I wanted to display. First, define functions that should display the prev and next picture.
 def show_Prev(self):
 self.picture.setPixmap(QtGui.QPixmap("Picture prev.png"))
This finds the picture called ‘picture prev.png’ in the folder containing all the file am using. 
This does not mean the picture will display when the previous button is pressed that will require linking the button to this defined function. This is done by:
 self.prev.clicked.connect(self.show_Prev)
which takes the created prev button and connects it to the defined function when clicked. 
Now, this displays the prev picture as defined. The same goes for next only with different picture linked and a function defined as show_next. Then connect the next button to the defined function.
Now moving on to the contact information page. With the Api’s found some required
money to use the service or accredited business. The skype Api could not work for the latest skype version because third party members are not supported anymore. So instead I found Twilio that allows us to create a trial account and create such a function but only works for text messages and one way. To add just a little something extra I added a function that will allow a pop up to show up when clicked and my number will receive a text message.
def show_popup(self):
 msg= QMessageBox()
 msg.setWindowTitle('Confirmation')
 msg.setText('Your Message has been sent Succefully')
 msg.setStandardButtons(QMessageBox.Ok)
 
 msg.exec_()
def show_call_me(self):
 account_sid = 'AC47c1f834866be49903ef47432080131c'
 auth_token = 'd10627f2b0ec5e27d65e7d8e7db7e149'
 client = Client(account_sid, auth_token)
 
 message = client.messages.create(
 from_='+13474915638', 
 body='Hello', 
 to='+265991071898'
 )
 
 print(message.sid)
The first function is defined for the pop-up window. For this to be functional I needed to import QMessageBox from the PyQt5 library. The first msg simply creates the popup window using QMessageBox, the second names the window in this case it is called confirmation, the third sets the text that will show in the pop-up window which is a message has been sent to my number, the fourth allows for a button to be created called ok and more can be added by using ‘l’ and writing the same QMessageBox but using another name like exit, cancel and so many more which can be 
connected to another function but this time instead of using a self-link a function has to be a msg.button.clicked and now lastly the msg.exec_() is used to execute the pop-up window otherwise it will not show. The function is linked using the function as the picture expect with show_popup.
After the first action is executed and the ok button is pressed the second function comes into action which a function linked to Twilio. It will send me the message ‘Hello’ with the number above and that will be the end. To explain what is happening let first explain what an API is. So there are terms people confuse a lot the REST and an API. The difference is a REST as by name only receives 
information and will do exactly one thing either get, post, and all the others but another function will not follow while an API does both it can get and post at the same time or two other functions at the same time. These are mostly used by developers who want to constantly make sure their users have the latest updated application without having to install the whole application again. What it 
does is it stores the information on the server and is available for both a desktop of phone application which is what WhatsApp does. So in this case the code requests to Twilio to send me the text using their server.