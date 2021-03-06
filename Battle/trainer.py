from Pockemon_Battle.Battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        for p in self.pokemon:
            if p.name == pokemon_name:
                self.pokemon.remove(p)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for pok in self.pokemon:
            res += pok.pokemon_details()
        return res

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
