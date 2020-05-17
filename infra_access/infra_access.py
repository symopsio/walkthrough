from sym.annotations import hook, action, reducer
from sym import slack


@reducer
def get_approver(event):
    raise NotImplementedError


@hook
def on_prompt(event):
    """
    Executed before the requesting user is prompted for details about their request.
    """

    pass


@action
def after_prompt(event):
    """
    Executed after the requesting user is prompted for details about their request.
    """

    pass


@hook
def on_request(event):
    """
    Executed before the user's request is sent for approval.
    """

    pass


@action
def after_request(event):
    """
    Executed after the user's request is sent for approval.
    """

    pass


@hook
def on_approval(event):
    """
    Executed before the request is approved.
    """

    pass


@action
def after_approval(event):
    """
    Executed after the request is approved.
    """

    pass


@hook
def on_escalate(event):
    """
    Executed before the user with an approved request is escalated.
    """

    pass


@action
def after_escalate(event):
    """
    Executed after the user with an approved request is escalated.
    """

    pass


@hook
def on_denial(event):
    """
    Executed before the request is denied.
    """

    pass


@action
def after_denial(event):
    """
    Executed after the request is denied.
    """

    pass
