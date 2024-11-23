import MathQuestion
import savedata

class PlayerInterface():
    """
    🛡️ The Guardian of the Game Realm 🛡️

    Every ninja starts their journey by stepping into the dojo, and every player begins their adventure by stepping into the realm of Number Ninjas. The PlayerInterface is the gateway for all aspiring ninjas to make their mark, be it by signing up for the first time or by returning to further their quest for knowledge and mastery over numbers.

    As the overseer of entry into the digital dojo, this interface ensures that every ninja's credentials are in order before they embark on their mathematical journey. It's here that heroes are born, and legends begin their path to greatness.
    """
    def __init__(self):
        """
        Initializes a new player instance. This is the foundation upon which every ninja's journey begins.
        """
        pass
    def signup(self, username: str, password: str, email: str, saves: savedata):
        """
        Registers a new ninja in the dojo.

        📝 Parameters:
        - username (str): The chosen name of the ninja, unique and memorable.
        
        - password (str): A secret series of characters, protecting the ninja's identity.
        
        - email (str): The digital pigeon post for all dojo communications.
        
        - saves (savedata): The ancient scrolls where all ninja records are kept.
        """
        pass
    def signin(self, username: str, password: str, saves: savedata):
        """
        Welcomes a returning ninja to the dojo.

        📝 Parameters:
        - username (str): The name under which the ninja's legend has been recorded.
        
        - password (str): The key to unlocking the dojo's gates once more.
        
        - saves (savedata): The archives of achievements and trials faced by the ninja.

        🚪 Step through the gates once more, brave ninja, and resume your quest for wisdom and glory!
        """
        pass

