# import examCalculator as exC
# import examCalculator
from examCalculator import *

x=int(input('과목1 점수 입력>> '))
y=int(input('과목2 점수 입력>> '))
z=int(input('과목3 점수 입력>> '))
print(totalScore(x,y,z))
print(averageScore(x,y,z))
print(passfail(x,y,z))
