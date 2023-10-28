#!/usr/bin/env python3
# Clash of Clans - IRC Stats Bot and Announcer
# coded by vorteckz@vorteckzstudios.online

import coc
from coc import utils
import time
import os
import logging
import logging.handlers
import ssl
import asyncio
import threading
from time import sleep
from dotenv import load_dotenv
load_dotenv('bot.env')
import colors
from importlib import reload
from config import config
import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()


print('#'*56)
print('#{0}#'.format(''.center(54)))
print('#{0}#'.format('Clash of Clans - IRC Based Bot'.center(54)))
print('#{0}#'.format('Developed by vorteckz in Python'.center(54)))
print('#{0}#'.format('https://github.com/therealvorteckz/ClashIRCBot'.center(54)))
print('#{0}#'.format(''.center(54)))
print('#'*56)




def createtable():
    c.execute('''CREATE TABLE if not exists users (
        name text unique,
        clan text,
        tag text

        )''')
    conn.commit()
    c.execute(f'INSERT OR REPLACE INTO users VALUES (:name, :clan, :tag)', {'name': None, 'clan': None, 'tag': None})
    conn.commit()
coc_client = coc.EventsClient()    


 # Pro Tip : if you don't have @client.event then your events won't run! Don't forget it!
def color(msg: str, foreground: str, background: str='') -> str:
    '''
    Color a string with the specified foreground and background colors.
    
    :param msg: The string to color.
    :param foreground: The foreground color to use.
    :param background: The background color to use.
    '''
    return f'\x03{foreground},{background}{msg}{colors.reset}' if background else f'\x03{foreground}{msg}{colors.reset}'


