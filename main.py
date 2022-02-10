import discord
from discord.ext import commands
from discord.utils import get
import os
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle
from discord.ext import tasks
from datetime import datetime
import re
import matplotlib.pyplot as plt
import io
import os
from dotenv import load_dotenv
import matplotlib.ticker as ticker
from bs4 import BeautifulSoup
import requests

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

channel = "https://www.youtube.com/channel/UC_hK9fOxyy_TM8FJGXIyG8Q"

plt.style.use('_mpl-gallery')

max_x_val = 10

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.niyatiba = 777607820144279562
        self.kruth = 908900123000598548
        self.previous_value = None
        self.alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
        self.previous_person = None
        self.abc = False
        self.count = False
        self.previous_number = None
        self.naenaeki = 885465751815847946

    def detect(self, author):
        return author == self.niyatiba

    @commands.command()
    async def hep(self, ctx):
        if self.detect(ctx.author.id):
            await ctx.channel.send("Sorry, I don't talk with dumb ugly simps.")
            return

        await ctx.channel.send(f"<@{self.kruth}>, {ctx.author} needs some help. ")

    @commands.command()
    async def solve(self, ctx, *args):
        if self.detect(ctx.author.id):
            await ctx.channel.send("Sorry, I don't talk with dumb ugly simps.")
            return

        content = " ".join(args)
        content = content.replace("^", "**")

        if trySolve(content) != False:
            content = str(eval(content))
            await ctx.channel.send(content)
        else:
            content = content.replace("my", "your")
            await ctx.channel.send(f'I can\'t solve {content} dumbf***.')

    @commands.command()
    async def ship(self, ctx, args):
        if args:
            if args[0].lower() == 'niyati':
                await ctx.channel.send("Niyati is a verified simp on Twitter.")

    @commands.command()
    async def abc(self, ctx):
        if str(ctx.channel) == ("learn-abcs"):
            self.abc = not self.abc
            self.previous_value = None
            self.previous_person = None
            await ctx.channel.send("ABC mode is turned %s" % ("on." if self.abc else "off."))

    @commands.command()
    async def count(self, ctx):
        self.count = not self.count
        await ctx.channel.send("Count mode is turned %s" % ("on." if self.count else "off."))

    @commands.command()
    async def plot(self, ctx, *args):
        args = ' '.join(args)
        data_stream = io.BytesIO()
        e = graph(0, args)
        print(e)
        if e != False:
            e1 = graph(max_x_val, args)
            e = e+e1

            xpoints = [0] + np.array([e[0], e1[0]])
            ypoints = [0] + np.array([e[1], e1[1]])

            fig = plt.figure()

            ax = plt.axes()
            ax.xaxis.set_major_locator(ticker.MultipleLocator((10**len(max(xpoints)))/2))
            ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))

            ax.yaxis.set_major_locator(ticker.MultipleLocator((10**len(max(ypoints)))/2))
            ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

            plt.plot(xpoints, ypoints, c = 'k')

            plt.savefig(data_stream, dpi=fig.dpi, bbox_inches='tight', format='jpg')

            data_stream.seek(0)

            chart = discord.File(data_stream,filename="plot.png")

            plt.grid()

            plt.close()

            embed = discord.Embed(title="Graph")
            embed.set_image(
            url="attachment://plot.png"
            )

            await ctx.send(embed=embed, file=chart)

    @commands.command()
    async def daniel(self, ctx):
        await ctx.message.delete()
        embed = discord.Embed(title="This Won't Work", description="Daniel Lapusso is gay, you're not getting him Niyatiba. ", color = 0x00ff00)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def dhardhar(self, ctx):
        e = discord.Embed()
        shuffle(random_urls)
        e.set_image(url=random_urls[0])
        await ctx.channel.send(embed=e)

    @commands.command()
    async def nae(self, ctx):
        await ctx.message.delete()
        user = discord.utils.get(self.bot.users, name="Nanaki")
        await ctx.channel.send(f"<@885465751815847946>, NAENAEKI LEAVE THE GOD DAMN SERVER DIRTY B*!")

    @tasks.loop(seconds = 3600)
    async def dharmann(self, ctx):
        days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday')

        now = datetime.now()
        s = now.strftime("%A %H")

        times = s.split(" ")
        if times[0] in days and times[1] == "20":
            embed = discord.Embed(title="Our Man Dhar Mann", description="Dhar Mann might have uploaded, check his channel. ", color = 0x00ff00)
            embed.add_field(name="Link", value="https://www.youtube.com/channel/UC_hK9fOxyy_TM8FJGXIyG8Q")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def dhar(self, ctx):
        embed = discord.Embed(title="Our Man Dhar Mann", description="Dhar Mann might have uploaded, check his channel. ", color = 0x00ff00)
        embed.add_field(name="Link", value="https://www.youtube.com/channel/UC_hK9fOxyy_TM8FJGXIyG8Q")
        await ctx.channel.send(embed=embed)


    @commands.command()
    @commands.has_role('med')
    async def roast(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.message.author

        if ctx.author.id == 777607820144279562:
            await ctx.channel.send(member + "Sorry, I don't talk with dumb ugly simps.")
        else:
            shuffle(l)
            await ctx.reply(l[0], mention_author=False)
            await ctx.message.delete()

    @commands.command()
    async def cmdlist(self, ctx):
        commands =  [str(i) for i in list(self.get_commands())]
        commands = list(sorted(commands))
        print(commands)

        embed = discord.Embed(title="Command List", color = 0x00ff00)
        embed.add_field(name="Commands", value="\n".join(commands))
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def setmax(self, ctx, value):
        global max_x_val

        value = tryInt(value)
        if value == False:
            return

        max_x_val = value
        await ctx.channel.send("The new max x value is %s" % max_x_val)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in")

    @commands.Cog.listener()
    async def on_message(self, message):
        if str(message.channel) == "learn-abcs":
            if len(message.content) == 1 and message.content.isalpha() and self.abc:
                msg = message.content.lower()
                emoji = '\N{WHITE HEAVY CHECK MARK}'
                print(self.alphabet[self.alphabet.index(msg) - 1])
                print(self.previous_value)
                if not self.previous_value and msg == "a":
                    await message.add_reaction(emoji)
                    self.previous_value = msg
                    self.previous_person = message.author
                elif self.previous_value and self.alphabet[self.alphabet.index(msg) - 1] == self.previous_value and message.author != self.previous_person and msg != "z":
                    print("MSG: %s" % msg)
                    await message.add_reaction(emoji)
                    self.previous_value = msg
                    self.previous_person = message.author
                elif msg == "z" and self.alphabet[self.alphabet.index(msg) - 1] == self.previous_value and message.author != self.previous_person:
                    await message.channel.send("Congratulations, you passed the challenge! You can play again if you want, just use !abc")
                    await message.add_reaction(emoji)
                    self.previous_value = None
                    self.previous_person = None
                    self.abc = False
                else:
                    await message.add_reaction('\N{CROSS MARK}')
                    await message.channel.send(f"{message.author.name} ruined it :(")
                    self.previous_value = None
                    self.previous_person = None
                    self.abc = False

        if message.author.id == self.naenaeki or message.author.id == self.niyatiba:
            await message.add_reaction("<:SIMP:936741664037412924>")
            await message.add_reaction("\N{WARNING SIGN}")







random_urls = ["https://www.dharmann.com/wp-content/uploads/2019/11/lifes-better-with-someone-that-always-got-your-back-dhar-mann-quote.png.webp", "https://www.dharmann.com/wp-content/uploads/2019/11/Dhar-Mann-quote-about-life.jpg.webp", "https://www.dharmann.com/wp-content/uploads/2019/11/Dhar-Mann-quote-about-success.jpg.webp", "https://www.dharmann.com/wp-content/uploads/2019/11/Dhar-Mann-quotes-on-being-happy.jpg.webp", "https://www.dharmann.com/wp-content/uploads/2019/11/Dhar-Mann-inspirational-quote.jpg.webp", "https://www.dharmann.com/wp-content/uploads/2019/11/Dhar-Mann-quote-image.jpg.webp"]

count = False

roasts = []

cooldown = 0.5

x = 0
y = 0

with open("roasts.txt", "r", encoding="utf8") as f:
    l = f.readlines()
    for i in l:
        if i == "\n":
            l.remove(i)
            continue
        i.replace("\n", "")

def tryInt(v):
    try:
        return int(v)
    except:
        return False


def trySolve(v):
    try:
        exec(v)
    except:
        return False

def graph(xl, equation):
    x=xl
    try:
        y = eval(equation.replace("x", str(x)))
        return (x, y)
    except:
        return False


client = commands.Bot(command_prefix="!")

client.add_cog(Commands(client))

client.run(TOKEN)
