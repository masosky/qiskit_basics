import IPython
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit_aer import QasmSimulator

if __name__ == '__main__':
    # StateVector
    sv_initial: Statevector = Statevector.from_int(0, 2 ** 2)
    sv_initial.draw(output='text')
    sv_initial.draw(output='qsphere')
    sv_initial.draw(output='bloch')
    sv_initial_latex: IPython.display.Latex = array_to_latex(sv_initial)

    # Circuit
    circuit = QuantumCircuit(2, 2)
    circuit.h(0) # We apply a Hadamard gate https://quantum-computing.ibm.com/composer/docs/iqx/operations_glossary/#cnot-gate
    circuit.cx(0, 1) # We apply a CNOT gate https://quantum-computing.ibm.com/composer/docs/iqx/operations_glossary/#cnot-gate

    # StateVector after circuit
    sv_final = sv_initial.evolve(other=circuit)
    sv_final.draw(output='qsphere')

    # Measure circuit
    circuit.measure([0, 1], [0, 1])
    circuit.draw(output="mpl")

    # Simulate circuit
    simulator = QasmSimulator()
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    plot_histogram(counts)
    print("\nTotal count for 00 and 11 are:", counts)
