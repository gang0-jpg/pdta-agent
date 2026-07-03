try:
    import cupy as xp

    GPU_AVAILABLE = True
    print("GPU backend : CuPy")

except ImportError:
    import numpy as xp

    GPU_AVAILABLE = False
    print("CPU backend : NumPy")