@coc.ClanEvents.member_role_change()
async def on_clan_member_role_change(old_role, new_role):
    await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member Role Change", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(old_role.name, colors.color3)}{color("] [", colors.color1)}{color(old_role.role,colors.color3)} {color("to", colors.reset)} {color(new_role.role, colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_trophies_change()
async def on_clan_member_trophies_change(old_trophies, new_trophies):
    if old_trophies.trophies < new_trophies.trophies:
        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(old_trophies, colors.color3)}{color("] [", colors.color1)}{color("League:", colors.color2)} {color(old_trophies.league, colors.color3)}{color("] [", colors.color1)}{color("Trophies Increased:", colors.color2)} {color(old_trophies.trophies,colors.color3)} {color("->", colors.reset)} {color(new_trophies.trophies,colors.color3)}{color("] [", colors.color1)}+{color(new_trophies.trophies-old_trophies.trophies,colors.color3)}{color("]", colors.color1)}')
    else:	
        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(old_trophies, colors.color3)}{color("] [", colors.color1)}{color("League:", colors.color2)} {color(old_trophies.league, colors.color3)}{color("] [", colors.color1)}{color("Trophies Decreased:", colors.color2)} {color(old_trophies.trophies,colors.color3)} {color("->", colors.reset)} {color(new_trophies.trophies,colors.color3)}{color("] [", colors.color1)}-{color(old_trophies.trophies-new_trophies.trophies,colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_join()
async def on_clan_member_join(member, clan):
    await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(member.name,colors.color3)} {color("/", colors.reset)} {color(member.tag, colors.color3)}{color("] [", colors.color1)}{color("MP Trophies:", colors.color2)} {color(member.trophies, colors.color3)}{color("] [", colors.color1)}{color("BH Trophies:", colors.color2)} {color(member.builder_base_trophies, colors.color3)}{color("]", colors.color1)} {color("joined our clan", colors.color2)} {color("[", colors.color1)}{color(clan.name, colors.color3)}{color("] [", colors.color1)}{color("Tag:", colors.color2)} {color(clan.tag, colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_leave()
async def on_clan_member_leave(member, clan):
    await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(member.name,colors.color3)} {color("/", colors.reset)} {color(member.tag, colors.color3)}{color("] [", colors.color1)}{color("MP Trophies:", colors.color2)} {color(member.trophies, colors.color3)}{color("] [", colors.color1)}{color("BH Trophies:", colors.color2)} {color(member.builder_base_trophies, colors.color3)}{color("]", colors.color1)} {color("left our clan", colors.color2)} {color("[", colors.color1)}{color(clan.name, colors.color3)}{color("] [", colors.color1)}{color("Tag:", colors.color2)} {color(clan.tag, colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_league_change()
async def on_clan_member_league_change(old_league, new_league):
    await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("Member", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(old_league, colors.color3)}{color("] [", colors.color1)}{color("League Change:", colors.color2)} {color(old_league.league, colors.color3)} {color("->", colors.reset)} {color(new_league.league, colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_donations(config.clashconfig.tag)
async def on_clan_member_donation(old_member, new_member):
    final_donated_troops = new_member.donations - old_member.donations
    await bot.sendmsg(config.irc.channel, f'{color("[",colors.color1)}{color("Donations", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(new_member, colors.color3)}{color("] [", colors.color1)}{color("Clan:", colors.color2)} {color(new_member.clan, colors.color3)}{color("]", colors.color1)} {color("just donated", colors.color2)} {color("[", colors.color1)}{color("Troop Spaces:", colors.color2)} {color(final_donated_troops, colors.color3)}{color("]", colors.color1)}')
@coc.ClanEvents.member_received(config.clashconfig.tag)
async def on_clan_member_donation_receive(old_member, new_member):
    final_received_troops = new_member.received - old_member.received
    await bot.sendmsg(config.irc.channel, f'{color("[",colors.color1)}{color("Donations", colors.color2)}{color("] [", colors.color1)}{color("Player:", colors.color2)} {color(new_member, colors.color3)}{color("] [", colors.color1)}{color("Clan:", colors.color2)} {color(old_member.clan, colors.color3)}{color("]", colors.color1)} {color("just received", colors.color2)} {color("[", colors.color1)}{color("Troop Spaces:", colors.color2)} {color(final_received_troops, colors.color3)}{color("]", colors.color1)}')
@coc.WarEvents.state(tags=config.clashconfig.tag)
async def on_war_state_change(current_state, war):
    warscore = await coc_client.get_current_war(config.clashconfig.tag)
    
    if war.state == "preparation":
        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("]", colors.color1)} {color("Preparation has just begun for a war between", colors.color2)} {color("[", colors.color1)}{color(war.clan.name, colors.color3)}{color("]", colors.color1)} {color("and", colors.color2)} {color("[", colors.color1)}{color(war.opponent.name, colors.color3)}{color("]", colors.color1)}')
    elif war.state == "inWar":
        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("]", colors.color1)} {color("Battle has just begun between", colors.color2)} {color("[", colors.color1)}{color(war.clan.name, colors.color3)}{color("]", colors.color1)} {color("and", colors.color2)} {color("[", colors.color1)}{color(war.opponent.name, colors.color3)}{color("]", colors.color1)}')
    elif war.state == "warEnded":
        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("]", colors.color1)} {color("Battle has just ended between", colors.color2)} {color("[", colors.color1)}{color(war.clan.name, colors.color3)}{color("]", colors.color1)} {color("and", colors.color2)} {color("[", colors.color1)}{color(war.opponent.name, colors.color3)}{color("]", colors.color1)}')
        if war.status == "won":
            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.clan.name, colors.color3)}{color("]", colors.color1)} {color("won the war!", colors.color2)}') 
            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Home:", colors.color2)} {color(warscore.clan.stars, colors.color3)} {color("Stars", colors.reset)} {color("|", colors.color1)} {color("Destruction:", colors.color2)} {color(warscore.clan.destruction, colors.color3)}%{color("] [", colors.color1)}{color("Enemy:", colors.color2)} {color(warscore.opponent.stars, colors.color3)} {color("Stars", colors.reset)} {color("|", colors.color1)} {color("Destruction:", colors.color2)} {color(warscore.opponent.destruction, colors.color3)}%{color("]", colors.color1)}')
        elif war.status == "lost": 
            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.clan.name, colors.color3)}{color("]", colors.color1)} {color("lost...", colors.color2)}')
            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Home:", colors.color2)} {color(warscore.clan.stars,colors.color3)} Stars {color("|", colors.color1)} {color("Destruction:", colors.color2)} {color(warscore.clan.destruction, colors.color3)}%{color("] [", colors.color1)}{color("Enemy:", colors.color2)} {color(warscore.opponent.stars, colors.color3)} Stars {color("|", colors.color1)} {color("Destruction:", colors.color2)} {color(warscore.opponent.destruction, colors.color3)}%{color("]", colors.color1)}')
        else:
            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan_name, colors.color3)}{color("] [", colors.color1)}{color("War", colors.color3)}{color("]", colors.color1)} Looks like a tie!!!')

