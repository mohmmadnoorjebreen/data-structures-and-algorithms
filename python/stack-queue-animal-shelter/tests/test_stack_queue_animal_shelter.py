from stack_queue_animal_shelter import __version__

from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter ,Dogs ,Cats ,Bird
def test_version():
    assert __version__ == '0.1.0'



def test_enqueue():
    animal = AnimalShelter()
    cat = Cats('minmin')
    animal.enqueue(cat)
    excepted = 'minmin'
    actual = animal.s_cat1.top.data
    assert excepted == actual


def test_enqueue_not_cat_or_dog():
    animal = AnimalShelter()
    bird = Bird('sosa')
    excepted = 'null'
    actual = animal.dequeue(bird)
    assert excepted == actual


def test_dequeue():
    animal = AnimalShelter()
    cat = Cats('minmin')
    animal.enqueue(cat)
    excepted = 'minmin'
    actual = animal.dequeue('cat')
    assert excepted == actual

def test_dequeue_not_cat_or_dog():
    animal = AnimalShelter()
    excepted = 'null'
    actual = animal.dequeue('bird')
    assert excepted == actual
