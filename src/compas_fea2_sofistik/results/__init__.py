"""
********************************************************************************
abaqus.results
********************************************************************************

.. currentmodule:: compas_fea2.backends.abaqus.problem

Results
=======
.. autosummary::
    :toctree: generated/

    Results

"""


# additional software-based classes
from .results import (
    SofistikResult,
    SofistikDisplacementResult,
    SofistikStressResult,
    SofistikDisplacementFieldResults,
    SofistikStressFieldResults,
)
# from .results_to_sql import read_results_file


# __all__ = [name for name in dir() if not name.startswith('_')]
