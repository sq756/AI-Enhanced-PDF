import numpy as np
from diffpy.structure import Structure
import os

def load_gr_data(filename):
    """Load G(r) data from .gr or .xye file"""
    data = np.loadtxt(filename)
    if data.shape[1] >= 2:
        r = data[:, 0]
        gr = data[:, 1]
        # If uncertainties are provided
        sigma = data[:, 2] if data.shape[1] >= 3 else None
        return r, gr, sigma
    return None, None, None

def load_cif_structure(filename):
    """Load structure from CIF file"""
    try:
        structure = Structure()
        structure.read(filename)
        return structure
    except Exception as e:
        print(f"Error loading CIF file: {e}")
        return None

def save_structure(structure, filename):
    """Save structure to CIF file"""
    try:
        structure.write(filename, format='cif')
        return True
    except Exception as e:
        print(f"Error saving structure: {e}")
        return False
