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
    
    if message.content.startswith("곰띠님 투표해줘 "):
        
        vote_list = message.content[9:].split("/")
        if(len(vote_list) > 6):
            await message.channel.send("투표 항목이 너무 많으면 도배가 될수있으므로 5개 이하로 해주세요")
        else:
            embed = discord.Embed(title="★투표★   ->   " + vote_list[0], description=" ", color=0x00ff00)
            await message.channel.send(embed=embed)
            
            for i in range(1, len(vote_list)):
                choose = await message.channel.send("```" + str(i) + ". " + vote_list[i] + "```")
                await choose.add_reaction('👍')
        



client.run(os.environ['bot_token'])


