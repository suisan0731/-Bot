import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#envファイル読み込み
load_dotenv()

#環境変数を変数に読み込み
TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

#送信するテキストチャンネル指定
send_to_channel = int(os.environ["SEND_CHANNEL"])

#Botを動かすギルド指定
my_guild = int(os.environ["MY_GUILD"])


@bot.event
async def on_voice_state_update(member, before, after):

    #入退室に関係ない処理をスルー and 該当ギルドだけ処理をする
    if before.channel != after.channel and my_guild == member.guild.id:
        print("enter or leave")

        #入室
        if before.channel is None:
            print(f"{member.name} left from {after.channel}")
            message = f"```{member.name}が入室しました。```"
        
        #退室
        if after.channel is None:
            print(f"{member.name} left from {before.channel}")
            message = f"```{member.name}が退室しました。```"
        
        #メッセージを送信
        for channel in bot.get_all_channels():
            print(channel.id)
            if channel.id == send_to_channel:
                print("send message")
                await channel.send(message)


bot.run(TOKEN)