# discord-auth-bot

users can ping the auth bot a valid key stored in `keys.txt`. the bot then:

1. grants them a role
2. removes the key from `keys.txt` making the key invalid for future uses (one time use!)

# What it could be used for

1. keeping a exclusive discord for patrons exclusive!

2. keeping events/private groups safe from 4chan (as each key can only be used once, and you only need to generate as much as you plan to use).

# How to set up

1. Add as many 5 digit combos of letter and numbers seperated by new lines in `keys.txt`

2. Change the roles var to your role

3. [create a discord bot](https://discord.com/developers/applications) and invite it to your server

4. change the client secret vars to the secret
