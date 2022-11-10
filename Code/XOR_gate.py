def XOR(qc,a,b,output):
    qc.cx(a,output)
    qc.cx(b,output)
