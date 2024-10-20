## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys

def main(n):
    d = 0
    i = 1
    while i <= n:
        if n % i == 0:
            d += 1
        i += 1
    return d

def ap(n):
    num_divisores = main(n)
    i = 1
    while i < n:
        if main(i) >= num_divisores:
            return "Not anti-prime"  # Retornamos "not anti-prime" si encontramos un número menor con igual o más divisores
        i += 1
    return "Anti-prime"  

numero = int(sys.argv[1])

resultado = ap(numero)
print(resultado)


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())
