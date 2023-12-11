from matchers import All, And, Or

class Query():
    def __init__(self, operations=None):
        if None == operations:
            self.operations = []
        else:
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
    _query = None
    _oneOf = None

    def __init__(self, query=Query(), oneOf=None):
        QueryBuilder._query = query
        QueryBuilder._oneOf = oneOf

    def build(self):
        if None == QueryBuilder._oneOf:
            if len(QueryBuilder._query.operations) == 0:
                result = All()
            else:
                result = And(*QueryBuilder._query.operations)
        else:
            result = Or(*QueryBuilder._oneOf)
        self.reset()
        return result
    
    def oneOf(self, *args):
        return QueryBuilder(None, args)

    def reset(self):
        QueryBuilder._query = Query()
        QueryBuilder._oneOf = None

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(QueryBuilder._query, value, attr))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(QueryBuilder._query, value, attr))

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(QueryBuilder._query, team))
