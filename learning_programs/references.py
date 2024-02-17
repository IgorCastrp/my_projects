# Mutable

eggs = ['cat', 'dog',]
print(id(eggs))
eggs.append('mouse')
print(id(eggs))

# Immutable
name = 'Igor'
print(id(name))
name += ' Brambila'
print(id(name))