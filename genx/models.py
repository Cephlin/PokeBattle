import numpy


def get_damage(red_level, red_attack, blue_defence, red_move_base, red_modifier):
    # Check for doubles only
    damage_part1 = ((2.0 * float(red_level)) + 10.0) / 250.0
    damage_part2 = float(red_attack) / float(blue_defence)

    damage = ((damage_part1 * damage_part2 * float(red_move_base)) + 2.0) * float(red_modifier)
    return damage


def get_modifier(stab, type, critical, other):
    #  Other means:
    modifier = stab * type * critical * other * numpy.random.uniform(0.85, 1.0)
    return modifier


def calc_hp(base_stat, iv, ev, level):
    hp = int(calc_stat_part(base_stat, iv, ev, level) + float(level) + 10.0)
    return hp


def calc_other_stat(base_stat, iv, ev, level):
    stat = int(calc_stat_part(base_stat, iv, ev, level) + 5.0)
    return stat


def calc_stat_part(base_stat, iv, ev, level):
    part1 = (float(base_stat) + float(iv)) * 2.0
    part2 = numpy.sqrt(numpy.absolute(float(ev))) / 4.0
    part3 = part1 + part2
    part4 = part3 * level / 100.0
    return part4