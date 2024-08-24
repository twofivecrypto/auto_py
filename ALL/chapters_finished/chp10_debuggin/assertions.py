'''
An assertion is a sanity check to make sure your code isn't doing something obviously wrong.
These sanity checks are performed by assert statements. If the sanity check fails, then an
AssertionError exception is raised. In code, an assert statement consists of the following:
- The assert keyword
- A condition (that is, an expression that evaluates to True or False)
- A comma
- A string to display when the condition is False

Check example below:
'''


podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'