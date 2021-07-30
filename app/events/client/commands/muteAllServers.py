import discord
import asyncio

from app.vars.client import client
from app.helpers import sendEmbed
    
@client.command(aliases=['muteServerList', 'mas', 'forceMuteServers'])
async def muteAllServers(ctx):
    muted_servers = 0
    Embed = discord.Embed(description=f"> Servers mutated until now: **{int(muted_servers)}** / **{len(client.guilds)}**.\n> Current Status: **Starting...**", color=discord.Colour.blue())
    Message = await sendEmbed(ctx, Embed)
    for guild in client.guilds:
        try:
            await guild.mute()
            muted_servers = muted_servers + 1

            if (Message.embeds):
                Embed = discord.Embed(description=f"> Servers mutated until now: **{int(muted_servers)}** / **{len(client.guilds)}**.\n> Current Status: **In progress...**", color=discord.Colour.orange())
                await Message.edit(embed=Embed)
            else:
                await Message.edit(f"> Servers mutated until now: **{int(muted_servers)}** / **{len(client.guilds)}**.\n> Current Status: **Starting...**")

            await asyncio.sleep(0.3)
        except:
            pass

    if (Message.embeds):
        Embed = discord.Embed(description=f"> Total number of mutated servers: **{int(muted_servers)}** / **{len(client.guilds)}**.\n> Current Status: **All Done!**", color=discord.Colour.green())
        await Message.edit(embed=Embed)
    else:
        await Message.edit(f"> Total number of mutated servers: **{int(muted_servers)}** / **{len(client.guilds)}**.\n> Current Status: **All done!**")

    return