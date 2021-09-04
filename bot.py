import discord
import asyncio
import os

from functions import *


client = discord.Client()

token = "ODgyNTk2NDQyMzA3NDMyNDg5.YS9r_Q.v3kTFI_0yGR2WfwKMDfAf-vwDmg"

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
        await message.channel.send(embed=cmd_list())

    if message.content == "곰띠님 알려줘 리스트":
        await message.channel.send(embed=tell_list())

    if message.content == "곰띠님 놀아줘 리스트":
        await message.channel.send(embed=play_list())

    if message.content == "곰띠님":
        await message.channel.send(hi_bearddy())

    if message.content.startswith("곰띠님 알려줘 execute"):
        await message.channel.send(embed=cmd_execute_help())

    if message.content.startswith("곰띠님 알려줘 tp"):
        await message.channel.send(embed=cmd_tp_help())

    if message.content.startswith("곰띠님 알려줘 setblock"):
        await message.channel.send(embed=cmd_setblock_help())
    
    if message.content.startswith("곰띠님 놀아줘 랜덤숫자 "):
        await message.channel.send(random_num(message))

    if message.content.startswith("곰띠님 놀아줘 랜덤단어 "):
        await message.channel.send(random_word(message))








client.run(os.environ['bot_token'])

