from qiskit.quantum_info import Statevector

if __name__ == '__main__':
    # StateVector
    psi_sv_initial: Statevector = Statevector([0, 0, 1, 0])  # 10>
    phi_sv_initial: Statevector = Statevector([1, 0, 0, 0])  # 00>

    psi_sv_initial.draw(output='qsphere')
    phi_sv_initial.draw(output='qsphere')

    # Project phi on psi
    projector = phi_sv_initial.to_operator()
    result = psi_sv_initial.evolve(projector)

    result.draw(output='bloch')

    print('END')
