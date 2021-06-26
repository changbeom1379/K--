import discord
import asyncio

from discord import embeds

client = discord.Client()

token = "ODUzOTgzNjUwMDczMTQ5NDUw.YMdUQA.M7pTmzDQd1pPPcBvMmJBTEDgvcE"

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('저는 K-비온 구독자들 서버의 충실한 봇입니다')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):

    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="봇 제작자 : 서창범 #1437")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

    if message.content == "안녕 K-비봇":
        embed = discord.Embed(title="K-비봇", description="안녕하세요 저는 K-비봇입니다", color=0x00ff00)
        embed.set_image(url="https://cdn.discordapp.com/attachments/843487502136508438/857981831542472735/K-_2.gif")
        await message.channel.send(embed=embed)

    if message.content == "!기능 소개":
        embed = discord.Embed(Timestamp=message.created_at, colour=discord.Colour.red(), title= "기능")
        embed.add_field(name="기능 목록", value="채팅 청소 ㅣ 사용법 : 청소(숫자)", inline=False)
        await message.channel.send(embed=embed)
        

client.run(token)