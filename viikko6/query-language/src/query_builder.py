from matchers import All, And

class Query():
    def __init__(self, operations=[]):
        self.operations = operations

    def add(self, operation):
        self.operations.append(operation)

class HasAtLeast(Query):
    def __init__(self, queryStack, value, attr):
        super().__init__(queryStack.operations)
        queryStack.add(self)
        self._value = value
        self._attr = attr

    def test(self, player):
        playerValue = getattr(player, self._attr)
        
        return playerValue >= self._value

class HasFewerThan(Query):
    def __init__(self, queryStack, value, attr):
        super().__init__(queryStack.operations)
        queryStack.add(self)
        self._value = value
        self._attr = attr

    def test(self, player):
        playerValue = getattr(player, self._attr)
        
        return playerValue < self._value

class PlaysIn(Query):
    def __init__(self, queryStack, team):
        super().__init__(queryStack.operations)
        queryStack.add(self)
        self._team = team

    def test(self, player):
        return player.team == self._team

class QueryBuilder():
    def __init__(self, query=Query()):
        self._query = query

    def build(self):
        if len(self._query.operations) == 0:
            result = All()
        else:
            result = And(*self._query.operations)
        self.reset()
        return result
    
    def reset(self):
        self._query = Query()

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(self._query, value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(self._query, value, attr))

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self._query, team))
