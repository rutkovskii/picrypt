######################################################

# Playing around with the original example code
# When inputset = [(254, 200), (0, 0)], compiler does not compile at all after even 10 minutes

######################################################


import concrete.numpy as cnp


def add(x, y):
    return x + y


compiler = cnp.Compiler(add, {"x": "encrypted", "y": "encrypted"})
#inputset = [(254, 200), (0, 0)]
inputset =[(1, 6), (7, 7), (7, 1), (3, 2), (6, 1), (1, 7), (4, 5), (5, 4)]


print(f"Compiling...")
circuit = compiler.compile(inputset)

examples = [(7, 2), (1, 2), (7, 7), (0, 0)]
for example in examples:
    result = circuit.encrypt_run_decrypt(*example)
    print(f"Evaluation of {' - '.join(map(str, example))} homorphically = {result}")