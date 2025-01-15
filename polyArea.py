def rectArea(width,height):
    # a=width*height
    return width*height

def triArea(base,height):
    return base*height/2


if __name__ =='__main__':
    print(f'사각형의 넓이: {rectArea(5,10)}')
    print(f'삼각형의 넓이: {triArea(5,10)}')
