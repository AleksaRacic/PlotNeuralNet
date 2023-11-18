import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
factor = 6
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('nesto.jpg', name='slika', width = 80//factor, height=80//factor),
    to_Conv("conv1", 79, 16, offset="(2,0,0)", height=79//factor, depth=79//factor, width=16 , caption="Conv (3x3; stride: 2) BatchNorm2d ReLu"),
    to_BatchNorm2d("norm1", to="(conv1-east)", height=79//factor, depth=79//factor, width=3, caption=""),
    to_ReLu("relu1", 79, 16, offset="(0,0,0)", to="(norm1-east)", height=79//factor, depth=79//factor, width=3 , caption=""),
    from_input_to( "(-2, 0, 0)", "conv1"), 

    to_Conv("conv2", 38, 16, to="(relu1-east)", offset="(2,0,0)", height=40//factor, depth=40//factor, width=16 , caption="Conv (3x3; stride: 2) BatchNorm2d ReLu"),
    to_BatchNorm2d("norm2", to="(conv2-east)", height=40//factor, depth=40//factor, width=3, caption=""),
    to_ReLu("relu2", 80, 16, offset="(0,0,0)", to="(norm2-east)", height=40//factor, depth=40//factor, width=3 , caption=""),
    to_connection( "conv1", "conv2"), 

    to_Conv("conv3", 18, 16, to="(relu2-east)", offset="(2,0,0)", height=20//factor, depth=20//factor, width=16 , caption="Conv (3x3; stride: 2) BatchNorm2d ReLu"),
    to_BatchNorm2d("norm3", to="(conv3-east)", height=20//factor, depth=20//factor, width=3, caption=""),
    to_ReLu("relu3", 80, 16, offset="(0,0,0)", to="(norm3-east)", height=20//factor, depth=20//factor, width=3 , caption=""),
    to_connection( "conv2", "conv3"), 

    to_Conv("conv4", 9, 16, to="(relu3-east)", offset="(2,0,0)", height=10//factor, depth=10//factor, width=16 , caption="Conv (3x3; stride: 2) BatchNorm2d ReLu"),
    to_BatchNorm2d("norm4", to="(conv4-east)", height=10//factor, depth=10//factor, width=3, caption=""),
    to_ReLu("relu4", 9, 16, offset="(0,0,0)", to="(norm4-east)", height=10//factor, depth=10//factor, width=3 , caption=""),
    to_connection( "conv3", "conv4"), 
    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()