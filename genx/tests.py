from django.test import TestCase
import genx.models as gen


class TestType(TestCase):
    def test_get_damage(self):
        self.red_level = 75
        self.red_attack = 123
        self.blue_defence = 163
        self.red_move_base = 65
        self.red_modifier = 6.00

        damage = gen.get_damage(red_level=self.red_level, red_attack=self.red_attack,
                                     blue_defence=self.blue_defence, red_move_base=self.red_move_base,
                                     red_modifier=self.red_modifier)
        # (((((2 * level) + 10) / 250) * (attack / defence) * base) + 2) * modifier
        # (((((2 * 75) + 10) / 250) * (123 / 163) * 65) + 2) * 6 = ((16 / 25) * (123/ 163) * 65) + 2 = 200
        self.assertEqual(int(damage), 200)