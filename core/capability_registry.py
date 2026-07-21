"""
==========================================================
CLASSIFIC-AI

Capability Registry

Lists all available agents
and modules.

Initially this is a placeholder.

Later it will automatically
register every agent.

==========================================================
"""


class CapabilityRegistry:

    def __init__(self):

        self.registry = {}

    def register(self, agent_name, modules):

        self.registry[agent_name] = modules

    def get_agents(self):

        return list(self.registry.keys())

    def get_modules(self, agent_name):

        return self.registry.get(agent_name, [])
    