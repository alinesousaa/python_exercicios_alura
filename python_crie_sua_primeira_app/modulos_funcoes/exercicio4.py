cy = float(input("Digite o valor de coordenada y : "))
cx = float(input("Digite o valor de coordenada x : "))

if cy > 0 and cx > 0:
    print("O ponto está no primeiro quadrante.")
elif cx < 0 and cy > 0:
    print("O ponto está no segundo quadrante.")
elif cy < 0 and cx < 0:
    print("O ponto está no terceiro quadrante.")
else:
    print("O ponto está no eixo")