from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from character.models import Character


FIELDS = {
        "name": "name",
        "t": "character_type",
        "hp": "hit_points",
        "ac": "armor_class",
        "str": "strength",
        "dex": "dexterity",
        "con": "constitution",
        "int": "intelligence",
        "wis": "wisdom",
        "cha": "charisma",
        }

def character(request):
    text = ""

    if request.POST:
        text = body.POST.get("text")
        print ("text1", text)
    else:
        body = json.loads(request.body.decode(encoding='UTF-8'))
        text = body.get("text", "")
        print ("text2", text)
    words = text.split(" ")
    new_char = Character()

    for x, word in enumerate(words):
        if (x % 2 == 0 and word in FIELDS):
            if word in ("hp", "ac"):
                setattr(new_char, FIELDS[word], int(words[x + 1]))
            else:
                setattr(new_char, FIELDS[word], str(words[x + 1]))

    new_char.save()
    json_char = json.dumps(model_to_dict(new_char))

    return JsonResponse({
        "response_type": "in_channel",
        "text": "you entered {}".format(json_char),
        })
