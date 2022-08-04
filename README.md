# Python Discord Bot Template
Just a simple repository to get you started with your Discord Bot in Python.

For significantly more information, go to the [Discord.py Docs](https://discordpy.readthedocs.io/en/stable/).

![Python Version](https://img.shields.io/badge/Python-3.8.2-blue.svg) ![Discord.py Version](https://img.shields.io/badge/Discord.py-1.7.3-blue.svg)

#

### How to create a new bot:
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on **New Application** in the top-right corner.
3. Give your application a name.
4. When the application is created, click the **Bot** tab on the left.
5. Click on **Add Bot** on the left.
6. You've now created a bot!

### How to add the bot to your server:
1. When the bot is created, click on the **Oauth2** tab on the left.
2. In the drop-down menu, click on **URL Generator**.
3. Under **Scopes**, select **bot**.
4. Add the necessary permissions for your bot under the **Bot Permissions** menu that shows up.
5. Once your done, scroll down to the newly generated link. Copy it.
6. Enter the link in a new tab.
7. It should ask you which server to add the bot to.
8. Select your server, then confirm the permissions (and also complete the "hCaptcha").
9. Your bot is now added to your server!

### How to get the bot token:
1. When the bot is created, click on the **Reset Token** button.
2. Copy the token.
3. Go to `bot.py`.
4. Under `TOKEN`, paste the copied token inside the quotes.
5. Your code should now connect to the bot.

### Running the code:
1. Open a new terminal.
3. Run the command `pip install discord`
4. Now the needed libraries are installed.
5. Now run the bot!

## REMEMBER
DO NOT SHARE YOUR TOKEN. IT IS LIKE A PASSWORD. IF SOMEONE HAS THE TOKEN, THEY CAN THEN ACCESS THE BOT.
