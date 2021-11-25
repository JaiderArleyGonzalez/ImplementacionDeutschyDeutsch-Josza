import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

"""========================DeutschCircuito4========================="""
circuit = QuantumCircuit(2, 1)
#Algoritmo de Deutsch
#------Inicio
circuit.x(1)
circuit.barrier(0, 1)
circuit.h(0)
circuit.h(1)
#------Uf

circuit.barrier(0, 1)
circuit.cx(0, 1)
circuit.barrier(0, 1)
#------
circuit.h(0)
circuit.barrier(0, 1)
circuit.measure(0, 0)

#------Fin
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plt.show()
plot_histogram(counts)
