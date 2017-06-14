from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_see_a_list_of_bags(self):
        # Edith has heard about a cool new crochet bags store online. She goes
        # to check out its homepage
        self.browser.get('http://localhost')

        # She notices the page title and header mention dreamy crochet
        self.assertIn('Dreamy Crochet', self.browser.title)

        # She is invited to enter a to-do item straight away
        # header = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute('placeholder'),
        #     'Enter a to-do item'
        # )

        # She then notices the list of categories that she can click on
        # The categories have a name and a thumbnail of a product that comes
        # under it.

        self.fail('Finish the test!')
