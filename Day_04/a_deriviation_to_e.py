import math

# =============================================================================
# MAIN
# =============================================================================

def main():
    # Initialistion de a à 2, on sait que la valeur recherchée est proche de 2.71 on limite donc le nombre d'itération
    a = 2

    # Temps que le log de a est inférieur à 1 on incrémente de 0.0001
    while math.log(a) <= 1:
        print (math.log(a))
        print(a)
        a += 0.0001
    # Lorsque le log de a est supérieur à 1 on affiche la valeur de a
    print("A = %s" % (a))


# =============================================================================
# SCRIPT INITIATE
# =============================================================================

if __name__ == '__main__':
    main()
