#!/usr/bin/env python
# coding: utf-8

from random import choice

wer = ("ich", "Du", "das aufblasbare Schaf", "deine Mutter", "sie")
wie = ("zärtlich", "fest", "brutal", "schlecht", "angewidert", "lustig")
wo = ("Nippel", "Penis", "Pussy", "Schenkel", "Bauch", "Po", "Bauchnabel", "Ohrläppchen", "Nacken", "Hals", "kleiner Zeh")
was = ("küssen", "saugen", "lecken", "knabbern", "streicheln", "kitzeln", "schlagen", "foltern")
ort = ("in der Küche", "im Wohnzimmer", "im Aufzug", "im Bürgeramt", "auf dem Klo", "im Bett", "draußen", "im Türrahmen", "an den Dachbalken", "im Flur", "auf dem Balkon")
mod = ("Los!", "Zehn Minuten!", "Juhu!", "Okay.")

print "L I E B E S W Ü R F E L\n"

wers = choice(wer)
wers = wers[0].capitalize() + wers[1:]
print "%(wer)s %(ort)s: %(wie)s %(wo)s %(was)s. %(mod)s" % {"wer": wers, "ort": choice(ort), "wie": choice(wie), "wo": choice(wo), "was": choice(was), "mod": choice(mod)}
