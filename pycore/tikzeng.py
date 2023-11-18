
import os

def to_head( projectpath ):
    pathlayers = os.path.join( projectpath, 'layers/' ).replace('\\', '/')
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{import}
\subimport{"""+ pathlayers + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image 
"""

def to_cor():
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,4;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
\def\SumColor{rgb:blue,5;green,15}
\def\Relu{rgb:cyan,5;green,15}
\def\Picture{rgb:blue,5;green,15}
\def\BatchNorm{rgb:pink,5;green,15}
\def\DropoutColor{rgb:magenta,5;black,7}  
\def\LSTMColor{rgb:red,5;black,3}  
"""

def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""

# layers definition

def to_input( pathfile, to='(-3,0,0)', width=8, height=8, name="temp", caption = "" ):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """+ to +""" {\includegraphics[width="""+ str(width)+"cm"+""",height="""+ str(height)+"cm"+"""]{"""+ pathfile +"""}};
\\""" + r"""node[below, font=\Large] at (""" + name +""".south) {"""+ caption +"""};
"""

# Conv
def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Conv
def to_Lstm( name, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str("") +""", }},
        zlabel="""+ str("") +""",
        fill=\LSTMColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_vertical_dots(offset="(0,0)"):
    return r"""\filldraw[fill=black] (0,0) ++"""+offset+""" circle (0.1);
            """ \
            + r"""\filldraw[fill=black] (0,1) ++"""+offset+""" circle (0.1);
            """\
            + r"""\filldraw[fill=black] (0,2) ++"""+offset+""" circle (0.1);
            """

def to_picture( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=3, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        zlabel="""+ str(s_filer) +""",
        fill=\Picture,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_Linear( name, s_filer=256, offset="(0,0,0)", to="(0,0,0)", height=40, depth_width=3, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        zlabel="""+ str(s_filer) +""",
        fill=\FcColor,
        height="""+ str(height) +""",
        width="""+ str(depth_width) +""",
        depth="""+ str(depth_width) +"""
        }
    };
"""

def to_colored_box( name, s_filer=256, offset="(0,0,0)", to="(0,0,0)", height=3, width=3, depth=40, caption=" ", color=r"{rgb: red, 5}" ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        zlabel="""+ str(s_filer) +""",
        fill="""+ color +""",
        height="""+ str(height) +""",
        width="""+ str(depth) +""",
        depth="""+ str(width) +"""
        }
    };
"""

def to_ReLu( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=3, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        fill=\Relu,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""
def to_BatchNorm2d( name, offset="(0,0,0)", to="(0,0,0)", width=3, height=40, depth=40, caption="BatchNorm2d" ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +r""",
        caption=\\""" + caption +r""",
        fill=\BatchNorm,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_BatchNorm1d( name, offset="(0,0,0)", to="(0,0,0)", height=40, depth_width=3, caption="BatchNorm1d" ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +r""",
        caption=\\""" + caption +r""",
        fill=\BatchNorm,
        height="""+ str(height) +""",
        width="""+ str(depth_width) +""",
        depth="""+ str(depth_width) +"""
        }
    };
"""

def to_Dropout( name, offset="(0,0,0)", to="(0,0,0)", height=40, depth_width=3, caption="Dropout" ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +r""",
        caption=\\""" + caption +r""",
        fill=\DropoutColor,
        height="""+ str(height) +""",
        width="""+ str(depth_width) +""",
        depth="""+ str(depth_width) +"""
        }
    };
"""

def to_BatchNorm2d( name, offset="(0,0,0)", to="(0,0,0)", width=3, height=40, depth=40, caption="BatchNorm2d" ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        fill=\BatchNorm,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# Conv,Conv,relu
# Bottleneck
def to_ConvConvRelu( name, s_filer=256, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""" }},
        zlabel="""+ str(s_filer) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(width[0]) +""" , """+ str(width[1]) +""" },
        depth="""+ str(depth) +"""
        }
    };
"""



# Pool
def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        fill=\PoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# unpool4, 
def to_UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {Box={
        name="""+ name +r""",
        caption="""+ caption +r""",
        fill=\UnpoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""



def to_ConvRes( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" " ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +""" 
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        xlabel={{ """+ str(n_filer) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


# ConvSoftMax
def to_ConvSoftMax( name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# SoftMax
def to_SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" " ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        xlabel={{" ","dummy"}},
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def to_Sum( name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +""" 
    {Ball={
        name=""" + name +""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo=$+$
        }
    };
"""


def to_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
"""

def to_vertical_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-south)    -- node {\midarrow} ("""+to+"""-north);
"""

def to_sm_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-east);
"""

def to_normal_connection( of, to):
    return r"""
\draw [connection]  ("""+of+"""-south)    |- node {\midarrow} ("""+to+"""-west);
"""

def from_input_to( of, to):
    return r"""
\draw [connection]  """+of+"""    -- node {\midarrow} ("""+to+"""-west);
"""

def to_skip( of, to, pos=1.25):
    return r"""
\path ("""+ of +"""-southeast) -- ("""+ of +"""-northeast) coordinate[pos="""+ str(pos) +"""] ("""+ of +"""-top) ;
\path ("""+ to +"""-south)  -- ("""+ to +"""-north)  coordinate[pos="""+ str(pos) +"""] ("""+ to +"""-top) ;
\draw [copyconnection]  ("""+of+"""-northeast)  
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""

def to_add_legend(w,h):
    return r"""
\fill[white] ("""+str(w)+r""","""+str(h)+r""") rectangle ++(-12,-4);
\draw ("""+str(w)+r""","""+str(h)+r""") rectangle ++(-12,-4);

\filldraw[fill=\ConvColor] ("""+str(w-11)+r""","""+str(h-1)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-1)+r""") {\textcolor{black}{Konvolucija (3x3)}};

\filldraw[fill=\BatchNorm] ("""+str(w-11)+r""","""+str(h-2)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-2)+r""") {\textcolor{black}{Normalizacija Grupe}};

\filldraw[fill=\Relu] ("""+str(w-11)+r""","""+str(h-3)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-3)+r""") {\textcolor{black}{ReLu funkcja}};

\filldraw[fill=\FcColor] ("""+str(w-5)+r""","""+str(h-1)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-5)+r""","""+str(h-1)+r""") {\textcolor{black}{Linearni sloj}};

\filldraw[fill=\DropoutColor] ("""+str(w-5)+r""","""+str(h-2)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-5)+r""","""+str(h-2)+r""") {\textcolor{black}{Izostavljanje(0.5)}};
    """

def to_add_legend1(w, h):
    return r"""
\fill[white] ("""+str(w)+r""","""+str(h)+r""") rectangle ++(-12,-4);
\draw ("""+str(w)+r""","""+str(h)+r""") rectangle ++(-12,-4);

\filldraw[fill=\ConvColor] ("""+str(w-11)+r""","""+str(h-1)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-1)+r""") {\textcolor{black}{Konvolucija (3x3)}};

\filldraw[fill=\BatchNorm] ("""+str(w-11)+r""","""+str(h-2)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-2)+r""") {\textcolor{black}{Normalizacija Grupe}};

\filldraw[fill=\Relu] ("""+str(w-11)+r""","""+str(h-3)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-11)+r""","""+str(h-3)+r""") {\textcolor{black}{ReLu funkcja}};

\filldraw[fill=\FcColor] ("""+str(w-5)+r""","""+str(h-1)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-5)+r""","""+str(h-1)+r""") {\textcolor{black}{Linearni sloj}};

\filldraw[fill=\DropoutColor] ("""+str(w-5)+r""","""+str(h-2)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-5)+r""","""+str(h-2)+r""") {\textcolor{black}{Izostavljanje(0.5)}};

\filldraw[fill=\LSTMColor] ("""+str(w-5)+r""","""+str(h-3)+r""") ++(-0.5,0) circle (0.2);
\node[font=\Large, anchor=west] at ("""+str(w-5)+r""","""+str(h-3)+r""") {\textcolor{black}{LSTM blok}};
    """

#function to draw line from one point to other point
def to_line( of, to):
    return r"""\draw [dashed]  """+of+"""    --   """+to+""";"""

def to_text(pos, text):
    return r"""\node[font=\Large, anchor=west] at ("""+pos+r""") {\textcolor{black}{"""+text+"""}};
    """

def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate( arch, pathname="file.tex" ):
    with open(pathname, "w") as f: 
        for c in arch:
            print(c)
            f.write( c )
     


