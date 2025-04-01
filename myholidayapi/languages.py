from myholidayapi.client import HolidayAPIClient


class Languages:
    def __init__(self, client: HolidayAPIClient) -> None:
        self.client = client

    def get(self) -> dict:
        '''

        :return: json formatted holidays

        lalalalallala
        '''
        # params = {
        #     "country": country,
        #     "year": year}
        params = {}
        response = self.client.request("/languages", params=params)['languages']
        return response