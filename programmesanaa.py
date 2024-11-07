 x = int(input("Ievadi veselu skaitli x: "))
            y = int(input("Ievadi veselu skaitli y: "))
            return x, y
        except ValueError:
            print("Lūdzu ievadiet veselu skaitli.")

def calculate_expressions(x, y):
    result_1 = (2 + x) / (x * y)
   
    result_2 = 5 * x**3 - x**2 + 7 * x - 6
   
    result_3 = (x * y)**0.5
   
    result_4 = (2 * x * y) / (5 * y)