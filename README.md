# Cipher Buddy

Cipher Buddy combines latest technologies and innovative approaches that make reporting any kind of cyber crime super smooth.

[Cipher Buddy](https://dataencrypted.herokuapp.com/) has an easy to navigate menu.

* Submit Cyber Complaint
* Submit Site Complaint
* Complaint Status
* P2P Chat
* Contact Us
* About us
* Host it yourself

To use [Cipher Buddy](https://dataencrypted.herokuapp.com/) one needs to signup using a valid email id and then login.

### Submit Cyber Complaint

The section contails a form in which a complaint can be filed regading any cyber crime and required action will be taken.

### Submit Site Complaint

The section contails a form in which a complaint can be filed regading any shady website and the website will be added to a database of potentially harmful websites.

### Complaint Status
Shows the status of complaint.

### P2P Chat 
The Section contains 3 tabs
* Send Chat 
* Recieve Chat
* Data

  * Send Chat 
  To have an encrypted serverless chat with your peer.
  1. Enter ID shared by the peer in the text box provided.
  2. Click connect.
  3. Once the status changes to connected you can communicate with your peer using the chat window provided. 

  * Recieve Chat
  1. An ID is shown when you open the window.
  2. Share the ID to your peer. 
  3. Once the status changes to connected you can communicate with your peer using the chat window provided. 

  * Data 
  1. As you open the window you are provided with and option to upload file.
  2. Once you upload file a link will be generated.
  3. Share the link with your peer.
  4. File will be downloaded once the link is accessed.

### Contact Us
The Section provides you with an option to contact us.

### About Us
The section has the information regading [Cipher Buddy](https://dataencrypted.herokuapp.com/) and the vision of developers.

## Image Gallery

* Submit Cyber Complaint
  ![CC](/ss/cc.jpg)
* Submit Site Complaint
  ![CS](/ss/sc.jpg)
* Complaint Status
  ![CC](/ss/cs.jpg)
* P2P Chat
  ![CC](/ss/p2p.jpg)
* Contact Us
  ![CC](/ss/CU.jpg)
* About us
  ![CC](/ss/AU.jpg)


### Host It Yourself
- Clone this repo on your machine
- Create an account on [Heroku](https://heroku.com)
- Install [Heroku CLI](https://cli-assets.heroku.com/heroku-x64.exe)
- Open Command Prompt and navifate to the directory in which you have cloned the repo.
- Login into your [Heroku](https://heroku.com) account using [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
- Enter `heroku create` in cmd to create an app.
- Enter `git push heroku main` to push the repo to heroku.
- Enter `heroku ps:scale web=1` to assign a free dyno to the app.
- Enter `heroku open` to open the link of your app.
- You are good to go.
- Admin panel has all the submissions and can be accesed at at `/admin`, however, due to restriction of free deployement, the database may not work properly.
- You can refer [here](https://stackoverflow.com/questions/36938414/cannot-log-in-to-django-admin-interface-with-heroku-deployed-app) to create a super user.
