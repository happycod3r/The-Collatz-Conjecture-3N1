import matplotlib.pyplot as mpl
import random
import sys 

#
# The Collatz Conjecture or (3N + 1)
# 
# - Pick a random number, x.
# - If positive do 3x + 1
# - If negative x / 2

def collatz_conjecture(
    seed: int, 
    max_calculations: int=100,
    even_divisor: int=2,
    odd_multiplier: int=3,
    odd_increment: int=1,
    print_output: bool=False,
    graph_line_color: str='black',
    graph_line_width: int=1,
    graph_point_marker: str='o',
    graph_point_color: str='yellow',
    graph_point_size: int=4,
    graph_line_style=None) -> None:

    def _3np1():
        
        def is_even(number: int) -> bool:
            if number % 2 == 0: return True
            else: return False
            
        def _process_even(num: int) -> int:
            return int(num / even_divisor)
        
        def _process_odd(num: int) -> int:
            return int(num * odd_multiplier + odd_increment)
        
        try:    
            _seed = seed
            _cap = max_calculations
            index = 0
            while index != _cap:
                if is_even(_seed):
                    _seed = _process_even(_seed)
                    yield _seed
                else:
                    _seed = _process_odd(_seed)
                    yield _seed
                if index == _cap: 
                    break
                index = index + 1
            
        except ValueError as e:
            print("Number is larger than the max of (4300 digits)")
        except OverflowError as e:
            print("Number is too large to convert from int to str.")
        except RecursionError as e:
            print("You broke reality.")

    def plot_graph(x: list, y: list) -> None:
        
        mpl.plot(x, y, 
                 color=graph_line_color, 
                 linewidth=graph_line_width, 
                 marker=graph_point_marker, 
                 markerfacecolor=graph_point_color, 
                 markersize=graph_point_size,
                 linestyle=graph_line_style)
        mpl.autoscale(True, 'both', True)
        mpl.xlabel('Calculations')
        mpl.ylabel('HS Nums')
        mpl.title('The Collatz Conjecture | 3N + 1')
        mpl.grid(True, which='both', axis='both')
        mpl.show()        

    def calculation_loop():  
        x_calcs = []      
        y_hailstones = []
        index = 0
        try:
            for num in _3np1():
                y_hailstones.append(num)
                x_calcs.append(index)
                index = index + 1
            if print_output:
                for i in range(len(y_hailstones)):
                    print(y_hailstones[i])
            else:
                plot_graph(x_calcs, y_hailstones)
        except ValueError as e:
            print("Number is larger than the max of (4300 digits)")
        except OverflowError as e:
            print("Number is too large to convert from int to str.")
        except RecursionError as e:
            print("You broke reality.")
    
    calculation_loop()

collatz_conjecture(
    
    ######## EQUATION VARIABLES ###########################################################
    #######################################################################################
    seed=1119,                  # The number to start with. The 'N' in 3N + 1
    max_calculations=100,       # Lengthen or shorten to control the length of the trailing loop. 
    even_divisor=2,             # The number to divide an even number by.
    odd_multiplier=3,           # The number to multiply an odd number by.
    odd_increment=1,            # The number to increment the multiplied odd number by.
    #######################################################################################
    #######################################################################################
    
    ######### OUTPUT STYLE ################################################################
    ####################################################################################### 
    print_output=False,         # Whether to print the results to output or to plot the results.
    graph_line_color='black',   # The color of the plot line.
    graph_line_width=1,         # The width of the plot line
    graph_point_marker="o",     # The marker style of the plot points in the plot line.
    graph_point_color="yellow", # The color of the plot points
    graph_point_size="4",       # The size of the plot points.
    graph_line_style=None       # dashed | dotted | dashdot
    #######################################################################################
    #######################################################################################
)
