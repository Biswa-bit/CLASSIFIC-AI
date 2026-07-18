"""
==============================================================
CLASSIFIC-AI

State Manager

Stores pipeline state shared between AI agents.

Author : Biswadip Choudhury
Version : 1.0.0
==============================================================
"""


class StateManager:
    """
    Maintains pipeline state throughout execution.
    """

    def __init__(self):

        self.state = {}

    ###########################################################
    # Store Value
    ###########################################################

    def set(self, key, value):

        self.state[key] = value

    ###########################################################
    # Get Value
    ###########################################################

    def get(self, key, default=None):

        return self.state.get(key, default)

    ###########################################################
    # Check Key
    ###########################################################

    def exists(self, key):

        return key in self.state

    ###########################################################
    # Remove Key
    ###########################################################

    def remove(self, key):

        if key in self.state:

            del self.state[key]

    ###########################################################
    # Clear State
    ###########################################################

    def clear(self):

        self.state.clear()

    ###########################################################
    # Return Entire State
    ###########################################################

    def get_state(self):

        return self.state
    