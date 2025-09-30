import discord
from discord.ext import commands
from config import TOKEN
from logic import sorular

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

@bot.command()
async def start(ctx):
    """Bot kendini tanıtır."""
    await ctx.send("Merhaba! Ben **Alabileceğin Her Şey** mağazasının teknik destek botuyum. "
                   "Sorularınızı `!sor <soru>` şeklinde sorabilirsiniz.")

@bot.command()
async def sor(ctx, *, soru):
    """Hazır sorulara cevap verir."""
    
    soru_lower = soru.lower()  # Kullanıcının sorusunu küçük harfe çevir

    # Küçük harfli sözlük oluştur
    sorular_lower = {key.lower(): value for key, value in sorular.items()}

    if soru_lower in sorular_lower:
        await ctx.send(sorular_lower[soru_lower])
    else:
        await ctx.send("Bu soruya cevap veremiyorum.")


bot.run(TOKEN)