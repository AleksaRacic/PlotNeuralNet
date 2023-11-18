import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
factor = 6
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('nesto.png', to='slika-east', height=224//factor, width=224//factor, name="input"),
    to_picture("slika", 224, 1, offset="(0,0,0)", to="(conv1-east)", height=224//factor, depth=224//factor, width=3 , caption="Slika"),
    to_Conv("conv1", 224, 16, offset="(2,0,0)", to="(slika-east)", height=224//factor, depth=224//factor, width=16 , caption="Conv (5x5)"),
    to_connection( "slika", "conv1"), 
    to_BatchNorm2d("norm1", to="(conv1-east)", height=224//factor, depth=224//factor, width=3),
    to_ReLu("relu1", 224, 16, offset="(0,0,0)", to="(norm1-east)", height=224//factor, depth=224//factor, width=3 , caption="Relu"),
    to_Pool("pool1", offset="(1,0,0)", to="(relu1-east)", height=110//factor, depth=110//factor, caption = "Pool(2x2)"),
    to_connection( "relu1", "pool1"), 

    to_Conv("conv2", 110, 32, offset="(2,0,0)", to="(pool1-east)", height=110//factor, depth=110//factor, width=32 , caption="Conv (5x5)"),
    to_connection( "pool1", "conv2"), 
    to_BatchNorm2d("norm2", to="(conv2-east)", height=110//factor, depth=110//factor, width=3),
    to_ReLu("relu2", 110, 3, offset="(0,0,0)", to="(norm2-east)", height=110//factor, depth=110//factor, width=3 , caption="Relu"),
    to_Pool("pool2", offset="(1,0,0)", to="(relu2-east)", height=53//factor, depth=53//factor, caption = "Pool(2x2)"),
    to_connection( "relu2", "pool2"),

    to_Linear("linear1", 89888, offset="(2,0,0)", to="(pool2-east)", height=224//factor, depth_width=3 , caption="Flatten"),
    to_connection( "pool2", "linear1"),
    to_Linear("linear2", 120, offset="(2,0,0)", to="(linear1-east)", height=60//factor, depth_width=3 , caption="Linear"),
    to_connection( "linear1", "linear2"),
    to_BatchNorm1d("norm3", to="(linear2-east)", height=60//factor),
    to_ReLu("relu4", 120, 3, offset="(0,0,0)", to="(norm3-east)", height=60//factor, depth = 3, width=3 , caption="Relu"),

    to_Linear("linear3", 84, offset="(2,0,0)", to="(relu4-east)", height=50//factor, depth_width=3 , caption="Linear"),
    to_connection( "relu4", "linear3"),
    to_BatchNorm1d("norm4", to="(linear3-east)", height=50//factor),
    to_ReLu("relu5", 84, 3, offset="(0,0,0)", to="(norm4-east)", height=50//factor, depth = 3, width=3 , caption="Relu"),
    to_Linear("linear4", 10, offset="(2,0,0)", to="(relu5-east)", height=30//factor, depth_width=3 , caption="Linear"),
    to_connection( "relu5", "linear4"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()