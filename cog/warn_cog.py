import discord
from discord.ext.commands import Cog, Bot, command
import json

with open('reports.json', encoding='utf-8') as f:
    try:
        report = json.load(f)
    except ValueError:
        report = {}
        report['users'] = []

class 경고명령어(Cog):

    @command(pass_context = True)
    async def 경고해줘(self, ctx, user:discord.User, *, reason:str):
        
        if not reason:
            await ctx.send("사유를 적으세요")
            return

        reason = ' '.join(reason)

        for current_user in report['users']:
            if current_user['id'] == user.id:
                current_user['reasons'].append(reason)
                break
        else:
            report['users'].append({
            'id':user.id,
            'reasons': [reason,]
            })
        await ctx.send(f"성공적으로 {user.name}에게 경고를 부여했습니다")
        await ctx.send(f"{user.name}님의 경고 횟수 : {len(current_user['reasons'])}")
        
        with open('reports.json','w+') as f:
            json.dump(report,f)

    @command(pass_context = True)
    async def 경고확인(self, ctx, user:discord.User):
        for current_user in report['users']:
            if user.id == current_user['id']:

                warn_list = (','.join(current_user['reasons'])).split(',')

                embed = discord.Embed(title=f"{user.name}님의 경고판", description="　", color=0xff0000)
                
                embed.add_field(name="경고 횟수 : ", value=f"{len(current_user['reasons'])}번", inline=False)
                for i in range(len(current_user['reasons'])):
                    embed.add_field(name=f"경고 사유 {i+1}:", value=f"{warn_list[i]}", inline=False)
                
                embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
                embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

                await ctx.send(embed=embed)
                break
        else:
            await ctx.send(f"{user.name}님은 경고가 없는 클린한 사람입니다")  


def setup(bot: Bot):
    bot.add_cog(경고명령어())
