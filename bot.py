import discord
import asyncio
import os

from functions import *

client = discord.Client()


@client.event
async def on_ready():
    
    print(client.user.name)
    print('봇이 시작됨')
    game = discord.Game('곰띠가 오프라인일때 "곰띠님 도와줘"를 입력해보세요')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    
    if message.content == "곰띠봇 테스트메시지":
        await message.channel.send("곰띠봇 ===== //////// ------ 테스트 메시지 입니다")

    if message.content == "곰띠님 도와줘":
        cmd_list(message)

    if message.content == "곰띠님 알려줘 리스트":
        tell_list(message)

    if message.content == "곰띠님 놀아줘 리스트":
        play_list(message)

    if message.content == "곰띠님":
        hi_bearddy(message)

    if message.content.startswith("곰띠님 알려줘 execute"):
        cmd_execute_help(message)

    if message.content.startswith("곰띠님 알려줘 tp"):
        cmd_tp_help(message)

    if message.content.startswith("곰띠님 알려줘 setblock"):
        cmd_setblock_help(message)
    
    if message.content.startswith("곰띠님 놀아줘 랜덤숫자 "):
        random_num(message)

    if message.content.startswith("곰띠님 놀아줘 랜덤단어 "):
        random_word(message)
    
    if message.content.startswith("곰띠님 투표해줘 "):
        vote(message)



client.run(os.environ['bot_token'])

