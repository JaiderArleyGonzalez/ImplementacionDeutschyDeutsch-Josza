import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

"""========================Deutsch-JozsaCircuito2========================="""
circuit = QuantumCircuit(3, 2)
#Algoritmo de Deutsch-Jozsa
#------Inicio
circuit.x(2)
circuit.barrier(range(3))
circuit.h(range(3))
#------Uf
circuit.barrier(range(3))
circuit.i(range(3))
circuit.barrier(range(3))
#------
circuit.h((0, 1))
circuit.barrier(range(3))
circuit.measure((0, 1), (0, 1))

#------Fin
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 000 and 111 are:", counts)
print(circuit)
plt.show()
plot_histogram(counts)
