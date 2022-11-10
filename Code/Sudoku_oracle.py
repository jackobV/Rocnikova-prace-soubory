def sudoku_oracle(qc,clause_list,clause_qubits):
    i=0
    for clause in clause_list:
        XOR(qc,clause[0],clause[1], clause_qubits[i])
        i +=1
    qc.mct(clause_qubits, output_qubit)
    i = 0
    for clause in clause_list:
        XOR(qc,clause[0],clause[1], clause_qubits[i])
        i +=1
sudoku_oracle(qc, clause_list, clause_qubits)
qc.draw()
