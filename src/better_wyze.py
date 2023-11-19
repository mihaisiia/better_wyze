import os
from glob import glob
from wyze_sdk import Client

class BetterWyze:
    def __init__(self) -> None:
        self.client = Client()
        self._bulbs = []

    # Login and generate tokens
    def _login_and_generate_tokens(self):
        response = self.client.login(
            email=os.getenv('WYZE_EMAIL'), 
            password=os.getenv('WYZE_PASSWORD'),
            key_id=os.getenv('WYZE_API_KEY_ID'), 
            api_key=os.getenv('WYZE_API_KEY'))
        os.environ["WYZE_ACCESS_TOKEN"] = f"{response['access_token']}"
        os.environ["WYZE_REFRESH_TOKEN"] = f"{response['refresh_token']}"
        with open("./access.token","w") as file:
            file.write(response['access_token'])
        with open("./refresh.token", "w") as file:
            file.write(response['refresh_token'])

    def login(self):
        # Get stored tokens if they exist
        token_files = glob("*.token")
        for token_file in token_files:
            token_env_var_name = "WYZE_" + token_file.replace(".","_").upper()
            with open(token_file) as file:
                token = file.readline()
                os.environ[token_env_var_name] = token

        # Use stored tokens if they exist
        self.client._update_session(
            access_token=os.environ["WYZE_ACCESS_TOKEN"],
            refresh_token=os.environ["WYZE_REFRESH_TOKEN"])
        
        # Test tokens, try to generate new ones if they fail
        try:
            print(self.client.user_get_info())
        except Exception as e:
            self.client = Client()
            self._login_and_generate_tokens()

    def get_devices(self):
        self._bulbs = self.client.bulbs.list()

    def turn_on_lights(self):
        for bulb in self._bulbs:
            # print(bulb.mac, bulb.product.model)
            self.client.bulbs.turn_on(device_mac=bulb.mac, device_model=bulb.product.model)
            # self.client.bulbs.turn_on(bulb.mac, bulb.parent_device)

    def turn_off_lights(self):
        for bulb in self._bulbs:
            self.client.bulbs.turn_off(device_mac=bulb.mac, device_model=bulb.product.model)
