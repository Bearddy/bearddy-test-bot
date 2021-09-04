import discord
import asyncio
import os
from random import *


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
        await message.channel.send("곰띠봇 ===== 테스트 메시지 입니다")

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
    
    if message.content.startswith("곰띠님 놀아줘 랜덤숫자 "):
        await message.channel.send(random_num(message))

    if message.content.startswith("곰띠님 놀아줘 랜덤단어 "):
        await message.channel.send(random_word(message))





def cmd_list():
    embed = discord.Embed(title="*명령어 리스트*", description="　", color=0x00ffff)

    embed.add_field(name="곰띠님", value="랜덤으로 다양하게 말합니다", inline=False)
    
    embed.add_field(name="곰띠님 알려줘 리스트", value="알려줘에 관한 명령어 리스트를 알려줍니다", inline=False)
    embed.add_field(name="곰띠님 놀아줘 리스트", value="놀아줘에 관한 명령어 리스트를 알려줍니다", inline=False)
    

    embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

    return embed


def tell_list():
    embed = discord.Embed(title="*곰띠님 알려줘 리스트*", description="　", color=0x00ffff)
        
    embed.add_field(name="곰띠님 알려줘 execute", value="execute 명령어에 대해 설명합니다", inline=False)
    embed.add_field(name="곰띠님 알려줘 tp", value="tp 명령어에 대해 설명합니다", inline=False)
    

    embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

    return embed


def play_list():
    embed = discord.Embed(title="*곰띠님 놀아줘 리스트*", description="　", color=0x00ffff)
        
    embed.add_field(name="곰띠님 놀아줘 랜덤숫자", value="1부터 설정한 값에서 랜덤으로 하나를 배출합니다", inline=False)
    embed.add_field(name="곰띠님 놀아줘 랜덤단어", value="단어1, 단어2, 단어3 ..... 중에서 랜덤으로 하나를 배출합니다", inline=False)
    

    embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

    return embed


def hi_bearddy():
    rand = int(random() * 8) + 1
    sentece = " "

    if rand == 1 or rand == 2:
        sentence = "안녕하세요"
    elif rand == 3 or rand == 4:
        sentence = "네 왜부르셨나요"
    elif rand == 5 or rand == 6:
        sentence = "좋은하루 보내세요"
    elif rand == 7 or rand == 8:
        sentence = "https://www.youtube.com/c/곰띠Bearddy 여기 가셈"
    elif rand == 9:
        sentence = "대답하기 싫은데.."
    
    return sentence


def cmd_execute_help():
    embed = discord.Embed(title="execute 명령어", description=" ", color=0xff00ff)

    embed.add_field(name="execute as <선택자>", value="뒤에 사용할 @s 를 선택해주는 역할합니다", inline=False)
    embed.add_field(name="execute at <선택자>", value="<선택자>의 좌표를 가져옵니다", inline=False)
    embed.add_field(name="execute positioned <x> <y> <z>", value="xyz를 설정하게 해줍니다 \n물론 상대좌표 시점좌표도 사용가능합니다", inline=False)
    embed.add_field(name="execute rotated as <선택자>   또는   execute rotated <yaw> <pitch>", value="<선택자>의 바라보는 방향을 가져오거나 <yaw> <pitch> 를 가져옵니다  \n이것또한 물론 상대랑 시점좌표도 사용가능합니다", inline=False)
    embed.add_field(name="execute facing entity <선택자>   또는   execute facing <yaw> <pitch>", value="<선택자>를 바라보게하는 방향을 가져오거나 <yaw> <pitch> 쪽을 바라보게하는 방향을 가져옵니다 \n이것또한 상대랑 시점좌표도 사용가능합니다", inline=False)
    embed.add_field(name="execute if [block/blocks/data/entity/predicate/score]", value="뒤에 조건식이 만족하면(True) run 뒤에 명령어를 실행합니다", inline=False)
    embed.add_field(name="execute unless [block/blocks/data/entity/predicate/score]", value="뒤에 조건식이 만족하지않으면(False) run 뒤에 명령어를 실행합니다", inline=False)
    embed.add_field(name="execute anchored [feet/eyes]", value="좌표같은것들을 feet(발) 또는 eyes(눈)을 기초로 하게합니다", inline=False)
    embed.add_field(name="execute align <좌표축>", value="뒤에 좌표축의 값을 정수화 시킵니다", inline=False)
    embed.add_field(name="execute store result [score/bossbar/entity/block/storage]", value="run 뒤에 나온값을 [score/bossbar/entity/block/storage] \n이것들중에 선택하신것에다가 저장합니다", inline=False)
    embed.add_field(name="execute store success [score/bossbar/entity/block/storage]", value="run 뒤가 참이면 [score/bossbar/entity/block/storage] \n이것들중에 선택하신것에다가 1을 저장합니다 \n거짓이면 0을 저장합니다", inline=False)

    embed.set_footer(text="오류가있을시 곰띠/Bearddy#4453 로 해주세요")
    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

    return embed


def cmd_tp_help():
    embed = discord.Embed(title="tp 명령어", description=" ", color=0xff00ff)

    embed.add_field(name="tp [상대좌표/상대좌표]", value="실행자를 상대좌표 또는 시점좌표로 계산해서 나온결과로 이동시킵니다", inline=False)
    embed.add_field(name="tp <선택자> [상대좌표/상대좌표]", value="<선택자>를 상대좌표 또는 시점좌표로 계산해서 나온결과로 이동시킵니다", inline=False)
    embed.add_field(name="tp <선택자1> <선택자2>", value="<선택자1>을 <선택자2>의 좌표와 바라보는방향으로 이동시킵니다", inline=False)
    embed.add_field(name="tp <선택자> [상대좌표/상대좌표] <yaw> <pitch>", value="<선택자>를 상대좌표 또는 시점좌표로 계산해서 나온결과로 이동시키고<yaw> <pitch>로 방향을 바꿉니다 ", inline=False)
    embed.add_field(name="tp <선택자> [상대좌표/상대좌표] <yaw> <pitch>", value="<선택자1>이 상대좌표 또는 시점좌표로 계산해서 나온결과로 이동시키고 <선택자2>를 바라보게 만듭니다", inline=False)

    embed.set_footer(text="오류가있을시 곰띠/Bearddy#4453 로 해주세요")
    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

    return embed


def random_num(message):
    answer = " "
    num = int(message.content[13:])
    if num < 2147483647 and num > 0 :
        rand = int(random() * num) + 1
        answer = "1 부터 " + str(num) + " 중에서 랜덤으로 " + str(rand) + "이/가 나왔습니다"
    elif num < 0 or num > 2147483647:
        answer = "0이하의 정수거나 값이 너무 크면 곰띠봇이 힘들어해요 ㅠㅠ"

    return answer


def random_word(message):
    answer = " "
    arr_list = str(message.content[13:])
    list = arr_list.split(', ')
    rand = int(random() *len(list))

    answer = "단어 리스트중에서 \"" + list[rand] + "\"이/가 나왔습니다"

    return answer


client.run(os.environ['bot_token'])

