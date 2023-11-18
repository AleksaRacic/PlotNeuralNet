import sys
sys.path.append('../')
from pycore.tikzeng import *

def create_lstm_module(input, factor, vertical_offset, name_prefix, previus_module):

    lstm_module = [
    to_input(input,to='(-3,'+str(vertical_offset)+',0)' , name= name_prefix+'slika14', width = 20//factor, height=20//factor, caption = ""),
    to_Conv(name_prefix+"conv1", 79, 16, offset="(2,"+str(vertical_offset)+",0)", height=79//factor, depth=79//factor, width=16//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm1", to="("+name_prefix+"conv1-east)", height=79//factor, depth=79//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu1", 79, 16, offset="(0,0,0)", to="("+name_prefix+"norm1-east)", height=79//factor, depth=79//factor, width=3 , caption=""),
    from_input_to( "(-2, "+str(vertical_offset)+", 0)", name_prefix+"conv1"), 

    to_Conv(name_prefix+"conv2", 38, 16, to="("+name_prefix+"relu1-east)", offset="(2,0,0)", height=40//factor, depth=40//factor, width=16//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm2", to="("+name_prefix+"conv2-east)", height=40//factor, depth=40//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu2", 41, 16, offset="(0,0,0)", to="("+name_prefix+"norm2-east)", height=40//factor, depth=40//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu1", name_prefix+"conv2"), 

    to_Conv(name_prefix+"conv3", 18, 16, to="("+name_prefix+"relu2-east)", offset="(2,0,0)", height=20//factor, depth=20//factor, width=16//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm3", to="("+name_prefix+"conv3-east)", height=20//factor, depth=20//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu3", 41, 16, offset="(0,0,0)", to="("+name_prefix+"norm3-east)", height=20//factor, depth=20//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu2", name_prefix+"conv3"), 

    to_Conv(name_prefix+"conv4", 9, 16, to="("+name_prefix+"relu3-east)", offset="(2,0,0)", height=10//factor, depth=10//factor, width=16//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm4", to="("+name_prefix+"conv4-east)", height=10//factor, depth=10//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu4", 9, 16, offset="(0,0,0)", to="("+name_prefix+"norm4-east)", height=10//factor, depth=10//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu3", name_prefix+"conv4"), 

    to_Lstm(name_prefix+"lstm1", to="("+name_prefix+"relu4-east)", offset="(2,0,0)", height=40//factor, depth=40//factor, width=40//factor , caption=""),
    to_connection( name_prefix+"relu4", name_prefix+"lstm1"),
    ]
    if previus_module is not None:
        lstm_module.append(to_sm_connection(name_prefix+"lstm1", previus_module+"lstm1"))
        lstm_module.append(to_vertical_connection(name_prefix+"lstm1", previus_module+"lstm1"))
    return lstm_module

# defined your arch
factor = 4

arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    *create_lstm_module("slika_1.png", factor, 0,"jedan", None),
    *create_lstm_module("slika_2.png", factor, 10,"dva", "jedan"),
    to_vertical_dots("(3,4)"),
    to_vertical_dots("(18,4)"),
    to_Dropout("Dropout", to="(jedanlstm1-south)", offset="(4,-2,0)", height=200//factor, caption=""),
    to_Linear("linear3", 96, offset="(0,0,0)", to="(Dropout-east)", height=200//factor, depth_width=3 , caption=""),
    to_normal_connection("jedanlstm1", "Dropout"),
    to_Linear("linear4", 8, offset="(4,0,0)", to="(linear3-east)", height=100//factor, depth_width=3 , caption=""),
    to_connection("linear3", "linear4"),
    to_add_legend1(33,13),
    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()