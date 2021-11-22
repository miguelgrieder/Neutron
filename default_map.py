#def show_default_map(generator), layer1(generator) -- layer4(generator), before_extras(generator), after_extras(generator)

def show_default_map(generator):
    before_extras(generator)
    layer1(generator)
    layer2(generator)
    layer3(generator)
    layer4(generator)
    after_extras(generator)


def layer1(generator):

    generator.reset()

    generator.fill_empty(1)
    generator.fill_piece(12)
    generator.next_line()

    generator.fill_empty(3)
    generator.fill_piece(8)
    generator.fill_empty(2)
    generator.next_line()

    generator.fill_empty(2)
    generator.fill_piece(10)
    generator.fill_empty(1)
    generator.next_line()

    generator.fill_empty(1)
    generator.fill_piece(12)
    generator.next_line()

    generator.fill_empty(1)
    generator.fill_piece(12)
    generator.next_line()

    generator.fill_empty(2)
    generator.fill_piece(10)
    generator.fill_empty(1)
    generator.next_line()
    
    generator.fill_empty(3)
    generator.fill_piece(8)
    generator.fill_empty(2)
    generator.next_line()

    generator.fill_empty(1)
    generator.fill_piece(12)
    generator.next_line()

def layer2(generator):
    generator.next_floor()

    for i in range(6):
        generator.next_line()
        generator.fill_empty(4)
        generator.fill_piece(6)

def layer3(generator):
    generator.next_floor()
    generator.next_line()

    for i in range(4):
        generator.next_line()
        generator.fill_empty(5)
        generator.fill_piece(4)
        
def layer4(generator):
    generator.next_floor()
    generator.next_line()
    generator.next_line()

    for i in range(2):
        generator.next_line()
        generator.fill_empty(6)
        generator.fill_piece(2)

def before_extras(generator):
    generator.reset()

    for i in range(3):
        generator.next_line()

    generator.fill_empty(13)


    generator.fill_piece(2, 0, 0.5)
    pass


def after_extras(generator):
    generator.reset()

    for i in range(3):
        generator.next_line()

    generator.fill_piece(1, 0, 0.5)

    for i in range(4):
        generator.next_floor()

    for i in range(3):
        generator.next_line()

    generator.fill_empty(6)
    generator.fill_piece(1, 0.5, 0.5)