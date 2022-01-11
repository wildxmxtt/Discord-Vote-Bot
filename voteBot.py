from discord import message
from discord import reaction
from discord import emoji
from discord import client
from discord import channel
from discord import file
from discord import activity
from discord.ext import commands
import time


from discord.utils import get

TOKEN = 'TOKEN'

bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    print('VoteBot: ON')


#This is the help command that lets the user know all of the avaliable commands that can be used 
@bot.command()
async def hlp(ctx):
    await ctx.reply('The list of commands are: \n !vs for a ITEM VS ITEM poll \n !vote for a THIS or THAT poll Ex: Cars OR Trains \n To input !vote or !vs make sure to type \n !vote OPTION OPTION')

#This is the vote command it takes context (ctx) the first option (opt1) and second option (opt2)
@bot.command()
#the defualt time 300 seconds is equal to 5 minutes 
async def vote(ctx, opt1, opt2, timeSet = 300):
    #sends a message 
    msgV = await ctx.send(f"{ctx.author.name} wants to know " + opt1 + ' OR ' + opt2)
    #defines the emojis
    one = "1️⃣"
    two = "2️⃣"
    #adds emojis on to the message the bot just sent
    await msgV.add_reaction(one)
    await msgV.add_reaction(two)
    
    #creates a sleep loop for reminder messages to be sent
    if(timeSet < 30 ):
        print("In wait loop 1a")
        time.sleep(timeSet - 5)
    else:
        print("In wait loop 1b")
        time.sleep(timeSet / 2)
    await ctx.reply('The poll for {} OR {} is almost over please vote!'.format(opt1,opt2))

    #sends the final vote message
    print("In wait loop 2")
    time.sleep(timeSet)
    await ctx.reply("The poll for {} OR {} is now over please type '!r' to see the results".format(opt1,opt2))
    print("'Poll over' message was sent")

#This is the vs command it takes context (ctx) the first option (opt1) and second option (opt2)
@bot.command()
#the defualt time 300 seconds is equal to 5 minutes 
async def vs(ctx, opt1, opt2, timeSet = 300):
    #sends a message 
    msgV = await ctx.send(f"{ctx.author.name} wants to know who would win " + opt1 + ' VS ' + opt2)
    #defines emojiis
    one = "1️⃣"
    two = "2️⃣"
    #adds emojis on to the message the bot just sent
    await msgV.add_reaction(one)
    await msgV.add_reaction(two)
    
    #creates a sleep loop for reminder messages to be sent
    if(timeSet < 30 ):
        print("In wait loop 1a")
        time.sleep(timeSet - 5)
    else:
        print("In wait loop 1b")
        time.sleep(timeSet / 2)
    await ctx.reply('The poll for {} VS {} is almost over please vote!'.format(opt1,opt2))
    
    #sends the final vote message
    print("In wait loop 2")
    time.sleep(timeSet)
    await ctx.reply("The poll for {} VS {} is now over please type '!r' to see the results".format(opt1,opt2))



#this is the last event to be evaluated 
#This script only is designed to look for the emojis 'one' and 'two'

@bot.event
async def on_raw_reaction_add(payload):
    one = "1️⃣"
    two = "2️⃣"
    
    #fetches the channel, the message, and the reactions on that message in that particaular channel
    channel = bot.get_channel(payload.channel_id)
    msg = await channel.fetch_message(payload.message_id)
    reaction = get(msg.reactions, emoji = payload.emoji.name)
    
    #checks to see if the emoji is one or two
    if(payload.emoji.name == one or payload.emoji.name == two): 
        #if so it creates a file at this location, this will need to be changed if used on another machine XXXX
        file1 = open(r"C:\Users\Mattw\Documents\Python programs\Discord_Vote_Bot\vB_voteOne.txt", "w+")
        file2 = open(r"C:\Users\Mattw\Documents\Python programs\Discord_Vote_Bot\vB_voteTwo.txt", "w+")

        if(reaction.count > 1):
            #if the reaction count is above one then it will evauate the message
            if(payload.emoji.name == one):
            #fetches the channel, the message, and the reactions on that message in that particaular channel
                channel = bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)
                reaction = get(msg.reactions, emoji = payload.emoji.name)
                #creates a count for the one emojis
                oneCount = reaction.count
                #assings this count to a text file with the letter X
                file1.write(str(oneCount) + " X")
                #sends a message to the console letting the user know the file has been written to
                print("vB_voteOne file has been written to" )
                file1.close()
                
            if(payload.emoji.name == two):
                time.sleep(7)
                #fetches the channel, the message, and the reactions on that message in that particaular channel
                channel = bot.get_channel(payload.channel_id)
                msg = await channel.fetch_message(payload.message_id)
                reaction = get(msg.reactions, emoji = payload.emoji.name)
                #creates a count for the one emojis
                twoCount = reaction.count    
                #assings this count to a text file with the letter Y
                file2.write(str(twoCount) + " Y")
                #sends a message to the console letting the user know the file has been written to
                print("vB_voteTwo file has been written to" )
                file2.close()

#This is the results command            
@bot.command()
async def r(ctx):  
    #defines the emojis 
    one = "1️⃣"
    two = "2️⃣"
    #opens a file at this location, this will need to be changed if used on another machine XXXX
    file1 = open(r"C:\Users\Mattw\Documents\Python programs\Discord_Vote_Bot\vB_voteOne.txt", "r+")
    fCont1 = file1.read()
    fCont1.split
    #opens a file at this location, this will need to be changed if used on another machine XXXX
    file2 = open(r"C:\Users\Mattw\Documents\Python programs\Discord_Vote_Bot\vB_voteTwo.txt", "r+")
    fCont2 = file2.read()
    fCont2.split
    #searches for the letter X and Y if to seee they exist in a text file. Discord.py only saves the biggest number to a text file, so there will only be either an X or a Y in a single text file at one time. UNLESS the reaction count of one's and two's are the same allowing for X and Y to exist at the same time.
    if("X" in fCont1 and "Y" in fCont2):
        #sends a message to say its a tie between one and two
        await ctx.send("It is a tie between {} and {} ".format(one, two))  
        #deletes all info in both files and closes them
        file1.truncate(0)
        file2.truncate(0)
        file1.close()
        file2.close()
        #sends message to console
        print("voting files have been cleared, new poll is ready to begin")
        return
        
    if("X" in fCont1 and "Y" not in fCont2):
        #sends message 
        await ctx.send('The winner is {} with votes of {}'.format(one, fCont1.split()[0]))
        #deletes all info in both files and closes them
        file1.truncate(0)
        file2.truncate(0)
        file1.close()
        file2.close()
        #sends message to console
        print("voting files have been cleared, new poll is ready to begin")
        return

    else:
        #sends message 
        await ctx.send('The winner is {} with votes of {}'.format(two, fCont2.split()[0]))
        #deletes all info in both files and closes them
        file1.truncate(0)
        file2.truncate(0)
        file1.close()
        file2.close()
        #sends message to console
        print("voting files have been cleared, new poll is ready to begin")
        return

#deals with errors
@bot.event
async def on_command_error(ctx, error):
    #if the command is not recongized
    if isinstance(error, commands.errors.CommandNotFound):
       await ctx.reply(f"{ctx.author.name}, Please try typing the command like !vote OPTION OPTION TIME (in seconds)")
    #if the command is entered wrong
    if isinstance(error, commands.errors.MissingRequiredArgument):
       await ctx.reply(f"{ctx.author.name}, Please try typing the command like !vote OPTION OPTION TIME (in seconds)")
    else:
        print("error not caught")
        print(error)


bot.run(TOKEN)
