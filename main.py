import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix="", case_insensitive=True)

@bot.command(pass_context = True, name='randomSite', description="Tell the user a random site.")
@bot.event
async def on_message(message):
    print(message.content)
    if 'random site' in str(message.content).lower():
        sitesRandom = [
            'http://burymewithmymoney.com/',
		    'http://www.fallingfalling.com/',
	    	'http://ducksarethebest.com/',
		    'http://www.trypap.com/',
	    	'http://www.republiquedesmangues.fr/',
	    	'http://www.movenowthinklater.com/',
	    	'http://www.partridgegetslucky.com/',
	    	'http://www.rrrgggbbb.com/',
	    	'http://beesbeesbees.com/',
	    	'http://www.koalastothemax.com/',
	    	'http://www.everydayim.com/',
	    	'http://www.leduchamp.com/',
	    	'http://grandpanoclothes.com/',
	    	'http://www.haneke.net/',
	    	'http://r33b.net/',
	    	'http://randomcolour.com/',
		    'http://cat-bounce.com/',
		    'http://cachemonet.com/',
	    	'http://www.sadforjapan.com/',
	    	'http://www.taghua.com/',
	    	'http://chrismckenzie.com/',
	    	'http://hasthelargehadroncolliderdestroyedtheworldyet.com/',
	    	'http://ninjaflex.com/',
	    	'http://ihasabucket.com/',
	    	'http://corndogoncorndog.com/',
		    'http://www.ringingtelephone.com/',
		    'http://www.pointerpointer.com/',
	    	'http://www.pleasedonate.biz/',
	    	'http://imaninja.com/',
	    	'http://willthefuturebeaweso.me/',
		    'http://salmonofcapistrano.com/',
		    'http://www.ismycomputeron.com/',
	    	'http://www.wwwdotcom.com/',
		    'http://www.nullingthevoid.com/',
	    	'http://www.muchbetterthanthis.com/',
	    	'http://www.ouaismaisbon.ch/',
	    	'http://iamawesome.com/',
	    	'http://www.pleaselike.com/',
	    	'http://crouton.net/',
	    	'http://corgiorgy.com/',
	    	'http://www.electricboogiewoogie.com/',
	    	'http://www.wutdafuk.com/',
	    	'http://unicodesnowmanforyou.com/',
	    	'http://tencents.info/',
	    	'http://intotime.com/',
		    'http://leekspin.com/',
		    'http://minecraftstal.com/',
	    	'http://www.patience-is-a-virtue.org/',
	    	'http://whitetrash.nl/',
		    'http://zombo.com',
	    	'http://secretsfornicotine.com/',
	    	'http://pixelsfighting.com/',
	    	'http://isitwhite.com/',
	    	'http://noot.space/',
	    	'http://hardcoreprawnlawn.com/',
		    'http://www.omfgdogs.com/']
        await message.reply(random.choice(sitesRandom))
        
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Talk with TheOrtsac#0087 for suggestions!", url="https://www.twitch.tv/theortsac"))
bot.run('Bot Token')
