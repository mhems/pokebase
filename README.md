# Pokebase [![swampert](https://veekun.com/dex/media/pokemon/main-sprites/heartgold-soulsilver/260.png)](https://pokeapi.co/api/v2/pokemon/swampert)

My modifications to `pokebase`: "a simple but powerful Python interface to the [PokeAPI database](https://pokeapi.co/)"

Mainly the option to avoid fetching certain fields which lend to very long (and large) responses.
e.g. to get a single Pokemon, all moves that this pokemon knows are recursively fetched
If I just want the types or stats, I don't want the other data to be fetched.

Refer to the [original repo](https://github.com/PokeAPI/pokebase) for docs.

This is provided as-is for my own use.