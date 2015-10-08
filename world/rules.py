from random import randint

def roll_skill(character, skill):
    attributes = character.get_attributes()
    skill_value = attributes[skill]

    skill_value = skill_value / 40

    if skill_value < 1:
        skill_value = 1

    return randint(skill_value, skill_value * 100)