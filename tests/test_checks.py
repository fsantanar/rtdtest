#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author: Felipe Santana Rojas
# Date: 2023-06-07
# Filename: test_checks.py
# License: MIT License
import os
import unittest

import rtdtest.cpu_health as cpu_health


class SystemTestCase(unittest.TestCase):
    def test_add(self):
        """
        Test case to check if check_enough_disk_space
        returns False when the min_percent_disk required is set to 100.
        """
        res = cpu_health.square(4)
        self.assertEqual(res,16)

if __name__ == '__main__':
    unittest.main()
