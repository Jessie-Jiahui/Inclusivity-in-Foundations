from final_proj import *
from final_plot import *
import unittest

class TestFoundation(unittest.TestCase):

    # def foundation_is_in_foundation_diction(self, foundation_name, foundation_diction):
    #     for f in foundation_diction:
    #         if foundation_name == f.foundation_name:
    #             return True
    #         return False

    # def get_foundation_from_diction(self, foundation_name, foundation_diction):
    #     for f in foundation_diction:
    #         if foundation_name == f.foundation_name:
    #             return f
    #     return None

    def setUp(self):
        self.esteelauder_doublewear = esteelauder_doublewear_data

    def test_scraped_number(self):
        self.assertEqual(self.esteelauder_doublewear.url, "https://www.esteelauder.com/product/643/22830/product-catalog/makeup/face/foundations/double-wear/stay-in-place-makeup")
        self.assertEqual(list(self.esteelauder_doublewear.years_diction.keys()), ["2013", "2015", "2016", "2018.3", "2018.7"])

    def test_str(self):
        self.assertEqual(str(self.esteelauder_doublewear.__str__()), "The data is for esteelauder_doublewear.")


class TestColorSearch(unittest.TestCase):

    def color_is_in_color_list(self, color_name, color_code, color_list):
        for c in color_list:
            if color_name == c.color_name and color_code == c.color_code:
                return True
        return False

    def get_color_from_list(self, color_name, color_list):
        for c in color_list:
            if color_name == c.color_name:
                return c
        return None

    def setUp(self):
        self.color_list = get_color_instance_list('esteelauder_doublewear')
        self._0n1 = self.get_color_from_list('0N1', self.color_list)
        self._8n1 = self.get_color_from_list('8N1', self.color_list)

    def test_scraped_number(self):
        self.assertEqual(len(self.color_list), 56)

    def test_scraped_colors(self):
        self.assertTrue(self.color_is_in_color_list('0N1',
            '#fbdcbd', self.color_list))
        self.assertTrue(self.color_is_in_color_list('8N1',
            '#5e3617', self.color_list))

    def test_hsl(self):
        self.assertEqual(self._0n1.hsl, 'hsl(30, 89%, 86%)')
        self.assertEqual(self._8n1.hsl, 'hsl(26, 61%, 23%)')

    def test_lightness(self):
        self.assertEqual(self._0n1.lightness, '86%')
        self.assertEqual(self._8n1.lightness, '23%')

    def test_str(self):
        self.assertEqual(str(self._0n1.__str__()), "0N1 is #fbdcbd, is hsl(30, 89%, 86%)")
    
    def test_color_in_2013(self):
        self._2013_list = colors_in_year('2013')
        self.assertEqual(len(self._2013_list), 20)

    def test_color_in_2015(self):
        self._2015_list = colors_in_year('2015')
        self.assertEqual(len(self._2015_list), 30)

    def test_color_in_2016(self):
        self._2016_list = colors_in_year('2016')
        self.assertEqual(len(self._2016_list), 38)

    def test_color_in_2018_3(self):
        self._2018_3_list = colors_in_year('2018.3')
        self.assertEqual(len(self._2018_3_list), 42)


class TestPlot(unittest.TestCase):

    # test the functions don't return an error!
    def test_plot_shades_year(self):
        try:
            # plot_shades_year('esteelauder_doublewear','2013')
            plot_shades_year('esteelauder_doublewear','2018.7')
        except:
            self.fail()

    def test_plot_shades(self):
        try:
            plot_shades('esteelauder_doublewear')
        except:
            self.fail()

if __name__ == '__main__':
    unittest.main()