@coc.WarEvents.war_attack()
async def current_war_stats(attack, war):
    await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color("Attack #", colors.color2)}{color(attack.order, colors.color3)}{color("] [", colors.color1)}{color("Attacker(#", colors.color2)}{color(attack.attacker.map_position, colors.color3)}{color("):", colors.color2)} {color(attack.attacker, colors.color3)}{color("] [", colors.color1)}{color("Defender(#", colors.color2)}{color(attack.defender.map_position, colors.color3)}{color("):", colors.color2)} {color(attack.defender, colors.color3)}{color("] [", colors.color1)}{color("Stars:", colors.color2)} {color(attack.stars, colors.color3)}{color("] [", colors.color1)}{color("Destruction:", colors.color2)} {color(attack.destruction, colors.color3)}{color("%]", colors.color1)}')


def ssl_ctx() -> ssl.SSLContext:
    '''Create a SSL context for the connection.'''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

class Bot(object):
    def __init__(self):
        self.nickname = config.irc.nickname
        self.username = config.irc.username
        self.realname = config.irc.realname
        self.channel = config.irc.channel
        self.channelkey = config.irc.channelkey
        self.reader   = None
        self.writer   = None			
    
    createtable()
    async def action(self, chan: str, msg: str):
        '''
        Send an ACTION to the IRC server.

        :param chan: The channel to send the ACTION to.
        :param msg: The message to send to the channel.
        '''
        await self.sendmsg(chan, f'\x01ACTION {msg}\x01')

    async def raw(self, data: str):
        '''
        Send raw data to the IRC server.
		
        :param data: The raw data to send to the IRC server. (512 bytes max including crlf)
        '''
        self.writer.write(data[:510].encode('utf-8') + b'\r\n')

    async def sendmsg(self, target: str, msg: str):
        '''
        Send a PRIVMSG to the IRC server.
        
        :param target: The target to send the PRIVMSG to. (channel or user)
        :param msg: The message to send to the target.
        '''
        try:
            await self.raw(f'PRIVMSG {target} :{msg}')
        
            time.sleep(config.throttle.msg)
        except:
            await bot.sendmsg(config.irc.channel, "Slow down homie!!")
           

    async def connect(self):
        '''Connect to the IRC server.'''
       
        while True:
            try:
                options = {
                    'host'       : config.irc.server,
                    'port'       : config.irc.port if config.irc.port else 6697 if config.irc.ssl else 6667,
                    'limit'      : 1024, # Buffer size in bytes (don't change this unless you know what you're doing)
                    'ssl'        : ssl_ctx() if config.irc.ssl else None,
                    'family'     : 2, # 10 = AF_INET6 (IPv6), 2 = AF_INET (IPv4)
                    'local_addr' : None # Can we just leave this as args.vhost?
                }
                self.reader, self.writer = await asyncio.wait_for(asyncio.open_connection(**options), 15) # 15 second timeout
                if config.irc.password:
                    await self.raw('PASS ' + config.irc.password) # Rarely used, but IRCds may require this
                await self.raw(f'USER {self.username} 0 * :{self.realname}') # These lines must be sent upon connection
                await self.raw('NICK ' + self.nickname)                      # They are to identify the bot to the serve
                          
                while not self.reader.at_eof():
                    data = await asyncio.wait_for(self.reader.readuntil(b'\r\n'), 300) # 5 minute ping timeout
                    await self.handle(data.decode('utf-8').strip()) # Handle the data received from the IRC server
                
            except Exception as ex:
                logging.error(f'failed to connect to {config.irc.server} ({str(ex)})')
            finally:
                await asyncio.sleep(5) # Wait 30 seconds before reconnecting

    async def handle(self, data: str):
        try:
            logging.info(data)
            args = data.split()
            if data.startswith('ERROR :Closing Link:'):
                    raise Exception('Cannot Connect')
            if args[0] == 'PING':
                    await self.raw('PONG ' + args[1]) # Respond to the server's PING request with a PONG to prevent ping timeout
            elif args[1] == '001': # RPL_WELCOME
                    await self.raw(f'MODE {self.nickname} +B') # Set user mode +B (Bot)
                    await asyncio.sleep(10) # Wait 10 seconds before joining the channel (required by some IRCds to wait before JOIN)
                    await self.raw(f'JOIN {self.channel} {self.channelkey}')
            elif args[1] == '433': # ERR_NICKNAMEINUSE
                    self.nickname += '_' # If the nickname is already in use, append an underscore to the end of it
                    await self.raw('NICK ' + self.nickname) # Send the new nickname to the server
            elif args[1] == 'KICK':
                    chan   = args[2]
                    kicked = args[3]
                    if kicked == self.nickname:
                        await asyncio.sleep(3)
                        await self.raw(f'JOIN {chan}')
            elif args[1] == 'PRIVMSG':
                    ident  = args[0][1:]
                    nick   = args[0].split('!')[0][1:].lower()
                    target = args[2]
                    msg  = ' '.join(args[3:])[1:]
                    arguments = msg.split()
                    bandageamount = '0'                
                    if target == self.nickname:
                        pass # Handle private messages here
                    if target.startswith('#'): # Channel message
                        if msg.startswith('!'):
                            try:    
                                if time.time() - config.throttle.last < config.throttle.cmd and config.throttle.lastnick == nick:
                                    if not config.throttle.slow:
                                        config.throttle.slow = True
                                        await bot.sendmsg(config.irc.channel, "Slow Down")
                                        
                                else:
                                    config.throttle.slow = False
                                    config.throttle.lastnick = nick
                                    if arguments[0] == '!hug':
                                        await bot.sendmsg(target, f'[XOXO Hugger9000... {nick} hugs {arguments[1]}]')
                                    if arguments[0] == '!reloadcolors':
                                        reload(colors)
                                        
                                    if arguments[0] == '!help':
                                        await bot.sendmsg(config.irc.channel, f'[ClashIRCBot Commands]')
                                        await bot.sendmsg(config.irc.channel, f'\r\n')
                                        await bot.sendmsg(config.irc.channel, f'!link <clan/player> <clan/playertag>')
                                        await bot.sendmsg(config.irc.channel, f'!link clan [clantag]')
                                        await bot.sendmsg(config.irc.channel, f'!link player [playertag]')
                                        await bot.sendmsg(config.irc.channel, f'\r\n')
                                        await bot.sendmsg(config.irc.channel, f"Tags not needed for following commands if !link'ed clan/playertag")
                                        await bot.sendmsg(config.irc.channel, f'!stats [optional: playertag]')
                                        await bot.sendmsg(config.irc.channel, f'!clan [optional: clantag]')
                                        await bot.sendmsg(config.irc.channel, f'!troops [optional: playertag]')
                                        await bot.sendmsg(config.irc.channel, f'!showmembers [optional: clantag]')
                                        await bot.sendmsg(config.irc.channel, f'!war [shows war stats for curren/recent wars]')
                                        await bot.sendmsg(config.irc.channel, f'!reloadcolors [change bot colors in config and reload on-the-fly]')
                                    if arguments[0] == '!war':
                                        
                                        war = await coc_client.get_current_war(config.clashconfig.tag)
                                        if war.end_time:
                                            hours, remainder = divmod(int(war.end_time.seconds_until), 3600)    
                                            minutes, seconds = divmod(remainder, 60)
                                            if war.state == "preparation":
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color("Remaining Preparation Time:", colors.color2)} {color(hours- 24, colors.color3)} {color("hours", colors.color2)} {color(minutes, colors.color3)} {color("minutes", colors.color2)} {color(seconds, colors.color3)} {color("seconds", colors.color2)}{color("]", colors.color1)}')
                                            if war.state == "inWar":
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color("Remaining War Time:", colors.color2)} {color(hours, colors.color3)} {color("hours", colors.color2)} {color(minutes, colors.color3)} {color("minutes", colors.color2)} {color(seconds, colors.color3)} {color("seconds", colors.color2)}{color("]", colors.color1)}')
                                            if war.state == "warEnded":
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color("War is completed", colors.color3)}{color("]", colors.color1)}')
                                        warperc = f"{war.clan.destruction:.2f}"
                                        enemyperc = f"{war.opponent.destruction:.2f}"
                                        if war.clan.name != None:
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.clan.name, colors.color3)}{color("] [", colors.color1)}{color(war.clan.stars, colors.color3)} {color("Stars", colors.color2)}{color("] [", colors.color1)}{color(warperc, colors.color3)}%{color("/", colors.color1)}{color("100", colors.color3)}%{color("] [", colors.color1)}{color("Attacks:", colors.color2)} {color(war.clan.attacks_used, colors.color3)}{color("/", colors.color1)}{color(int(war.clan.total_attacks), colors.color3)}{color("]", colors.color1)}')
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.opponent.name, colors.color3)}{color("] [", colors.color1)}{color(war.opponent.stars, colors.color3)} {color("Stars", colors.color2)}{color("] [", colors.color1)}{color(enemyperc, colors.color3)}%{color("/", colors.color1)}{color("100", colors.color3)}%{color("] [", colors.color1)}{color("Attacks:", colors.color2)} {color(war.opponent.attacks_used, colors.color3)}{color("/", colors.color1)}{color(int(war.clan.total_attacks), colors.color3)}{color("]", colors.color1)}')
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.clan.name, colors.color3)}{color("] - [", colors.color1)}{color(war.clan.tag, colors.color3)}{color("]", colors.color1)}')
                                            for m, b in enumerate(war.clan.members, start=1):
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [#", colors.color1)}{color(m, colors.color3)} {color("[", colors.color1)}{color(b.name, colors.color3)}{color("] [", colors.color1)}{color("Stars:", colors.color2)} {color(b.star_count, colors.color3)}{color("]", colors.color1)}')
                                                                        
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [", colors.color1)}{color(war.opponent.name, colors.color3)}{color("] - [", colors.color1)}{color(war.opponent.tag, colors.color3)}{color("]", colors.color1)}')
                                            for o, e in enumerate(war.opponent.members, start=1):
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War", colors.color3)}{color("] [#", colors.color1)}{color(o, colors.color3)} {color("[", colors.color1)}{color(e.name, colors.color3)}{color("] [", colors.color1)}{color("Stars:", colors.color2)} {color(e.star_count, colors.color3)}{color("]", colors.color1)}')
                                    if arguments[0] == '!showmembers':
                                        if len(arguments) <= 1:
                                                c.execute(f"SELECT * FROM users WHERE name=:name", {'name': nick})
                                                user = c.fetchall()
                                                for regs in user:
                                                    ptag = regs[1]
                                                if coc.utils.is_valid_tag(ptag):
                                                    player = await coc_client.get_clan(ptag)  
                                        else:
                                            
                                            if arguments[1] and coc.utils.is_valid_tag(arguments[1]):
                                                player = await coc_client.get_clan(arguments[1])
                                                   
                                        clan = player
                                            #embed = discord.Embed(title=f"[**Members of {clan.name}**]", color=discord.Color.gold(), description=member)
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan.name, colors.color3)}{color("]", colors.color1)}')
                                        for i, a in enumerate(clan.members, start=1):
                                                name1 = a.name
                                                tag1 = a.tag
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Tag:", colors.color2)}{color(a.tag, colors.color3)}{color("]", colors.color1)} {color("[", colors.color1)}{color("Player:", colors.color2)} {color(a.name, colors.color3)}{color("]", colors.color1)}')
                                                #member += f"{name1}\n"
                                                #membertag += f"{tag1}\n"
                                    if arguments[0] == '!clan':
                                        if len(arguments) <= 1:
                                                c.execute(f"SELECT * FROM users WHERE name=:name", {'name': nick})
                                                user = c.fetchall()
                                                for regs in user:
                                                    ptag = regs[1]
                                                if coc.utils.is_valid_tag(ptag):
                                                    player = await coc_client.get_clan(ptag)
                                                    clan = await coc_client.get_clan(ptag)
                                        else:
                                            
                                            if arguments[1] and coc.utils.is_valid_tag(arguments[1]):
                                                player = await coc_client.get_clan(arguments[1])
                                                clan = await coc_client.get_clan(arguments[1])
                                                   
                                        leader = utils.get(clan.members, role=coc.Role.leader)
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color(clan.name, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Invite Link:", colors.color2)} {color(clan.share_link,colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Level:", colors.color2)} {color(clan.level, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Leader:", colors.color2)} {color(leader, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Tag:", colors.color2)} {color(clan.tag, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Description:", colors.color2)} {color(clan.description,colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War League:", colors.color2)} {color(clan.war_league, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Trophies", colors.color2)}{color("] [", colors.color1)}{color("MP:", colors.color2)} {color(clan.points, colors.color3)}{color("] [", colors.color1)}{color("VS:", colors.color2)} {color(clan.builder_base_points, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Member Count", colors.color2)} {color("[", colors.color1)}{color(clan.member_count, colors.color3)}{color("/", colors.color1)}{color("50", colors.color3)}{color("]", colors.color1)}')
                                        if clan.war_losses != None:
                                            if clan.war_wins != None:
                                                if clan.war_ties != None:
                                                   await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Wars Total:", colors.color2)} {color(clan.war_wins+ clan.war_losses+ clan.war_ties, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Wars Won:", colors.color2)} {color(clan.war_wins, colors.color3)}{color("] [", colors.color1)}{color("Wars Lost:", colors.color2)} {color(clan.war_losses, colors.color3)}{color("] [", colors.color1)}{color("Wars Ties:", colors.color2)} {color(clan.war_ties, colors.color3)}{color("]", colors.color1)}')
                                    if arguments[0] == '!link':
                                        c.execute(f'SELECT rowid FROM users WHERE name=(:name)', {'name': nick})
                                        data=c.fetchone()
                                        if data is None:
                                            c.execute(f'INSERT OR REPLACE INTO users VALUES (:name, :clan, :tag)', {'name': nick, 'clan': None, 'tag': None})
                                            conn.commit()
                                        if len(arguments) >= 1:
                                         if arguments[1] == 'player':
                                            if coc.utils.is_valid_tag(arguments[2]):
                                                c.execute(f'UPDATE USERS set TAG = (:tag) where NAME = (:name)', {'tag': arguments[2], 'name': nick})
                                                player = await coc_client.get_player(arguments[2])
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Linked your nickname to Clash Player:", colors.color2)} {color(player, colors.color3)} {color("Tag:", colors.color2)}{color(arguments[2], colors.color3)}{color("]", colors.color1)}')
                                                conn.commit()
                                            else:
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("You entered a NON-existant Player Tag", colors.color2)}{color("]", colors.color1)}')
                                         elif arguments[1] == 'clan':
                                            if coc.utils.is_valid_tag(arguments[2]):
                                                teamname = await coc_client.get_clan(arguments[2])
                                                c.execute(f'UPDATE USERS set CLAN = (:clan) where NAME = (:name)', {'clan': arguments[2], 'name': nick})
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Linked your nickname to clan name: ", colors.color2)}{color(teamname, colors.color3)} {color("Tag: ", colors.color2)}{color(arguments[2], colors.color3)}]')
                                                conn.commit()  
                                            else:
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("You entered a NON-existant Clan Tag", colors.color2)}{color("]", colors.color1)}')

                                    if arguments[0] == '!stats':
                                        if len(arguments) <= 1:
                                                c.execute(f"SELECT * FROM users WHERE name=:name", {'name': nick})
                                                user = c.fetchall()
                                                for regs in user:
                                                    ptag = regs[2]
                                                if coc.utils.is_valid_tag(ptag):
                                                    player = await coc_client.get_player(ptag)  
                                        else:
                                            
                                            if arguments[1] and coc.utils.is_valid_tag(arguments[1]):
                                                player = await coc_client.get_player(arguments[1])
                                         
                                        conq = player.get_achievement("Conqueror")
                                        defs = player.get_achievement("Unbreakable") 
                                        siege = player.get_achievement("Siege Sharer")
                                        don = player.get_achievement("Friend in Need")
                                        spells = player.get_achievement("Sharing is caring")
                                        
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Player Information:", colors.color2)} {color(player.name, colors.color3)}{color("] [", colors.color1)}{color("Experience:", colors.color2)} {color(player.exp_level, colors.color3)}{color("]", colors.color1)}')
                                        if player.town_hall >= 12:
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Town Hall:", colors.color2)} {color(player.town_hall, colors.color3)}{color("] [", colors.color1)}{color("Weapon:", colors.color2)} {color(player.town_hall_weapon, colors.color3)}{color("] [", colors.color1)}{color("Builder Hall:", colors.color2)} {color(player.builder_hall, colors.color3)}{color("]", colors.color1)}')
                                        else:
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Town Hall:", colors.color2)} {color(player.town_hall, colors.color3)}{color("] [", colors.color1)}{color("Builder Hall:", colors.color2)} {color(player.builder_hall, colors.color3)}{color("]", colors.color1)}')
                                        
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Tag:", colors.color2)} {color(player.tag, colors.color3)}{color("]", colors.color1)}')
                                        if (player.role):
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Clan:", colors.color2)} {color(player.clan, colors.color3)}{color("] [", colors.color1)}{color("Tag:", colors.color2)} {color(player.clan.tag, colors.color3)}{color("] [", colors.color1)}{color("Member Role:", colors.color2)} {color(player.role, colors.color3)}{color("]", colors.color1)}')
                                                await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("War Stars:", colors.color2)} {color(player.war_stars, colors.color3)}{color("]", colors.color1)}')
                                        
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("MP Trophies:", colors.color2)} {color(player.trophies, colors.color3)}{color("] [", colors.color1)}{color("VS Trophies:", colors.color2)} {color(player.builder_base_trophies, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("League:", colors.color2)} {color(player.league, colors.color3)}{color("]", colors.color1)}')
                             
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Season Attacks:", colors.color2)} {color(player.attack_wins, colors.color3)}{color("] [", colors.color1)}{color("Season Defenses:",  colors.color2)} {color(player.defense_wins, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Season Donated:", colors.color2)} {color(player.donations, colors.color3)}{color("] [", colors.color1)}{color("Season Received:", colors.color2)} {color(player.received, colors.color3)}{color("]", colors.color1)}')
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Total Attacks:", colors.color2)} {color(conq.value, colors.color3)}{color("] [", colors.color1)}{color("Total Defenses:", colors.color2)} {color(defs.value, colors.color3)}{color("]", colors.color1)}')
                                        
                                        if siege.value < 1:
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Total Troops Donated:", colors.color2)} {color(don.value, colors.color3)}{color("] [", colors.color1)}{color("Total Spells Donateds:", colors.color2)} {color(spells.value, colors.color3)}{color("]", colors.color1)}')
                                        else:  
                                            #member += f'[Total Troops Donated: {don.value:,}] [Total Spells Donateds: {spells.value:,}]\n[**Total Siege Machines Donated:** {siege.value:,}]\n"
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Total Troops Donated:", colors.color2)} {color(don.value, colors.color3)}{color("]", colors.color1)}') 
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Total Spells Donateds:", colors.color2)} {color(spells.value, colors.color3)}{color("]", colors.color1)}')
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Total Siege Machines Donated:", colors.color2)} {color(siege.value, colors.color3)}{color("]", colors.color1)}')
                                                                                                                                                          
                                    if arguments[0] == '!troops':
                                        if len(arguments) <= 1:
                                                c.execute(f"SELECT * FROM users WHERE name=:name", {'name': nick})
                                                user = c.fetchall()
                                                for regs in user:
                                                    ptag = regs[2]
                                                if coc.utils.is_valid_tag(ptag):
                                                    player = await coc_client.get_player(ptag)  
                                        else:
                                            
                                            if arguments[1] and coc.utils.is_valid_tag(arguments[1]):
                                                player = await coc_client.get_player(arguments[1])
                                         
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Player Troop Levels:", colors.color2)} {color(player.name, colors.color3)} - {color("Experience", colors.color2)} {color(player.exp_level, colors.color3)}{color("]", colors.color1)}')
                                       
                                        for hero in player.heroes:
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Heroes", colors.color2)}{color("] [", colors.color1)}{color(str(hero.name), colors.color3)}{color("] [", colors.color1)}{color("Level:", colors.color2)} {color(hero.level, colors.color3)}/{color(hero.max_level, colors.color3)}]')
       
                                        for hero_pets in player.pets:
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Pets", colors.color2)}{color("] [", colors.color1)}{color(str(hero_pets.name), colors.color3)}{color("] [", colors.color1)}{color("Level:", colors.color2)} {color(hero_pets.level, colors.color3)}/{color(hero_pets.max_level, colors.color3)}{color("]", colors.color1)}')
                                     
                                        await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("MP Troops for", colors.color2)} {color(str(player.name), colors.color3)}{color("]", colors.color1)}')                                        
                                        for troop in player.home_troops:
                                            await bot.sendmsg(config.irc.channel, f'{color("[", colors.color1)}{color("Troop:", colors.color2)} {color(str(troop.name), colors.color3)}{color("] [", colors.color1)}{color("Level:", colors.color2)} {color(troop.level, colors.color3)}/{color(troop.max_level, colors.color3)}{color("]", colors.color1)}')
                                                            
                                config.throttle.last = time.time()
                            except Exception as ex:
                                if time.time() - config.throttle.last < config.throttle.cmd:
                                    if not config.throttle.slow:
                                        await bot.sendmsg(config.irc.channel, 'Slow down homie!')
                                        config.throttle.slow = True
                                config.throttle.last = time.time()

                            
                #except (UnicodeDecodeError, UnicodeEncodeError):
        except (UnicodeDecodeError, UnicodeEncodeError):
            pass # Some IRCds allow invalid UTF-8 characters, this is a very important exception to catch
        except Exception as ex:
            logging.exception(f'Unknown error has occured! ({ex})')


       
