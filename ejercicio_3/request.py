import requests

url = "http://www.thecocktaildb.com/api/json/v1/1/search.php"

http_rsp = requests.get(url, params = {'s': 'margarita'})

rsp_json = http_rsp.json()

print(rsp_json)
print(type(rsp_json))

print(rsp_json['drinks'][0]['idDrink'])

class Drinks:
    def __init__(self, title, strAlcoholic, strInstructions):
        self.title = title
        self.strAlcoholic = strAlcoholic
        self.strInstructions = strInstructions

    def __str__(self) -> str:
        return f'{self.title}, {self.strAlcoholic}, {self.strInstructions}'

drink_type = input('Drink: >> ')

req_params = {'s': drink_type}

http_rsp = requests.get(url, params = req_params)

print(http_rsp.json())