from discord import ButtonStyle
from nextcord.ui import View, Button

from models.game.player import Player

class RegisterView(View):
    class JoinButton(Button):

        def __init__(self,emoji):

            super().__init__(label="JOIN !",style=ButtonStyle.blurple,emoji=emoji)

        async def callback(self,interaction):

            if not [p for p in self.view.players if p.member.id == interaction.user.id] :
                player = Player(interaction.user)
                dm_url = await player.get_dm_url()
                self.view.players.append(player)

                await interaction.response.send_message(f"Tu as été ajouté au jeu\nDès que le jeu commencera j'enverai les questions en mp ➡️ {dm_url} ⬅️\nTiens toi prêt !\n",ephemeral=True)

                await self.update_message()

        async def update_message(self):
            
            msg = 'Player :\n'

            for player in self.view.players:
                msg += str(player) + "\n"

            await self.view.message.edit(msg)

    def __init__(self,players,emoji,message) -> None: 
        self.players = players
        self.emoji = emoji
        self.message = message
        super().__init__(timeout=None)

        self.add_item(self.JoinButton(emoji))