import nextcord

from config import DUELIT_ID


class StartTournamentView(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    async def set_duelist_role(self, interaction : nextcord.Interaction):
        role_id = int(DUELIT_ID)
        role = interaction.guild.get_role(role_id)
        assert isinstance(role,nextcord.Role)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("tu t'es DESINSCRIT du tournoi", ephemeral = True)
        else : 
            await interaction.user.add_roles(role)
            await interaction.response.send_message("tu es INSCRIT pour le tournoi", ephemeral = True)


    @nextcord.ui.button(label="je participe", style=nextcord.ButtonStyle.primary)
    async def participate_button(self,button,interaction):
        await self.set_duelist_role(interaction)