#!/usr/bin/env python3
import discord
from discord.ext import commands

LOGFILE = "talklog.txt"
from .target import TARGET

class ChatLogger(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.log = open(LOGFILE, 'a')

    def cog_unload(self):
        self.log.close()

    @commands.Cog.listener(name="on_message")
    async def chatlogger(self, msg: discord.Message):
        if ( msg.guild!=None and
             msg.guild.id in TARGET and
             msg.author.bot == False ):
            self.log.write(msg.content + '\n')

def setup(bot: commands.Bot):
    print("Chat logging started")
    bot.add_cog(ChatLogger(bot))

def teardown(bot: commands.Bot):
    print("Chat logging stopped")
