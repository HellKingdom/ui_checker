# !/usr/bin/env python
# -*- coding=utf-8 -*-

from page_obj.customer import IndexPage
from .base_case import BaseCase


class TestCcustomer(BaseCase):
    
    def test_search_exist_customer(self):
        """
        pre-condition: 18010181267 customer exists
        no cleaning need
        """
        phone = '18010181267'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        
        # assert page_obj value and search value
        customer_phone = page.get_value('会员电话：')
        self.assertEqual(customer_phone, phone)

        # compare page_obj values and db values
        where_condition = "phone='%s'" % phone
        self.assertTrue(page.compare_db_all(where_condition))
        page.logout()
        
    def test_search_not_exist_customer(self):
        """
            pre-condition: 18010181261 customer not exists
            no cleaning need
        """
        phone = '18010181261'
        page = IndexPage(self.driver)
        page.load()
        page.search_phone(phone)
        customer_phone = page.get_value('customer_phone')
        self.assertFalse(customer_phone)
        page.logout()
        

        


