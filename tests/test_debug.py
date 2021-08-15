# -*- coding: utf-8 -*-
# @File    : test_debug.py
# @Software: PyCharm
from selene.support.shared import browser

from web_test.pages import pypi
from selene import have, be



def test_pypi():
    """
    LocatorModules/PageObjectLess
    LocatorModules == page locators/selectors are simply vars in python modules
    Might be also called as PageModules
    ===========================================================================

    Here the page model is implemented in the simplest modular way
    with simplification to "just vars, no functions for steps" in python modules.

    GO FOR:
    * a bit higher abstraction (no more technical selectors in tests code)
      * extra readability in test code
    * reusable vars with locators
    * easier refactoring (Refactor>Rename, etc. can be applied)
    * yet KISS modeling (Keep It Simple Stupid)

    TRADEOFFS:
    - common ones for "programming without functions" style ;)
      some code might be too bulky,
      business steps might be hardly visible in a long e2e test
   """
    browser.open(pypi.url)

    pypi.search.type('selene').press_enter()
    pypi.results\
        .should(have.size_greater_than_or_equal(9)) \
        .first.should(have.text('Concise API for selenium in Python'))

    pypi.results.first.click()
    browser.should(have.url(pypi.url + 'project/selene/'))
    browser.should(have.title_containing('selene · PyPI'))
