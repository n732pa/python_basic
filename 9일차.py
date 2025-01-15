import polyArea

print('사각형의 넓이 게산')
width=float(input('사각형의 가로 입력>> '))
height=float(input('사각형의 세로 입력>> '))
print(f'사각형의 넓이: {polyArea.rectArea(width,height)}')

print('삼각형의 넓이 게산')
width=float(input('삼각형의 밑변 입력>> '))
height=float(input('사각형의 높이 입력>> '))
print(f'삼각형의 넓이: {polyArea.triArea(width,height)}')50
