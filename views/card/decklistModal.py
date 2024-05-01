from nextcord.ui import Modal, TextInput

from models.card.decklist import Decklist

class DecklistModal(Modal):
    def __init__(self, bot, channel_id):
        super().__init__("Edit decklist")
        self.bot = bot

        self.name = TextInput(
            "Nom à afficher",
            placeholder="Les decklists des joueurs meilleurs que toi",
            required=True,
        )
        self.msg = TextInput(
            "URL",
            placeholder="https://bestdecklist.cafe/",
            required=True,
        )

        self.add_item(self.name)
        self.add_item(self.msg)

    async def callback(self, interaction):
        try:
            user = interaction.user
            if Decklist(
                self.name.value, self.msg.value, user.name
            ).save():
                return await interaction.response.send_message(
                    f"Decklist updated", ephemeral=True
                )
            else:
                raise Exception("Error while saving")
        except Exception as e:
            return await interaction.response.send_message(
                f"Error : {e}", ephemeral=True
            )