bot = Bot()

testone = 0
global clan_name
async def main() -> None:
        coc_client.add_events(
                    on_clan_member_role_change,
                    on_clan_member_trophies_change,
                    on_clan_member_join,
                    on_clan_member_leave,
                    on_clan_member_league_change,
                    on_clan_member_donation,
                    on_clan_member_donation_receive,
                    on_war_state_change,
                    current_war_stats
                    )
        setup_logger('clash-ircbot', to_file=True) 
        try:     
            await coc_client.login(os.environ['EMAIL'],os.environ['PASSWORD'])
            coc_client.add_clan_updates(config.clashconfig.tag)
            global clan_name 
            team_name = await coc_client.get_clan(config.clashconfig.tag)
            
            clan_name = team_name


    # creates users table in sqlite3 "data.db" if not created already
    # Attempt to log into 
    # CoC API using your credentials. You must use the
    # coc.EventsClient to enable event listening

    # Register all the callback functions that are triggered when a
    # event if fired.
        except:
            print("error")
            sleep(5)
            coc_client.remove_events(
                    on_clan_member_role_change,
                    on_clan_member_trophies_change,
                    on_clan_member_join,
                    on_clan_member_leave,
                    on_clan_member_league_change,
                    on_clan_member_donation,
                    on_clan_member_donation_receive,
                    on_war_state_change,
                    current_war_stats
                    )     
            await main()       
        threading.Thread(target=await bot.connect(),daemon=True).start()
        createtable() 


