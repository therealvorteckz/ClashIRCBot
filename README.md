# ClashIRCBot
# Clash of Clans IRC - Stats and Announcer
# New feature - Private Message !login adminpass
# New feature - !announce <bb/mp> <on/off> - Turn on and off announcer for mutliplayer/builder base trophy changes

![image](https://i.imgur.com/J1w8zaD.png)
![image](https://pbs.twimg.com/media/F9K2TLNWsAAnRbh?format=png&name=medium)

Create "bot.env" file with the following parameters for your CoC API

[bot.env]


EMAIL="your@developer.email"

PASSWORD="Developer account pass"


Commands:
!login <adminpass> # Private message the bot to login, to avoid people seeing your admin password
!announce <bb/mp> <on/off> # Turn on or off for builder base/mutliplayer trophy changes

!link <clan / player> <clan/playertag>
   - !link clan [clantag]
   - !link player [playertag]
    
- tags not needed for following commands if !link'ed clan/playertag
  
!stats [optional: playertag]

!clan [optional: clantag]

!troops [optional: playertag]

!showmembers [optional: clantag]

!war [shows war stats for current/recent wars]

!reloadcolors [change bot colors in config and reload on-the-fly]
