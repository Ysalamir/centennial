from random import randint

def roll_skill(character, skill):
    attributes = character.get_attributes()
    skill_value = attributes[skill]

    skill_value = skill_value / 40

    if skill_value < 1:
        skill_value = 1

    return randint(skill_value, skill_value * 100)


def challenge_skill(challenger, defender, cSkill, dSkill):
    cAttributes = challenger.get_attributes()
    dAttributes = defender.get_attributes()

    cSkill_value = cAttributes[cSkill]
    dSkill_value = dAttributes[dSkill]

    result = (cSkill_value - dSkill_value) / 40

    if result < 1:
        result = 1

    return randint(result, result * 100)