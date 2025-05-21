from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter
from .structure_viewer import StructureViewer
from .pdf_plot import PDFPlot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Fitting GUI")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)
        
        # Create splitter for resizable panels
        splitter = QSplitter()
        layout.addWidget(splitter)
        
        # Left panel: Structure viewer
        self.structure_viewer = StructureViewer()
        splitter.addWidget(self.structure_viewer)
        
        # Right panel: PDF plot
        self.pdf_plot = PDFPlot()
        splitter.addWidget(self.pdf_plot)
        
        # Set initial splitter sizes
        splitter.setSizes([600, 600])
