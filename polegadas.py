def conversor(i):
  arq = open('Polegada', 'a')
  m1 = i * 0.39
  arq.write(f'o valor {i} em centímetros corresponde a {m1} valor em polegadas\n')
  arq.close()
  print(f'o valor {i} em centímetros corresponde a {m1} valor em polegadas')