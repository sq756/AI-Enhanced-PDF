# PDF Fitting GUI

An interactive GUI application for PDF (Pair Distribution Function) analysis and structure refinement.

## Features

- Load and visualize experimental G(r) data
- Import crystal structures from CIF files
- Interactive 3D structure visualization and editing using Napari
- Real-time PDF calculation and comparison with experimental data
- Structure refinement using DiffPy
- Optional CGAN-based structure suggestion (experimental)

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

## Project Structure

- `main.py`: Application entry point
- `ui/`: User interface components
  - `main_window.py`: Main application window
  - `structure_viewer.py`: 3D structure visualization (Napari)
  - `pdf_plot.py`: G(r) plotting component
- `fitting/`: PDF calculation and fitting
  - `diffpy_fit.py`: DiffPy-based PDF calculator and fitter
  - `cgan_model.py`: Machine learning structure generator
- `utils/`: Helper functions
  - `file_io.py`: Data import/export utilities

## Dependencies

- DiffPy-CMI: PDF calculation and fitting
- PyQt5: GUI framework
- Napari: 3D visualization
- Matplotlib: 2D plotting
- PyTorch: Machine learning (CGAN)
- NumPy/SciPy: Numerical computations

## License

MIT License
