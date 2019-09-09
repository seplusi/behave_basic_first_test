# file:features/steps/step_tutorial03.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave  import given, when, then


@given('I insert number {num1} and number {num2}')
def step_given_put_thing_into_blender(context, num1, num2):
    print(num1 + ' ' + num2)
    context.num1 = int(num1)
    context.num2 = int(num2)


@when("I perform the sum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.sum_total = context.num1 + context.num2


@then("it should print the correct sum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print('Total = %d' % context.sum_total)
