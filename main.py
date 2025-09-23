from config import TOKEN
import discord
#import komutları eklenecek






                   
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

@bot.command()
async def start(ctx):
    await ctx.send(f"Merhaba, {ctx.author.name}, Alabileceğin Her Şey mağazasının teknik destek botuna hoş geldin! Sormak istediğin soruları bana sorabilirsin.")











 
bot.run(TOKEN)