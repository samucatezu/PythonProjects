largura = float(input('largura da parede:  '))
alt = float(input('altura da parede: '))
área = largura * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

