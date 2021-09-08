import discord
from discord.ext.commands import Cog, Bot, command, Context
from discord.ext.commands.core import group
from discord.ext.commands.errors import BadArgument, CommandError, CommandNotFound
from random import *


class 유용한기능(Cog):

    @command()
    async def 안녕(self, ctx: Context):
        """
        랜덤으로 인사를 한다
        """

        rand = int(random() * 9) + 1

        if rand == 1 or rand == 2:
            await ctx.channel.send("안녕하세요")
        elif rand == 3 or rand == 4:
            await ctx.channel.send("네 왜부르셨나요")
        elif rand == 5 or rand == 6:
            await ctx.channel.send("좋은하루 보내세요")
        elif rand == 7 or rand == 8:
            await ctx.channel.send("https://www.youtube.com/c/곰띠Bearddy 여기 가셈")
        elif rand == 9:
            await ctx.channel.send("대답하기 싫은데..")

    @command()
    async def 채팅청소(self, ctx: Context, count: int):

        """
        채팅청소를 해준다
        """

        if ctx.author.guild_permissions.administrator:
            if count < 2147483647 and count > 0 :
                await ctx.channle.purge(limit=count + 1)
                await ctx.send(str(count) + "개의 메시지를 청소했습니다")
            elif count < 0 or count > 2147483647:
                if count > 2147483647:
                    await ctx.send("그렇게나 많은 메시지를 지울필요는 없어보이는데요?")
                elif count < 0:
                    count *= -1
                    await ctx.purge(limit=count+1)
                    await ctx.send(str(count) + "개의 메시지를 청소했습니다")
        else:
            await ctx.send("관리자 권한이 없습니다!")


    @command(name='투표')
    async def vote_(self, ctx: Context, *, list: str):
        vote_list = list.split("/")
        if(len(vote_list) > 6):
            await ctx.send("투표 항목이 너무 많으면 도배가 될수있으므로 5개 이하로 해주세요")
        else:
            embed = discord.Embed(title="★투표★   ->   " + vote_list[0], description=" ", color=0x00ff00)
            await ctx.send(embed=embed)
            
            for i in range(1, len(vote_list)):
                choose = await ctx.send("```" + str(i) + ". " + vote_list[i] + "```")
                await choose.add_reaction('👍')

    @command()
    async def 도와줘(self, ctx: Context):

        """
        명령어 리스트를 알려준다
        """

        embed = discord.Embed(title="*명령어 리스트*", description="　", color=0x00ffff)

        embed.add_field(name="곰띠님 안녕", value="랜덤으로 다양하게 말합니다", inline=False)
        embed.add_field(name="곰띠님 투표 질문/항목1/항목2/항목3....", value="항목1 ~... 마지막 항목까지 투표를 진행합니다", inline=False)
        embed.add_field(name="곰띠님 채팅청소 [숫자]", value="[숫자] 만큼의 채팅을 지웁니다 (관리자 권한만 사용가능)", inline=False)
        embed.add_field(name="곰띠님 커맨드", value="마크 커맨드에 관한 명령어 리스트를 알려줍니다", inline=False)
        embed.add_field(name="곰띠님 놀아줘", value="놀음거리에 관한 명령어 리스트를 알려줍니다", inline=False)
        

        embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
        embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

        await ctx.send(embed=embed)


    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        if isinstance(error, CommandNotFound):
            await ctx.send('해당 명령어가가 존재하는지 확인해주세요')
        elif isinstance(error, BadArgument):
            await ctx.send('값을 제대로 대입하셨나요?')
        else:
            await ctx.send('명령어 실행중 알수없는 오류가 발생했습니다')
        

def setup(bot: Bot):
    bot.add_cog(유용한기능())