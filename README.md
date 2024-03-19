**Discord BOT's Developer:** [ https://t.me/ahtohnis ]
**Command usage:** !alert [@user_tag]

_To make this bot work, you need to follow these steps:_

**1.** Create a new Discord application and add a bot to it on the Discord Developer Portal. Copy the bot token.

**2.** Invite the bot to your Discord server using the OAuth2 URL provided by the Discord Developer Portal with ADMINISTRATOR Permissions.

**3.** Replace the placeholder token `BOT_TOKEN` with your actual bot token in the `client.run()` function at the end of the code.

**4.** Run the script and the bot should come online in your Discord server.

**5.** You can now use the `!alert` command in your Discord server to set alerts for specific users. Only the server owner will be able to use this command.

**6.** When the alert is set, the user will be notified in the server and a message will be sent to their DMs. If the user does not respond within 12 hours, the bot will revoke their read permissions for the channel and notify them that the ticket has been closed.

Make sure to have the necessary permissions for the bot in your Discord server and ensure that you are handling user input properly to prevent any misuse of the bot's functionalities.
