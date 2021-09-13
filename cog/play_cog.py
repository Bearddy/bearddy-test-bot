import discord
from discord.ext.commands import Cog, Bot, command, Context
from discord.ext.commands.core import group
from random import *

class 놀음거리(Cog):
    @command(name='놀아줘')
    async def 놀아줘_리스트(self, ctx: Context):
        embed = discord.Embed(title="*놀음거리 리스트*", description="　", color=0x00ffff)
            
        embed.add_field(name="곰띠님 랜덤숫자 [숫자1] [숫자2]", value="[숫자1]부터 [숫자2]에서 랜덤으로 하나를 배출합니다", inline=False)
        embed.add_field(name="곰띠님 랜덤단어 단어1/단어2/단어3...", value="단어1, 단어2, 단어3 ..... 중에서 랜덤으로 하나를 배출합니다", inline=False)

        embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
        embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

        await ctx.send(embed=embed)

    @command(name='랜덤숫자')
    async def rand_num_(self, ctx: Context, num1: int, num2: int):
        if num1 < num2:

            if num2 < 2147483647 and num2 > 0 :
                rand = int(random() * (num2 - num1 + 1)) + num1
                await ctx.send(f"{num1}부터 {num2}중에서 랜덤으로 {rand} 이/가 나왔습니다")
            elif num2 < 0 or num2 > 2147483647:
                await ctx.send("0이하의 정수거나 값이 너무 크면 곰띠봇이 힘들어해요 ㅠㅠ")
        else :
            await ctx.send("두번째 숫자가 더작습니다")

    @command(name='랜덤단어')
    async def rand_words_(self, ctx: Context, words: str):
        list = words.split("/")
        rand = int(random() * len(list))

        await ctx.send(f"단어 리스트중에서 \"{list[rand]}\"이/가 나왔습니다")


def setup(bot: Bot):
    bot.add_cog(놀음거리())