init python:
    class StateMachine:
        def __init__(self, state):
            self.karma = 50
            self.currentState = state
            self.syringe = False
            self.drink = True
            self.branch = 1

        def Start(self):
            stateData = StateData(self.karma, self.syringe, self.drink, self.branch)
            while self.currentState is not None:
                nextState = self.currentState.Invoke(stateData)
                self.currentState = nextState