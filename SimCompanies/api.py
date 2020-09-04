import datetime

class Api:
    """Interact with Sim Companies API."""

    def _about_me_url(self):
         return "https://www.simcompanies.com/api/v2/players/me/"

    def _resources_url(self):
        return "https://www.simcompanies.com/api/v2/resources/"

    def _encyclopedia_resources_url(self):
        return "https://www.simcompanies.com/api/v3/en/encyclopedia/resources/"

    def _buildings_url(self):
        return "https://www.simcompanies.com/api/v2/buildings/1/"

    def _market_ticker(self):
        return self._market_ticker_url_base() + self._market_ticker_date_creator()

    def _market_ticker_url_base(self):
        return "https://www.simcompanies.com/api/v1/market-ticker/" #2020-02-26T17:47:28.155Z

    def _market_ticker_date_creator(self, datetime_isoformat=None):
        if datetime_isoformat == None:
            return datetime.datetime.today().isoformat()

    

    


if __name__ == "__main__":
    api = Api()
