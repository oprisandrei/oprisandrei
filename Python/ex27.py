def cel_mai_mic_divizor(n):
    for div in range(2,n+1):
        if n%div==0:
            m=div
            break
    return m

print(cel_mai_mic_divizor(15))
