from discrete_distribution import DiscreteDistribution 

states = ['sun', 'rain', 'clouds', 'snow']

distribution = DiscreteDistribution.random_initialize(states)

for s, f in zip(distribution.states, distribution.probabilities):
    print(s, f)

print(distribution.df)

print(distribution['sun'])
print(distribution['rain'])
print(distribution.argmax())
