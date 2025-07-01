from cat import Cat
from dog import Dog
from panda import Panda
from farm import Farm

if __name__=="__main__":
    dog = Dog('Buddy')
    cat = Cat('Kitty')
    panda = Panda('Fubao')

    dog.speak()
    cat.speak()
    panda.speak()

    dog.move()
    cat.move()
    panda.move()

    # 반복문으로 10번 움직임
    for _ in range(10): # i가 쓰이지 않으므로 _로 대체해도 됨. Pythonic
        dog.move()
        cat.move()

    farm = Farm('a')
    print(farm._farm_name)

    farm.add_animal(cat)
    farm.add_animal(dog)
    farm.add_animal(panda)

    cat2 = Cat('Momo')
    dog2 = Dog('Among')

    farm.add_animal(cat2)
    farm.add_animal(dog2)

    farm.feed_all()

    farm.play_all()

    farm.show_all()



