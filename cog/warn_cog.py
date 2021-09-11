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
    async def 경고해줘(self, ctx, user:discord.User, amount: int, *, reason):
        if ctx.author.guild_permissions.administrator:
            if not user.guild_permissions.administrator:
                if not reason:
                    await ctx.send("사유를 적으세요")
                    return

                reason = ' '.join(reason)

                for current_user in report['users']:
                    if current_user['id'] == user.id:
                        current_user['warn_count'] += amount
                        current_user['reasons'].append(reason)
                        
                        if current_user['kicked'] == False and current_user['warn_count'] > 3 and current_user['warn_count'] < 7:
                            await user.send(f"경고 횟수가 4번이 됬으므로 \"{ctx.message.guild.name}\" 에서 강퇴 당하셨습니다")
                            await user.kick(reason=f"경고 횟수가 4번이 됬으므로 \"{ctx.message.guild.name}\" 에서 강퇴 당하셨습니다")
                            current_user['kicked'] = True
                        if current_user['warn_count'] > 6:
                            await user.send(f"경고 횟수가 7번이 됬으므로 \"{ctx.message.guild.name}\" 에서 밴 당하셨습니다")
                            await user.ban(reason=f"경고 횟수가 7번이 됬으므로 \"{ctx.message.guild.name}\" 에서 밴 당하셨습니다")
                            current_user['warn_count'] = 0
                            current_user['kicked'] = False
                        
                        await ctx.send(f"성공적으로 {user.name}에게 {amount}개의 경고를 부여했습니다")
                        await ctx.send(f"{user.name}님의 경고 횟수 : {current_user['warn_count']}번")

                        break
                else:
                    report['users'].append({
                    'id':user.id,
                    'warn_count':amount,
                    'kicked':False,
                    'reasons': [reason,]
                    })
                    await ctx.send(f"성공적으로 {user.name}에게 {amount}개의 경고를 부여했습니다")
                    await ctx.send(f"{user.name}님의 경고 횟수 : {amount}번")

                
                
                with open('reports.json','w+') as f:
                    json.dump(report,f)
            else:
                await ctx.send("관리자권한이 있는사람한테는 경고를 못줍니다!")
        else:
            await ctx.send("관리자 권한이 없습니다!")

    @command(pass_context = True)
    async def 경고확인(self, ctx, user:discord.User):
        for current_user in report['users']:
            if user.id == current_user['id']:
                if not current_user['warn_count'] == 0:
                    embed = discord.Embed(title=f"{user.name}님의 경고판", description="　", color=0xff0000)
                    
                    embed.add_field(name="경고 횟수 : ", value=f"{current_user['warn_count']}번", inline=False)
                    embed.add_field(name="경고 사유:", value=f"{','.join(current_user['reasons'])}", inline=False)
                    
                    embed.set_footer(text="버그제보는 곰띠/Bearddy#4453 로 해주세요", icon_url="https://ifh.cc/g/nxRpdO.png")
                    embed.set_thumbnail(url="https://ifh.cc/g/5LIwNe.jpg")

                    await ctx.send(embed=embed)
                    break   
                else:
                    await ctx.send(f"{user.name}님은 경고가 없는 클린한 사람입니다") 
        else:
            await ctx.send(f"{user.name}님은 경고가 없는 클린한 사람입니다") 


    @command(pass_context = True)
    async def 경고제거(self, ctx, user: discord.User, amount: int):
        if ctx.author.guild_permissions.administrator:
            if not user.guild_permissions.administrator:
                for current_user in report['users']:
                    if current_user['id'] == user.id:
                        if (current_user['warn_count'] - amount) < 0:
                            await ctx.send(f"성공적으로 {user.name}의 경고횟수에서 {current_user['warn_count']}을/를 뺐습니다")
                            current_user['warn_count'] = 0
                            
                        else:
                            current_user['warn_count'] -= amount
                            await ctx.send(f"성공적으로 {user.name}의 경고횟수에서 {amount}을/를 뺐습니다")

                        await ctx.send(f"{user.name}님의 경고 횟수 : {current_user['warn_count']}번")
                        break
                else:
                    await ctx.send(f"{user.name}님은 아직 경고당한적이 없습니다")

                with open('reports.json','w+') as f:
                    json.dump(report,f)
            else:
                await ctx.send("관리자권한이 있는 사람은 애초에 경고가 없습니다!")
        else:
            await ctx.send("관리자 권한이 없습니다!")


def setup(bot: Bot):
    bot.add_cog(경고명령어())
