import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
factor = 4
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('slika_0.png', name='slika0', to="(-3,0,0)",width = 41//factor, height=41//factor),
    to_input('slika_1.png', name='slika1', to="(-3,0,1)", width = 41//factor, height=41//factor),
    to_input('slika_2.png', name='slika2', to="(-3,0,2)", width = 41//factor, height=41//factor),
    to_input('slika_3.png', name='slika3', to="(-3,0,3)", width = 41//factor, height=41//factor),
    to_input('slika_5.png', name='slika5', width = 41//factor, height=41//factor),
    to_input('slika_6.png', name='slika6', width = 41//factor, height=41//factor),
    to_input('slika_7.png', name='slika7', width = 41//factor, height=41//factor),
    to_input('slika_8.png', name='slika8', width = 41//factor, height=41//factor),
    to_input('slika_9.png', name='slika9', width = 41//factor, height=41//factor),
    to_input('slika_10.png', name='slika10', width = 41//factor, height=41//factor),
    to_input('slika_11.png', name='slika11', width = 41//factor, height=41//factor),
    to_input('slika_12.png', name='slika12', width = 41//factor, height=41//factor),
    to_input('slika_13.png', name='slika13', width = 41//factor, height=41//factor),
    to_input('slika_14.png', name='slika14', width = 41//factor, height=41//factor, caption = "16 naslaganih panela"),
    to_Conv("conv1", 79, 16, offset="(2,0,0)", height=79//factor, depth=79//factor, width=16//factor , caption=""),
    to_BatchNorm2d("norm1", to="(conv1-east)", height=79//factor, depth=79//factor, width=3, caption=""),
    to_ReLu("relu1", 79, 16, offset="(0,0,0)", to="(norm1-east)", height=79//factor, depth=79//factor, width=3 , caption=""),
    from_input_to( "(-2, 0, 0)", "conv1"), 

    to_Conv("conv2", 38, 16, to="(relu1-east)", offset="(2,0,0)", height=40//factor, depth=40//factor, width=16//factor , caption=""),
    to_BatchNorm2d("norm2", to="(conv2-east)", height=40//factor, depth=40//factor, width=3, caption=""),
    to_ReLu("relu2", 41, 16, offset="(0,0,0)", to="(norm2-east)", height=40//factor, depth=40//factor, width=3 , caption=""),
    to_connection( "relu1", "conv2"), 

    to_Conv("conv3", 18, 16, to="(relu2-east)", offset="(2,0,0)", height=20//factor, depth=20//factor, width=16//factor , caption=""),
    to_BatchNorm2d("norm3", to="(conv3-east)", height=20//factor, depth=20//factor, width=3, caption=""),
    to_ReLu("relu3", 41, 16, offset="(0,0,0)", to="(norm3-east)", height=20//factor, depth=20//factor, width=3 , caption=""),
    to_connection( "relu2", "conv3"), 

    to_Conv("conv4", 9, 16, to="(relu3-east)", offset="(2,0,0)", height=10//factor, depth=10//factor, width=16//factor , caption=""),
    to_BatchNorm2d("norm4", to="(conv4-east)", height=10//factor, depth=10//factor, width=3, caption=""),
    to_ReLu("relu4", 9, 16, offset="(0,0,0)", to="(norm4-east)", height=10//factor, depth=10//factor, width=3 , caption=""),
    to_connection( "relu3", "conv4"), 

    to_Linear("linear1", 512, offset="(2,0,0)", to="(relu4-east)", height=100//factor, depth_width=3 , caption=""),
    to_connection( "relu4", "linear1"),
    to_ReLu("linear2", 410, offset="(0,0,0)", to="(linear1-east)", height=100//factor, depth=3, width=3 , caption=""),
    to_Dropout("Dropout", to="(linear2-east)", height=100//factor, caption=""),

    to_Linear("linear3", 8, offset="(2,0,0)", to="(Dropout-east)", height=20//factor, depth_width=3 , caption=""),
    to_connection( "Dropout", "linear3"),

    to_add_legend(23,8),
    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()