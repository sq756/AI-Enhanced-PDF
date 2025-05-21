from diffpy.srfit.pdf import PDFContribution
from diffpy.structure import Structure
import numpy as np

class PDFFitter:
    def __init__(self):
        self.contribution = None
        self.structure = None
        
    def load_experimental_data(self, r, gr, sigma=None):
        """Load experimental PDF data"""
        self.contribution = PDFContribution("pdf")
        self.contribution.setData(r, gr, dy=sigma)
        
    def load_structure(self, structure):
        """Load initial structure for fitting"""
        self.structure = structure
        if self.contribution:
            self.contribution.addStructure("structure", self.structure)
            
    def calculate_pdf(self, r):
        """Calculate PDF from current structure"""
        if self.contribution:
            return self.contribution.evaluate()
        return None
        
    def optimize_fit(self, params=None):
        """Perform PDF fitting with optional parameter constraints"""
        if not self.contribution or not self.structure:
            return False
            
        # Set up parameters for refinement
        if params:
            for param, bounds in params.items():
                if param in self.contribution.params:
                    self.contribution.params[param].bounds = bounds
                    
        # Run optimization
        from scipy.optimize import least_squares
        result = least_squares(
            lambda x: self.contribution.residual(),
            x0=self.contribution.getValues(),
            bounds=self.contribution.getBounds()
        )
        
        return result.success
