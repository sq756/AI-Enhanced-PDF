from PyQt5.QtWidgets import QWidget, QVBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class PDFPlot(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        # Initialize plot
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('r (Å)')
        self.ax.set_ylabel('G(r)')
        self.ax.grid(True)
        
        # Store plot lines
        self.exp_line = None
        self.calc_line = None
        self.diff_line = None
        
    def plot_data(self, r, g_exp=None, g_calc=None):
        """Plot experimental and calculated G(r) data"""
        self.ax.clear()
        
        if g_exp is not None:
            self.exp_line = self.ax.plot(r, g_exp, 'b-', label='Experimental')
            
        if g_calc is not None:
            self.calc_line = self.ax.plot(r, g_calc, 'r-', label='Calculated')
            
            if g_exp is not None:
                diff = g_exp - g_calc
                self.diff_line = self.ax.plot(r, diff + min(g_exp) - 2, 'g-', label='Difference')
        
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
