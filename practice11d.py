# Single Level

class A:
    pass

class B(A):
    pass


# Multi Level

class A:
    pass

class B(A):
    pass

class C(B):
    pass

# Hierarchy

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A):
    pass

# Multiple

class A:
    pass

class E:
    pass

class F(A,E):
    pass

# Hybrid

class G(A):
    pass


