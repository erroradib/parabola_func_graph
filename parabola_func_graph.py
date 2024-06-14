# Adnan Adib
# 14 June, 2024
# 12:34


import os as adib

try:
    import numpy as np
    import matplotlib.pyplot as PLOT

except ImportError:
    adib.system("pip install numpy")
    adib.system("pip install matplotlib")
    import numpy as np
    import matplotlib.pyplot as PLOT

def plot_parabola_1(a, x_value, x_range=10, num_points=400):
    """Plot y^2 = 4ax"""
    x_start = x_value - x_range
    x_end = x_value + x_range
    x_val = np.linspace(x_start, x_end, num_points)
    y_val_positive = np.sqrt(np.maximum(0, 4 * a * x_val))
    y_val_negative = -np.sqrt(np.maximum(0, 4 * a * x_val))
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val, y_val_positive, label=f'y = ±sqrt(4 * {a} * x)', color='green')
    PLOT.plot(x_val, y_val_negative, color='red')
    PLOT.title(f'Plot of y^2 = 4 * {a} * x\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def plot_parabola_2(a, y_value, y_range=10, num_points=400):
    """Plot x^2 = 4ay"""
    y_start = y_value - y_range
    y_end = y_value + y_range
    y_val = np.linspace(y_start, y_end, num_points)
    x_val_positive = np.sqrt(np.maximum(0, 4 * a * y_val))
    x_val_negative = -np.sqrt(np.maximum(0, 4 * a * y_val))
    
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val_positive, y_val, label=f'x = ±sqrt(4 * {a} * y)', color='green')
    PLOT.plot(x_val_negative, y_val, color='red')
    PLOT.title(f'Plot of x^2 = 4 * {a} * y\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def plot_parabola_3(a, b, c, x_range=10, num_points=400):
    """Plot y = ax^2 + bx + c"""
    x_val = np.linspace(-x_range, x_range, num_points)
    y_val = a * x_val**2 + b * x_val + c
    
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val, y_val, label=f'y = {a}x^2 + {b}x + {c}', color='green')
    PLOT.title(f'Plot of y = {a}x^2 + {b}x + {c}\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def plot_parabola_4(a, b, c, y_range=10, num_points=400):
    """Plot x = ay^2 + by + c"""
    y_val = np.linspace(-y_range, y_range, num_points)
    x_val = a * y_val**2 + b * y_val + c
    
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val, y_val, label=f'x = {a}y^2 + {b}y + {c}', color='green')
    PLOT.title(f'Plot of x = {a}y^2 + {b}y + {c}\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def plot_parabola_5(a, x_value, x_range=10, num_points=400):
    """Plot y^2 = -4ax"""
    x_start = x_value - x_range
    x_end = x_value + x_range
    x_val = np.linspace(x_start, x_end, num_points)
    y_val_positive = np.sqrt(np.maximum(0, -4 * a * x_val))
    y_val_negative = -np.sqrt(np.maximum(0, -4 * a * x_val))
    
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val, y_val_positive, label=f'y = ±sqrt(-4 * {a} * x)', color='green')
    PLOT.plot(x_val, y_val_negative, color='red')
    PLOT.title(f'Plot of y^2 = -4 * {a} * x\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def plot_parabola_6(a, y_value, y_range=10, num_points=400):
    """Plot x^2 = -4ay"""
    y_start = y_value - y_range
    y_end = y_value + y_range
    y_val = np.linspace(y_start, y_end, num_points)
    x_val_positive = np.sqrt(np.maximum(0, -4 * a * y_val))
    x_val_negative = -np.sqrt(np.maximum(0, -4 * a * y_val))
    
    PLOT.figure(figsize=(8, 6))
    PLOT.plot(x_val_positive, y_val, label=f'x = ±sqrt(-4 * {a} * y)', color='green')
    PLOT.plot(x_val_negative, y_val, color='red')
    PLOT.title(f'Plot of x^2 = -4 * {a} * y\nDev: Adnan Adib')
    PLOT.xlabel('x')
    PLOT.ylabel('y')
    PLOT.legend()
    PLOT.grid(True)
    PLOT.show()

def main():
    con = True
    while con:

        interface = '''

choose thr type of parabol to plot:
1> y^2 = 4ax
2> x^2 = 4ay
3> y = ax^2 + bx + c
4> x = ay^2 + by + c
5> y^2 = -4ax
6> x^2 = -4ay

'''
        try:
            print(interface)
            choice = int(input("Enter the choice (1/2/3/4): "))
            
            if choice == 1:
                a = float(input("Enter the coefficient a: "))
                x = float(input("Enter the x value: "))
                plot_parabola_1(a, x)
            elif choice == 2:
                a = float(input("Enter the coefficient a: "))
                y = float(input("Enter the y value: "))
                plot_parabola_2(a, y)
            elif choice == 3:
                a = float(input("Enter the coefficient a: "))
                b = float(input("Enter the coefficient b: "))
                c = float(input("Enter the coefficient c: "))
                plot_parabola_3(a, b, c)
            elif choice == 4:
                a = float(input("Enter the coefficient a: "))
                b = float(input("Enter the coefficient b: "))
                c = float(input("Enter the coefficient c: "))
                plot_parabola_4(a, b, c)
            elif choice == 5:
                a = float(input("Enter the coefficient a: "))
                x = float(input("Enter the x value: "))
                plot_parabola_5(a, x)
            elif choice == 6:
                a = float(input("Enter the coefficient a: "))
                y = float(input("Enter the y value: "))
                plot_parabola_6(a, y)
            else:
                print("invalid")
                continue
            
            command = input("do you want to plot another parabola (y/n): ").strip().lower()
            if command != 'y':
                print("exiting...")
                break
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    main()
