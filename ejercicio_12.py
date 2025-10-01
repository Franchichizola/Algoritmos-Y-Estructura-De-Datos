def DCM(n1,n2):
    resto = n1 % n2
    if resto == 0:
        return n2
    return DCM(n2,resto)

if __name__ == "__main__":
    print(DCM(270,192))