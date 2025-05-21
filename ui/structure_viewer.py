from PyQt5.QtWidgets import QWidget, QVBoxLayout
import napari
from napari.qt.threading import thread_worker
import numpy as np

class StructureViewer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create napari viewer
        self.viewer = napari.Viewer(show=False)
        layout.addWidget(self.viewer.window._qt_window)
        
        # Initialize empty structure
        self.atoms = None
        self.positions = None
        
    def load_structure(self, structure):
        """Load atomic structure from DiffPy/ASE structure object"""
        # Convert atomic positions to numpy array
        self.positions = np.array([atom.xyz for atom in structure])
        self.atoms = [atom.element for atom in structure]
        
        # Clear previous layers
        self.viewer.layers.clear()
        
        # Add points layer for atoms
        self.viewer.add_points(
            self.positions,
            size=10,
            name='Atoms',
            edge_color='black',
            face_color='white'
        )
        
    def get_structure(self):
        """Return current structure as positions and atom types"""
        return self.positions, self.atoms
