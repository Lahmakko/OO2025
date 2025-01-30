def kertomat(n: int):
    kertomat_dict = {}
    kertoma = 1
    for i in range(1, n + 1):
        kertoma *= i
        kertomat_dict[i] = kertoma
    return kertomat_dict

# esimerkki
k = kertomat(5)
print(k[1])  # Tuloste: 1
print(k[3])  # Tuloste: 6
print(k[5])  # Tuloste: 120