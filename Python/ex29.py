def verifica_polindrom(sir):
    pol=sir[::-1]
    if sir==pol:
        print(True)
    else:
        print(False)
    return(sir)
print(verifica_polindrom("radar"))