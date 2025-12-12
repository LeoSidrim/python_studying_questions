name = ' Débora  ' # Remove apenas os espaços em branco fora ao lado da String
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

name = 'Débora ---'  # Não retira o espaço, pois considera que ele faz parte da String
print(name.strip())