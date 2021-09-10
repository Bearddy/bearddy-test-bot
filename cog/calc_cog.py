from discord.ext.commands import Cog, Bot, command, Context
from discord.ext.commands.core import group

class 계산기(Cog):
    @group()
    async def 계산기(self, ctx: Context):
        '''
        곰띠봇이 계산해줍니다
        '''

    @계산기.command()
    async def 더하기(self, ctx: Context, *, nums: str): 
        num_list = nums.split(' ')
        answer = 0
        for i in range(len(num_list)):
           
            answer += int(num_list[i])

        
        await ctx.send(f"전부 더한값은 {answer}입니다")

    @계산기.command()
    async def 빼기(self, ctx: Context, *, nums: str): 
        num_list = nums.split(' ')
        answer = 0
        for i in range(len(num_list)):
           
            answer -= int(num_list[i])

        
        await ctx.send(f"전부 뺸값은 {answer}입니다")

    @계산기.command()
    async def 곱하기(self, ctx: Context, *, nums: str): 
        num_list = nums.split(' ')
        answer = 1
        for i in range(len(num_list)):
           
            answer *= int(num_list[i])

        
        await ctx.send(f"전부 곱한값은 {answer}입니다")

    @계산기.command()
    async def 나누기(self, ctx: Context, *, nums: str): 
        num_list = nums.split(' ')
        answer = 1
        for i in range(len(num_list)):
           
            answer /= int(num_list[i])

        
        await ctx.send(f"전부 나눈값은 {answer}입니다")
    

def setup(bot: Bot):
    bot.add_cog(계산기())