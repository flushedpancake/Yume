# Bibliotecas utilizadas neste arquivo
from utils.embeds import InfoEmbed
from discord.ext import commands
from discord import app_commands
from utils import modals
import discord


# Realiza a definição da classe cog
class Dreams(commands.GroupCog, name='yume'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Yume is currently dreaming....')

    # Verify
    @app_commands.command(name='status', description="Check if I'm doing okay...")
    async def verify(self, interaction: discord.Interaction):

        await interaction.response.send_message('Everything seems fine! Thanks for checking up on Yume~ <3', ephemeral=True)

    # Information
    @app_commands.command(name='info', description="Yume's information, links, etc.")
    async def info(self, interaction: discord.Interaction):

        await interaction.response.send_message(embed=InfoEmbed.iembed, ephemeral=True)

    # Typo Report
    @app_commands.command(name='typo', description="Report any typos in commands here...")
    async def typo(self, interaction: discord.Interaction):

        typo = modals.TypoModal()
        await interaction.response.send_modal(typo)

    # Suggestions
    @app_commands.command(name='suggestion', description="Give Yume's developer your suggestions!")
    async def suggestion(self, interaction: discord.Interaction):

        suggestion = modals.SuggestionModal()
        await interaction.response.send_modal(suggestion)

    # Chat Restriction


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Dreams(yume))
