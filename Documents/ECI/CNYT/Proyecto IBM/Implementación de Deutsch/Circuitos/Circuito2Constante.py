import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

"""========================Circuito Caso 2========================="""
circuit = QuantumCircuit(2, 2)
#circuit.x(0)
#circuit.x(1)
circuit.barrier(0, 1)
circuit.i(0)
circuit.i(1)
circuit.barrier(0, 1)
circuit.measure([0, 1], [1, 0])
compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:", counts)
print(circuit)
plt.show()
plot_histogram(counts)
