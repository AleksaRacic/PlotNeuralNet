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
    to_text("0,6", "Konteksne ploce"),
    to_line("(-3,5)", "(30,5)"),
    to_text("0,4", "Potencijalni odgovori"),
    *create_lstm_module("../images/slika_2.png", factor, 10,"dva", color2),
    to_vertical_dots("(3,14)"),
    to_vertical_dots("(27,14)"),
    *create_lstm_module("../images/slika_3.png", factor, 20,"tri", color3),


    ####Ovde napraviti novi fajl#####

    to_colored_box("embedded1", 1, offset="(32,0,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="Spojeni parovi latentnih vektora", color=color1),
    to_colored_box("embedded2", 1, offset="(0,0,0)", to="(embedded1-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color2),

    to_colored_box("embedded12", 1, offset="(32,3,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color1),
    to_colored_box("embedded22", 1, offset="(0,0,0)", to="(embedded12-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color3),

    to_colored_box("embedded13", 1, offset="(32,6,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color2),
    to_colored_box("embedded23", 1, offset="(0,0,0)", to="(embedded13-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color1),

    to_vertical_dots("(34,9)"),

    to_colored_box("embedded132", 1, offset="(32,14,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color2),
    to_colored_box("embedded222", 1, offset="(0,0,0)", to="(embedded132-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color3),

    to_colored_box("embedded1321", 1, offset="(32,17,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color3),
    to_colored_box("embedded223", 1, offset="(0,0,0)", to="(embedded1321-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color2),

    to_colored_box("embedded1322", 1, offset="(32,20,0)", to="(0,0,0)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color3),
    to_colored_box("embedded224", 1, offset="(0,0,0)", to="(embedded1322-east)", height=10//factor, depth=40//factor, width=10//factor , caption="", color=color1),

    to_Linear("linear12", 256, offset="(2,0,0)", to="(embedded2-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded2", "linear12"),

    to_ReLu("relu12", 256, offset="(0,0,0)", to="(linear12-east)", height=40//factor, width=2, depth=2, caption=""),

    to_Linear("linear13", 256, offset="(2,0,0)", to="(relu12-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu12", "linear13"),

    to_ReLu("relu13", 256, offset="(0,0,0)", to="(linear13-east)", height=40//factor, width=2, depth=2, caption=""),

    to_Linear("linear14", 256, offset="(2,0,0)", to="(relu13-east)", height=40//factor, depth_width=2 , caption=""),

    to_connection( "relu13", "linear14"),

    to_ReLu("relu14", 256, offset="(0,0,0)", to="(linear14-east)", height=40//factor, width=2, depth=2, caption=""),

    to_Dropout("Dropout1", to="(relu14-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu14", "Dropout1"),

    to_ReLu("relu15", 256, offset="(0,0,0)", to="(Dropout1-east)", height=40//factor, width=2, depth=2, caption=""),

    #############################
    to_Linear("linear123", 256, offset="(2,0,0)", to="(embedded22-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded22", "linear123"),

    to_ReLu("relu123", 256, offset="(0,0,0)", to="(linear123-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear124", 256, offset="(2,0,0)", to="(relu123-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu123", "linear124"),
    to_ReLu("relu124", 256, offset="(0,0,0)", to="(linear124-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear125", 256, offset="(2,0,0)", to="(relu124-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu124", "linear125"),
    to_ReLu("relu125", 256, offset="(0,0,0)", to="(linear125-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Dropout("Dropout2", to="(relu125-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu125", "Dropout2"),
    to_ReLu("relu1261211", 256, offset="(0,0,0)", to="(Dropout2-east)", height=40//factor, width=2, depth=2, caption=""),
    
    #############################
    to_Linear("linear124", 256, offset="(2,0,0)", to="(embedded23-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded23", "linear124"),
    to_ReLu("relu124", 256, offset="(0,0,0)", to="(linear124-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear125", 256, offset="(2,0,0)", to="(relu124-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu124", "linear125"),
    to_ReLu("relu125", 256, offset="(0,0,0)", to="(linear125-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear126", 256, offset="(2,0,0)", to="(relu125-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu125", "linear126"),
    to_ReLu("relu126", 256, offset="(0,0,0)", to="(linear126-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Dropout("Dropout3", to="(relu126-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu126", "Dropout3"),
    to_ReLu("relu12700", 256, offset="(0,0,0)", to="(Dropout3-east)", height=40//factor, width=2, depth=2, caption=""),

    #############################
    to_Linear("linear1254", 256, offset="(2,0,0)", to="(embedded222-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded222", "linear1254"),
    to_ReLu("relu1254", 256, offset="(0,0,0)", to="(linear1254-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear1264", 256, offset="(2,0,0)", to="(relu1254-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu1254", "linear1264"),
    to_ReLu("relu1264", 256, offset="(0,0,0)", to="(linear1264-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear1274", 256, offset="(2,0,0)", to="(relu1264-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu1264", "linear1274"),
    to_ReLu("relu1274", 256, offset="(0,0,0)", to="(linear1274-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Dropout("Dropout4", to="(relu1274-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu1274", "Dropout4"),
    to_ReLu("relu1275", 256, offset="(0,0,0)", to="(Dropout4-east)", height=40//factor, width=2, depth=2, caption=""),

    #############################


    to_Linear("linear12612", 256, offset="(2,0,0)", to="(embedded223-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded223", "linear12612"),
    to_ReLu("relu12612", 256, offset="(0,0,0)", to="(linear12612-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear12712", 256, offset="(2,0,0)", to="(relu12612-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu12612", "linear12712"),
    to_ReLu("relu12712", 256, offset="(0,0,0)", to="(linear12712-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear12712", 256, offset="(2,0,0)", to="(relu12712-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu12712", "linear12712"),
    to_ReLu("relu12712", 256, offset="(0,0,0)", to="(linear12712-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Dropout("Dropout5", to="(relu12712-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu12712", "Dropout5"),
    to_ReLu("relu12713", 256, offset="(0,0,0)", to="(Dropout5-east)", height=40//factor, width=2, depth=2, caption=""),

    #############################


    to_Linear("linear12742", 256, offset="(2,0,0)", to="(embedded224-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "embedded224", "linear12742"),
    to_ReLu("relu12742", 256, offset="(0,0,0)", to="(linear12742-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear12742", 256, offset="(2,0,0)", to="(relu12742-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu12742", "linear12742"),
    to_ReLu("relu12742", 256, offset="(0,0,0)", to="(linear12742-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Linear("linear12742", 256, offset="(2,0,0)", to="(relu12742-east)", height=40//factor, depth_width=2 , caption=""),
    to_connection( "relu12742", "linear12742"),
    to_ReLu("relu12742", 256, offset="(0,0,0)", to="(linear12742-east)", height=40//factor, width=2, depth=2, caption=""),
    to_Dropout("Dropout6", to="(relu12742-east)", offset="(2,0,0)", height=40//factor,depth_width=2, caption=""),
    to_connection( "relu12742", "Dropout6"),
    to_ReLu("relu12743", 256, offset="(0,0,0)", to="(Dropout6-east)", height=40//factor, width=2, depth=2, caption=""),

    #############################

    to_Sum("sum1", offset="(55,9,0)", to="(0,0,0)", radius=3.5, opacity=0.6),

    to_connection( "relu15", "sum1"),
    to_connection( "relu1261211", "sum1"),
    to_connection( "relu12700", "sum1"),
    to_connection( "relu1275", "sum1"),
    to_connection( "relu12713", "sum1"),
    to_connection( "relu12743", "sum1"),

    to_colored_box("embedded3233", 256, offset="(2,0,0)", to="(sum1-east)", height=10//factor, depth=40//factor, width=10//factor , caption="Embeded ", color="{rgb:red,7;green,2;blue,3}"),
    to_connection( "sum1", "embedded3233"),

    to_end()
    ]

def main():
    print(sys.argv)
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()