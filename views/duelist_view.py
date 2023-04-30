

import nextcord
from config import ADMIN_SPEED, TEAM_ID

from models.tournament.tournament import Tournament

class DuelistView(nextcord.ui.View):

    def __init__(self,ctx, tournament : Tournament):
        self.ctx = ctx
        self.tournament = tournament
        super().__init__()


    async def start(self):
       await self.tournament.start()

    @nextcord.ui.button(label="commencer le tournoi",emoji="✅" ,style=nextcord.ButtonStyle.primary, disabled=False)
    async def participate_button(self,button : nextcord.ui.Button ,interaction):

        user = interaction.user
        role_id = int(TEAM_ID)
        role_id_speed = int(ADMIN_SPEED)

        if interaction.guild.get_role(role_id):
            role = interaction.guild.get_role(role_id)
        
        elif interaction.guild.get_role(role_id_speed):
            interaction.guild.get_role(role_id_speed)
            
        assert isinstance(role,nextcord.Role)

        if role in user.roles:
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await self.start()

