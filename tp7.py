"""class Fraction qui gere plusieurs manipulations"""
class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : la valeur de num et den en entiers et den !=0
        POST : affect self._num et self._den
        Raise ZeroDivisionError
        """

        if den == 0:
            raise ZeroDivisionError("Dénominateur ne peut pas etre 0")
        self._num=num
        self._den=den

    @property
    def numerator(self):
        """Obtient le numérateur de la fraction.
        PRE : ""
        POST : Retourne le numérateur de la fraction.
        """
        return self._num
    @property
    def denominator(self):
        """Obtient le dénominateur de la fraction.

        POST : Retourne le dénominateur de la fraction.
        """
        return self._den

    @numerator.setter
    def numerator(self, value):
        """Définit le numérateur de la fraction.

        POST : Définit le numérateur à la valeur spécifiée.
        """
        self._num = value

    @denominator.setter
    def denominator(self, value):
        """Définit le dénominateur de la fraction.

        PRÉ : value != 0
        POST : Définit le dénominateur à la valeur spécifiée.
        """
        if value != 0:
            raise ZeroDivisionError("Dénominateur ne peut pas être zéro")
        self._den = value

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Retourne une représentation textuelle de la forme réduite de la fraction

        PRE : self est un objet Fraction valide
        POST : Retourne une chaîne de caractères au format num/den
        """
        ch = f'{self._num}/{self._den}'
        return ch

    def as_mixed_number(self) :
        """Retourne une représentation textuelle de la forme réduite
        de la fraction sous forme de nombre mixte

        Un nombre mixte est la somme d'un entier et d'une fraction propre

        PRE : self._den != 0
        POST : Retourne le nombre mixte sous forme de chaîne de caractères
        """
        entier = self._num // self._den
        reste = self._num % self._den
        ch = f'Le nombre mixte est {entier} et {reste}/{self._den}'
        return ch

# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Surcharge de l'opérateur + pour les fractions

        PRE : other._den != 0 et self._den != 0
        POST : Retourne un objet de type float, la somme de self et other
        """
        a, b = self._num, self._den
        c, d = other._num, other._den

        num = a * d + c * b
        den = b * d
        return Fraction(num, den)


    def __sub__(self, other):
        """Surcharge de l'opérateur - pour les fractions

        PRE : other._den != 0 et self._den != 0
        POST : Retourne un objet de type float, la différence entre self et other
        """
        a, b = self._num, self._den
        c, d = other._num, other._den

        num = a * d - c * b
        den = b * d
        return Fraction(num, den)

    def __mul__(self, other):
        """Surcharge de l'opérateur * pour les fractions

        PRE : other._den != 0 et self._den != 0
        POST : Retourne un objet de type float représentant le produit de self et other
        """
        a, b = self._num, self._den
        c, d = other._num, other._den

        num = a * c
        den = b * d
        return Fraction(num, den)

    def __truediv__(self, other):
        """Surcharge de l'opérateur / pour les fractions

        PRE : other._num != 0 et other._den != 0 et self._num != 0 et self._den != 0
        POST : Retourne un objet de type float 
        représentant le résultat de la division de self par other
        """
        a, b = self._num, self._den
        c, d = other._num, other._den
        if c == 0:
            raise ZeroDivisionError("c ne peut pas etre 0")
        num = a * d
        den = b * c
        return Fraction(num, den)



    def __pow__(self, other):
        """Surcharge de l'opérateur ** pour les fractions

        PRE : other._num et other._den sont des entiers
            other._den != 0
        POST : Retourne un objet de type float 
               représentant le résultat de l'exponentiation de self par other
        """
        a, b = self._num, self._den


        # Calculer la puissance sous forme de fraction
        n = other._num / other._den
        num = int(a ** n)
        den = int(b ** n)

        return Fraction(num, den)

    def __eq__(self, other):
        """Surcharge de l'opérateur == pour les fractions
        
        PRE : other._num et other._den sont des entiers
            other._den != 0
        POST : Retourne True si les fractions sont égales, False sinon
        """
        a, b = self._num, self._den
        c, d = other._num, other._den

        value1 = a / b
        value2 = c / d
        return value1 == value2

    def __float__(self):
        """Retourne la valeur décimale de la fraction

        PRE : self._den != 0
        POST : Renvoie le résultat de la fraction en tant que nombre à virgule flottante (float)
        """
        a, b = self._num, self._den

        result = a / b
        return result


# ------------------ Properties checking  ------------------

    def is_zero(self):
        """Vérifie si la valeur de la fraction est 0

        PRE : Le numérateur et le dénominateur sont des entiers, self._den != 0
        POST : Retourne True si la valeur de la fraction est 0
        """
        return self._num == 0

    def is_integer(self):
        """Vérifie si la fraction représente un entier (ex : 8/4, 3, 2/2, ...)

        PRE : Le numérateur et le dénominateur sont des entiers, self._den != 0
        POST : Retourne True si la fraction représente un entier
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Vérifie si la valeur absolue de la fraction est < 1

        PRE : Le numérateur et le dénominateur sont des entiers, self._den != 0
        POST : Retourne True si la valeur absolue de la fraction est inférieure à 1
        """
        return abs(float(self)) < 1

    def is_unit(self):
        """Vérifie si le numérateur de la fraction, après réduction, est égal à 1

        PRE : Le numérateur et le dénominateur sont des entiers, self._den != 0
        POST : Retourne True si le numérateur, après réduction, est égal à 1
        """
        num = self._num
        return abs(num)==1


    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent d'une fraction unitaire

        Deux fractions sont adjacentes si 
        la valeur absolue de leur différence est une fraction unitaire

        PRE : self._den et other._den != 0
        POST : Retourne True si la valeur absolue 
        de la soustraction de self par other est une fraction unitaire
        """
        a, b = self._num, self._den
        c, d = other.numerator, other.denominator

        return abs(a * d - c * b) == 1
        #return  abs(self.__sub__(other)).is_unit()
    # la valeur absolue de la soustraction de self
    #par other si la valeur est une fraction unitaire alors elle renvoie true
    # si non False

fraction1=Fraction(8,3)
fraction2=Fraction(1,9)
fraction3=Fraction(7,4)
fraction4=Fraction(6,4)
print (fraction1,fraction2,fraction3)
print (fraction1+fraction2)
print(fraction1.as_mixed_number())   # renvoie la partie entiere + le reste de la div
print(fraction1-fraction2)
print(fraction1*fraction4)
print(fraction1/fraction2)
print (fraction2**fraction3)
print( fraction1 == fraction2)
print ('float',float(fraction4))
print ('zero', fraction1.is_zero())
print ('integer', fraction1.is_integer())
print ('proper', fraction1.is_proper()) # si la valeur de la fraction <1.
print ('unit', fraction1.is_unit())
print ('adjacent', fraction1.is_adjacent_to(fraction3))
#si la soustraction entre fraction1 et fraction3 a un numerateur qui est egale a 1.
