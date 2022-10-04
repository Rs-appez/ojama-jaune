from re import T
import nextcord
from nextcord.ext import commands
from nextcord.interactions import Interaction

from models.cards import Cards


class RullingView(nextcord.ui.View):

    def __init__(self, card : Cards):
        self.card = card
        super().__init__()

    @nextcord.ui.button(label="Voir rulling", style=nextcord.ButtonStyle.primary)
    async def view_rulling(self, button, interaction : Interaction):
        await interaction.response.defer(with_message=True)
        await self.card.rulling(interaction)
        


