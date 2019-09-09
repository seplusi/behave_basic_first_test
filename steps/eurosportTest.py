from behave import *

use_step_matcher("re")


@then("I just want to print hello world")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then  I just want to print hello world')