from models.utility import Utility


class Grenade(Utility):

    def __init__(
        self,
        path,
        title,
        lineup=None,
        description=None
    ):

        super().__init__(path, title)

        self.lineup = lineup
        self.description = description


    def get_caption(self):

        return (
            f"💨 <b>{self.title}</b>\n\n"
            f"🎯 {self.description}"
        )