def setup_logger(log_filename: str, to_file: bool = False):
    '''
    Set up logging to console & optionally to file.

    :param log_filename: The filename of the log file
    '''
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)9s | %(message)s', '%I:%M %p'))
    if to_file:
        fh = logging.handlers.RotatingFileHandler(log_filename+'.log', maxBytes=250000, backupCount=3, encoding='utf-8') # Max size of 250KB, 3 backups
        fh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)9s | %(filename)s.%(funcName)s.%(lineno)d | %(message)s', '%Y-%m-%d %I:%M %p')) # We can be more verbose in the log file
        logging.basicConfig(level=logging.INFO, handlers=(sh,fh))
    else:
        logging.basicConfig(level=logging.INFO, handlers=(sh,))
        
               
if __name__ == "__main__":
    setup_logger('clashbot-irc', to_file=True) # Optionally, you can log to a file, change to_file to False to disable this.

    # Unlike the other examples that use `asyncio.run()`, in order to run
    # events forever you must set the event loop to run forever so we will use
    # the lower level function calls to handle this.

    loop = asyncio.get_event_loop()
    try:
        # Using the loop context, run the main function then set the loop
        # to run forever so that it continuously monitors for events
        loop.run_until_complete(main())
        #loop.run_forever()
    except KeyboardInterrupt:
        pass
    

asyncio.run(main())