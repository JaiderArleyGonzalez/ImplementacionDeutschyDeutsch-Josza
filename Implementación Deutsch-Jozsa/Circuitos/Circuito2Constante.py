import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

"""========================Circuito2========================="""
circuit = QuantumCircuit(3, 3)
#circuit.x(0)
#circuit.x(1)
#circuit.x(2)
#------Uf
circuit.barrier(range(3))
circuit.i(range(3))
circuit.barrier(range(3))
circuit.measure((0, 1, 2), (2, 1, 0))


compiled_circuit = transpile(circuit, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()
counts = result.get_counts(circuit)
print("\nTotal count for 000 and 111 are:", counts)
print(circuit)
plt.show()
plot_histogram(counts)
