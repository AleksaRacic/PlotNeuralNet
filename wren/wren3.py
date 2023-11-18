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
color4= "{rgb:red,0;green,10;blue,10}"
color5 = "{rgb:red,10;green,0;blue,10}"
color6 = "{rgb:red,10;green,10;blue,0}"
color7 = "{rgb:red,6;green,1;blue,10}"
color8 = "{rgb:red,3;green,0;blue,2}"
color9 = "{rgb:red,7;green,3;blue,0}"

arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_colored_box("score1", 1, offset="(0,0,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color1),
    to_colored_box("score2", 1, offset="(0,2,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color2),
    to_colored_box("score3", 1, offset="(0,4,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color3),
    to_colored_box("score4", 1, offset="(0,6,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color4),
    to_colored_box("score5", 1, offset="(0,8,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color5),
    to_colored_box("score6", 1, offset="(0,10,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color6),
    to_colored_box("score7", 1, offset="(0,12,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color7),
    to_colored_box("score8", 1, offset="(0,14,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="", color=color8),

    to_colored_box("softmax", 1, offset="(30,7,0)", to="(0,0,0)", height=160//factor, depth=20//factor, width=20//factor , caption="Softmax", color=color9),

    to_connection( "score1", "softmax"),
    to_connection( "score2", "softmax"),
    to_connection( "score3", "softmax"),
    to_connection( "score4", "softmax"),
    to_connection( "score5", "softmax"),
    to_connection( "score6", "softmax"),
    to_connection( "score7", "softmax"),
    to_connection( "score8", "softmax"),

    to_colored_box("argmax", 1, offset="(35,7,0)", to="(0,0,0)", height=20//factor, depth=20//factor, width=20//factor , caption="Argmax", color=color2),
    to_connection( "softmax", "argmax"),

    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()