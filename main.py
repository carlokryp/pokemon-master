#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pokemon.pokemon as pokemon
import makepdf.makepdf as makepdf


if __name__ == "__main__":
    tipos = pokemon.get_pokemontypes()
    resp = pokemon.get_onetype(tipos)
    equipo = pokemon.get_pokemon_user(resp)
    makepdf.hazcarta(tipos, resp, equipo)
