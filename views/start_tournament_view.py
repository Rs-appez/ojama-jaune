import nextcord
from nextcord.ext import commands
from config import DUELIST_ID, TEAM_ID


class StartTournamentView(nextcord.ui.View):

    def __init__(self, msg_nb_participant):
        self.msg_nb_participant = msg_nb_participant
        super().__init__()

    async def set_duelist_role(self, interaction : nextcord.Interaction):

        role_id = int(DUELIST_ID)
        role = interaction.guild.get_role(role_id)
        assert isinstance(role,nextcord.Role)

        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message("tu t'es DESINSCRIT du tournoi", ephemeral = True)
        else : 
            await interaction.user.add_roles(role)
            await interaction.response.send_message("tu es INSCRIT pour le tournoi", ephemeral = True)
        
        members = interaction.guild.members
        nb_participant = 0

        for member in members:
            
            if(role in member.roles):
                nb_participant += 1
        await self.msg_nb_participant.edit(content=f"Participant : {nb_participant}")


    @nextcord.ui.button(label="je participe", style=nextcord.ButtonStyle.primary)
    async def participate_button(self,button,interaction):
        await self.set_duelist_role(interaction)


