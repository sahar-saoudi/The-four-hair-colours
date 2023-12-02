from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import matplotlib.pyplot as plt
from qiskit.visualization import plot_gate_map, plot_histogram
from qiskit_aer import AerSimulator

def showcircuit(number_of_heads):

    number_of_qubits = 2 * number_of_heads
    number_of_heads_counter = number_of_heads - 1
    
    qreg = QuantumRegister(number_of_qubits, "q")
    creg = ClassicalRegister(number_of_qubits, "c")

    circuit = QuantumCircuit(qreg,creg)

    for counter in range(number_of_heads):

        circuit.h(qreg[counter])
        
    circuit.barrier()

    for counter_direction in range(number_of_heads - 1):

        for counter_vision in range(number_of_heads_counter):

            circuit.cx(qreg[counter_vision + 1], qreg[number_of_heads + counter_direction])
        
        circuit.barrier()

        for compteurCommunication in range(number_of_heads_counter):
            compteurCommunication = compteurCommunication + counter_direction
            circuit.cx(qreg[number_of_heads + counter_direction], qreg[compteurCommunication + 1 + number_of_heads])

        circuit.barrier()

        number_of_heads_counter = number_of_heads_counter- 1

    circuit.measure_all()
        
    return circuit
circuit = showcircuit(4)

print(circuit)
circuit.draw(output="mpl", style="clifford")
plt.show()