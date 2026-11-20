"""
Join order optimization via QUBO, packaged from base/Scripts of
https://github.com/lfd/sigmod23-reproduction (GPL-2.0).

Modules:
    SteinbrunnQueryGenerator  generate random join ordering problems
    QUBOGenerator             build the QUBO (does not require Gurobi WLS credentials, since we do not use optimize())
    Postprocessing            decode solver samples into join orders, brute force reference
"""
