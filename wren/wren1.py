import sys
sys.path.append('../')
from pycore.tikzeng import *

def create_lstm_module(input, factor, vertical_offset, name_prefix, color):

    lstm_module = [
    to_input(input,to='(-3,'+str(vertical_offset)+',0)' , name= name_prefix+'slika14', width = 20//factor, height=20//factor, caption = ""),
    to_Conv(name_prefix+"conv1", 79, 32, offset="(2,"+str(vertical_offset)+",0)", height=79//factor, depth=79//factor, width=32//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm1", to="("+name_prefix+"conv1-east)", height=79//factor, depth=79//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu1", 79, 32, offset="(0,0,0)", to="("+name_prefix+"norm1-east)", height=79//factor, depth=79//factor, width=3 , caption=""),
    from_input_to( "(-2, "+str(vertical_offset)+", 0)", name_prefix+"conv1"), 

    to_Conv(name_prefix+"conv2", 38, 32, to="("+name_prefix+"relu1-east)", offset="(2,0,0)", height=40//factor, depth=40//factor, width=32//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm2", to="("+name_prefix+"conv2-east)", height=40//factor, depth=40//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu2", 41, 32, offset="(0,0,0)", to="("+name_prefix+"norm2-east)", height=40//factor, depth=40//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu1", name_prefix+"conv2"), 

    to_Conv(name_prefix+"conv3", 18, 32, to="("+name_prefix+"relu2-east)", offset="(2,0,0)", height=20//factor, depth=20//factor, width=32//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm3", to="("+name_prefix+"conv3-east)", height=20//factor, depth=20//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu3", 41, 32, offset="(0,0,0)", to="("+name_prefix+"norm3-east)", height=20//factor, depth=20//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu2", name_prefix+"conv3"), 

    to_Conv(name_prefix+"conv4", 9, 32, to="("+name_prefix+"relu3-east)", offset="(2,0,0)", height=10//factor, depth=10//factor, width=32//factor , caption=""),
    to_BatchNorm2d(name_prefix+"norm4", to="("+name_prefix+"conv4-east)", height=10//factor, depth=10//factor, width=3, caption=""),
    to_ReLu(name_prefix+"relu4", 9, 32, offset="(0,0,0)", to="("+name_prefix+"norm4-east)", height=10//factor, depth=10//factor, width=3 , caption=""),
    to_connection( name_prefix+"relu3", name_prefix+"conv4"), 

    to_colored_box(name_prefix+"cnn", 1, offset="(2,0,0)", to="("+name_prefix+"relu4-east)", height=40//factor, depth=10//factor, width=10//factor , caption="Proces tagovanja"),
    to_colored_box(name_prefix+"tag", 1, offset="(0,1.2,0)", to="("+name_prefix+"cnn-west)", height=10//factor, depth=10//factor, width=10//factor , caption="", color="{rgb:red,1;green,2;blue,3}"),
    to_connection( name_prefix+"relu4", name_prefix+"cnn"),
    to_Linear(name_prefix+"linear1", 256, offset="(2,0,0)", to="("+name_prefix+"cnn-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( name_prefix+"cnn", name_prefix+"linear1"),
    to_colored_box(name_prefix+"embedded", 1, offset="(2,0,0)", to="("+name_prefix+"linear1-east)", height=10//factor, depth=40//factor, width=10//factor , caption="Embeded ", color=color),
    to_connection( name_prefix+"linear1", name_prefix+"embedded"),
    ]
    return lstm_module

# defined your arch
factor = 4
color1 = "{rgb:red,0;green,10;blue,0}"
color2 = "{rgb:red,10;green,0;blue,0}"
color3 = "{rgb:red,0;green,0;blue,10}"
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    *create_lstm_module("../images/slika_1.png", factor, 0,"jedan", color1),
    to_text("0,6", "Context panels"),
    to_line("(-3,5)", "(30,5)"),
    to_text("0,4", "Answer Candidate"),
    *create_lstm_module("../images/slika_2.png", factor, 10,"dva", color2),
    to_vertical_dots("(3,14)"),
    to_vertical_dots("(27,14)"),
    *create_lstm_module("../images/slika_3.png", factor, 20,"tri", color3),
    to_add_legend(30, 27),
    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()