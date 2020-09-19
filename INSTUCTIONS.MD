# Instructions

Welcome!

## Part 1 (Getting it):

1. Click the green "Code" button.
2. Click "Download Zip"
3. Extract the zip somewhere

## Part 2 (Config):

### 2.1 (Discord Dev Portal)

1. visit https://discord.com/developers/applications and click "create new application"
2. Give it a name
3. Click on the "bot" tab and make a bot
4. Add a PFP, and a username if you wish
5. click "Copy Token". DO NOT GIVE THIS TO ANYONE.
6. put this in `templateconfig.py`(one of the downloaded files), putting the token within the "".
7. save the file

![Screenshot](https://i.imgur.com/5j1GDVF.png)

### 2.2 (Creating a role):

#### 2.2.1 (Creating a role for your bot)

1. go to your discord server
2. click the down arrow in the top left corner of the server
3. click "server settings"
4. click "roles"
5. create a role you wish to assign to the bot
6. Disable EVERYTHING

#### 2.2.2 (Creating a role for your users)

1. go to your discord server
2. click the down arrow in the top left corner of the server
3. click "server settings"
4. click "roles"
5. create a role you wish to assign to your users
6. Add Spesial Premissions (If Any)
7. right click on the role before you leave settings, and select "Copy ID". put this in `templateconfig.py`(one of the downloaded files), replacing `1234567890` with the number you copied.
8. save the file

**IMPORTAINT NOTE: MAKE SURE YOUR BOT ROLE IS ABOVE THE USER ROLE**

##### Make certain channels public (IE: Vip Server)

1. go to the @everyone role
2. Disable "Read Text Channels & See Voice Channels"
3. Make what ever channels you wish for new users to see public (at least one for the authentication). do this by exiting settings, right clicking on a channel, selecting premissions, selecting @everyone and then enable "Read Text Channels & See Voice Channels" for @everyone.

##### OR make certain channels private (IE: Vip Channel)

1. Make what ever channels you wish to hide private. 
2. right click on a channel, select premissins, select @everyone and then disable "Read Text Channels & See Voice Channels" for @everyone.
3. then select your role that the bot will assign, and enable "Read Text Channels & See Voice Channels" for that role.

### 2.3 (making a auth channel)

1. create a new channel
2. right click on the channel, select premissins, select the bot role and then enable "Read Text Channels & See Voice Channels", "Send Messages", and "Manage Roles" for the bot.

### 2.4 (Invite the bot)

1. visit https://discord.com/developers/applications and go to the bot
2. click "General Information"
3. Copy "Client ID"
4. replace the marked bit of this url https://discord.com/oauth2/authorize?client_id=REPLACETHISWITHWHATYOUCOPIED&scope=bot and go to it.

### 2.5 (Renaming)

1. rename `configtemplate.py` to `config.py`

## Part 3 (downloading stuff):

### 3.1 (Python):

1. go to https://www.python.org/downloads/
2. download python for your platform
3. run the file
4. click "Install Now"

### 3.2 (Pip):

1. open up a command prompt (google it)
2. type in `pip install discord.py`

### 3.3 (Security Cirt):

1. go here https://crt.sh/?id=2835394
2. click "download certificate (PEM)
3. Click the file and go through installation (Open, Install, Next Next Finished Sucsessfully installed)

![Where is it?](https://beans-took-my-kids.reeee.ee/38qB2n.png)

## Part 4 (Run programs)

### 4.1 (generate keys):

1. go to the folder you unziped the file
2. in the navigation type `cmd` and hit enter
3. type `python keygenerator.py`
4. enter the number of keys you want and hit enter
5. write yes and hit enter

![Cmd](https://i.imgur.com/xqwUxKP.png)

### 4.2 (Run bot):

1. go to the folder you unziped the file
2. in the navigation type `cmd` and hit enter
3. type `python bot.py`
4. bot should be online

## Part 5 (Profit):

1. Distribute keys to each user (some email programs let you mass send emails, (https://www.extendoffice.com/documents/excel/3560-excel-send-personalized-email.html#a1) (you should be able to paste the list straight into exel and it will reconize the new lines))
2. have them enter it in the auth channel!