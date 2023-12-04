cat > #!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure tuples have at least two elements by padding with zeros if necessary
    tuple_a += (0, 0) if len(tuple_a) < 2 else ()
    tuple_b += (0, 0) if len(tuple_b) < 2 else ()
    
    # Perform element-wise addition
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    
    return new_tuple

