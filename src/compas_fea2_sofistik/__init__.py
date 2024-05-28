"""
********************************************************************************
Sofistik
********************************************************************************




.. currentmodule:: compas_fea2_sofistik


.. toctree::
    :maxdepth: 1


"""

from __future__ import print_function

import os
from dotenv import load_dotenv

__author__ = ["Francesco Ranaudo"]
__copyright__ = "Francesco Ranaudo"
__license__ = "MIT License"
__email__ = "ranaudo@arch.ethz.ch"
__version__ = "0.1.0"

HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, "../../"))
DATA = os.path.abspath(os.path.join(HOME, "data"))
DOCS = os.path.abspath(os.path.join(HOME, "docs"))
TEMP = os.path.abspath(os.path.join(HOME, "temp"))


__all__ = ["HOME", "DATA", "DOCS", "TEMP"]

from pydoc import ErrorDuringImport
import compas_fea2

# Models
from compas_fea2.model import Model
from compas_fea2.model import DeformablePart
from compas_fea2.model import Node
# Elements
from compas_fea2.model.elements import (
    MassElement,
    BeamElement,
    TrussElement,
    MembraneElement,
    ShellElement,
    _Element3D,
    TetrahedronElement,
    SpringElement,
)
# Sections
from compas_fea2.model.sections import (
    SpringSection,
    AngleSection,
    BeamSection,
    BoxSection,
    CircularSection,
    HexSection,
    ISection,
    MassSection,
    PipeSection,
    RectangularSection,
    SpringSection,
    StrutSection,
    TieSection,
    TrapezoidalSection,
    TrussSection,
    MembraneSection,
    ShellSection,
    SolidSection,
)
# Materials
from compas_fea2.model.materials.material import (
    ElasticIsotropic,
    ElasticOrthotropic,
    ElasticPlastic,
    Stiff,
    UserMaterial,
)
from compas_fea2.model.materials.concrete import (
    Concrete,
    ConcreteDamagedPlasticity,
    ConcreteSmearedCrack,
)
from compas_fea2.model.materials.steel import (
    Steel,
)
# Groups
from compas_fea2.model.groups import (
    NodesGroup,
    ElementsGroup,
    FacesGroup,
)

# Constraints
from compas_fea2.model.constraints import (
    TieConstraint,
)

# Connectors
from compas_fea2.model.connectors import (
    SpringConnector,
    ZeroLengthSpringConnector,
)

# Releases
from compas_fea2.model.releases import (
    BeamEndPinRelease,
)

# Boundary Conditions
from compas_fea2.model.bcs import (
    FixedBC,
    FixedBCX,
    FixedBCY,
    FixedBCZ,
    ClampBCXX,
    ClampBCYY,
    ClampBCZZ,
    PinnedBC,
    RollerBCX,
    RollerBCXY,
    RollerBCXZ,
    RollerBCY,
    RollerBCYZ,
    RollerBCZ,
)

# Problem
from compas_fea2.problem import Problem
# Steps
from compas_fea2.problem.steps import (
    ModalAnalysis,
    ComplexEigenValue,
    StaticStep,
    LinearStaticPerturbation,
    BucklingAnalysis,
    DynamicStep,
    QuasiStaticStep,
    DirectCyclicStep,
)
# Loads
from compas_fea2.problem.loads import (
    NodeLoad,
    EdgeLoad,
    FaceLoad,
    TributaryLoad,
    PrestressLoad,
    GravityLoad,
    HarmonicPointLoad,
    HarmonicPressureLoad,
)
# Displacements
from compas_fea2.problem.displacements import (
    GeneralDisplacement,
)
# Displacements
from compas_fea2.problem.combinations import (
    LoadCombination,
)
# Outputs
from compas_fea2.problem.outputs import (
    FieldOutput,
    HistoryOutput,
)

# Results
from compas_fea2.results import (
    Result,
    DisplacementResult,
    StressResult,
    DisplacementFieldResults,
    StressFieldResults,
)

# Input File
from compas_fea2.job import (
    InputFile,
    ParametersFile,
)
# =========================================================================
#                           OPENSEES CLASSES
# =========================================================================

try:
    # Opensees Models
    from .model import SofistikModel
    from .model import SofistikDeformablePart
    from .model import SofistikNode

    # Sofistik Elements
    from .model.elements import (
        SofistikMassElement,
        SofistikSpringElement,
        SofistikBeamElement,
        SofistikTrussElement,
        SofistikMembraneElement,
        SofistikShellElement,
        SofistikTetrahedronElement,
    )

    # Sofistik Sections
    from .model.sections import (
        SofistikSpringSection,
        SofistikAngleSection,
        SofistikBeamSection,
        SofistikBoxSection,
        SofistikCircularSection,
        SofistikHexSection,
        SofistikISection,
        SofistikMassSection,
        SofistikPipeSection,
        SofistikRectangularSection,
        SofistikSpringSection,
        SofistikStrutSection,
        SofistikTieSection,
        SofistikTrapezoidalSection,
        SofistikTrussSection,
        SofistikMembraneSection,
        SofistikShellSection,
        SofistikSolidSection,
    )

    # Sofistik Materials
    from .model.materials.material import (
        SofistikElasticIsotropic,
        SofistikElasticOrthotropic,
        SofistikElasticPlastic,
        SofistikStiff,
        SofistikUserMaterial,
    )
    from .model.materials.concrete import (
        SofistikConcrete,
        SofistikConcreteDamagedPlasticity,
        SofistikConcreteSmearedCrack,
    )
    from .model.materials.steel import (
        SofistikSteel,
    )
    # Sofistik Groups
    from .model.groups import (
        SofistikNodesGroup,
        SofistikElementsGroup,
        SofistikFacesGroup,
    )

    # Sofistik Constraints
    from .model.constraints import (
        SofistikTieConstraint,
    )

    # Sofistik Connectors
    from .model.connectors import (
        SofistikSpringConnector,
        SofistikZeroLengthSpringConnector,
    )

    # Sofistik release
    from .model.releases import (
        SofistikBeamEndPinRelease,
    )

    # Sofistik Boundary Conditions
    from .model.bcs import (
        SofistikFixedBC,
        SofistikFixedBCX,
        SofistikFixedBCY,
        SofistikFixedBCZ,
        SofistikClampBCXX,
        SofistikClampBCYY,
        SofistikClampBCZZ,
        SofistikPinnedBC,
        SofistikRollerBCX,
        SofistikRollerBCXY,
        SofistikRollerBCXZ,
        SofistikRollerBCY,
        SofistikRollerBCYZ,
        SofistikRollerBCZ,
    )

    # Sofistik Problem
    from .problem import SofistikProblem

    # Sofistik Steps
    from .problem.steps import (
        SofistikModalAnalysis,
        SofistikComplexEigenValue,
        SofistikStaticStep,
        SofistikLinearStaticPerturbation,
        SofistikBucklingAnalysis,
        SofistikDynamicStep,
        SofistikQuasiStaticStep,
        SofistikDirectCyclicStep,
    )
    # Sofistik Loads
    from .problem.loads import (
        SofistikNodeLoad,
        SofistikTributaryLoad,
        SofistikPrestressLoad,
        SofistikGravityLoad,
        SofistikHarmonicPointLoad,
        SofistikHarmonicPressureLoad,
    )

    # Sofistik Displacements
    from .problem.displacements import (
        SofistikGeneralDisplacement,
    )

    # Sofistik Displacements
    from .problem.combinations import (
        SofistikLoadCombination,
    )

    # Sofistik outputs
    from .problem.outputs import (
        SofistikFieldOutput,
        SofistikHistoryOutput,
    )

    # Sofistik Results
    from .results import (
        SofistikResult,
        SofistikDisplacementResult,
        SofistikStressResult,
        SofistikDisplacementFieldResults,
        SofistikStressFieldResults,
    )

    # Sofistik Input File
    from .job import(
        SofistikInputFile,
        SofistikParametersFile,
    )

    # build the plugin registry
    def _register_backend():
        backend = compas_fea2.BACKENDS['compas_fea2_sofistik']

        backend[Model] = SofistikModel
        backend[DeformablePart] = SofistikDeformablePart
        backend[Node] = SofistikNode

        backend[MassElement] = SofistikMassElement
        backend[SpringElement] = SofistikSpringElement
        backend[BeamElement] = SofistikBeamElement
        backend[TrussElement] = SofistikTrussElement
        backend[MembraneElement] = SofistikMembraneElement
        backend[ShellElement] = SofistikShellElement
        backend[TetrahedronElement] = SofistikTetrahedronElement

        backend[SpringSection] = SofistikSpringSection
        backend[AngleSection] = SofistikAngleSection
        backend[BeamSection] = SofistikBeamSection
        backend[BoxSection] = SofistikBoxSection
        backend[CircularSection] = SofistikCircularSection
        backend[HexSection] = SofistikHexSection
        backend[ISection] = SofistikISection
        backend[MassSection] = SofistikMassSection
        backend[MembraneSection] = SofistikMembraneSection
        backend[PipeSection] = SofistikPipeSection
        backend[RectangularSection] = SofistikRectangularSection
        backend[ShellSection] = SofistikShellSection
        backend[SolidSection] = SofistikSolidSection
        backend[SpringSection] = SofistikSpringSection
        backend[StrutSection] = SofistikStrutSection
        backend[TieSection] = SofistikTieSection
        backend[TrapezoidalSection] = SofistikTrapezoidalSection
        backend[TrussSection] = SofistikTrussSection

        backend[ElasticIsotropic] = SofistikElasticIsotropic
        backend[ElasticOrthotropic] = SofistikElasticOrthotropic
        backend[ElasticPlastic] = SofistikElasticPlastic
        backend[Stiff] = SofistikStiff
        backend[UserMaterial] = SofistikUserMaterial
        backend[Concrete] = SofistikConcrete
        backend[ConcreteDamagedPlasticity] = SofistikConcreteDamagedPlasticity
        backend[ConcreteSmearedCrack] = SofistikConcreteSmearedCrack
        backend[Steel] = SofistikSteel

        backend[NodesGroup] = SofistikNodesGroup
        backend[ElementsGroup] = SofistikElementsGroup
        backend[FacesGroup] = SofistikFacesGroup

        backend[TieConstraint] = SofistikTieConstraint

        backend[SpringConnector] = SofistikSpringConnector
        backend[ZeroLengthSpringConnector] = SofistikZeroLengthSpringConnector

        backend[BeamEndPinRelease] = SofistikBeamEndPinRelease

        backend[FixedBC] = SofistikFixedBC
        backend[FixedBCX] = SofistikFixedBCX
        backend[FixedBCY] = SofistikFixedBCY
        backend[FixedBCZ] = SofistikFixedBCZ
        backend[ClampBCXX] = SofistikClampBCXX
        backend[ClampBCYY] = SofistikClampBCYY
        backend[ClampBCZZ] = SofistikClampBCZZ
        backend[PinnedBC] = SofistikPinnedBC
        backend[RollerBCX] = SofistikRollerBCX
        backend[RollerBCXY] = SofistikRollerBCXY
        backend[RollerBCXZ] = SofistikRollerBCXZ
        backend[RollerBCY] = SofistikRollerBCY
        backend[RollerBCYZ] = SofistikRollerBCYZ
        backend[RollerBCZ] = SofistikRollerBCZ

        backend[Problem] = SofistikProblem

        backend[ModalAnalysis] = SofistikModalAnalysis
        backend[ComplexEigenValue, StaticStep] = SofistikComplexEigenValue
        backend[StaticStep] = SofistikStaticStep
        backend[LinearStaticPerturbation] = SofistikLinearStaticPerturbation
        backend[BucklingAnalysis] = SofistikBucklingAnalysis
        backend[DynamicStep] = SofistikDynamicStep
        backend[QuasiStaticStep] = SofistikQuasiStaticStep
        backend[DirectCyclicStep] = SofistikDirectCyclicStep

        backend[GravityLoad] = SofistikGravityLoad
        backend[NodeLoad] = SofistikNodeLoad
        backend[TributaryLoad] = SofistikTributaryLoad
        backend[PrestressLoad] = SofistikPrestressLoad
        backend[HarmonicPointLoad] = SofistikHarmonicPointLoad
        backend[HarmonicPressureLoad] = SofistikHarmonicPressureLoad

        backend[GeneralDisplacement] = SofistikGeneralDisplacement

        backend[LoadCombination] = SofistikLoadCombination

        backend[FieldOutput] = SofistikFieldOutput
        backend[HistoryOutput] = SofistikHistoryOutput

        backend[Result] = SofistikResult
        backend[DisplacementResult] = SofistikDisplacementResult
        backend[StressResult] = SofistikStressResult
        backend[DisplacementFieldResults] = SofistikDisplacementFieldResults
        backend[StressFieldResults] = SofistikStressFieldResults

        backend[InputFile] = SofistikInputFile
        backend[ParametersFile] = SofistikParametersFile

        print('Sofistik implementations registered...')
except:
    raise ErrorDuringImport()



def init_fea2_Sofistik(exe):
    """Create a default environment file if it doesn't exist and loads its variables.

    Parameters
    ----------
    verbose : bool, optional
        Be verbose when printing output, by default False
    point_overlap : bool, optional
        Allow two nodes to be at the same location, by default True
    global_tolerance : int, optional
        Tolerance for the model, by default 1
    precision : str, optional
        Values approximation, by default '3f'

    """

    env_path = os.path.abspath(os.path.join(HERE, ".env"))
    with open(env_path, "x") as f:
        f.write(
            "\n".join(
                [
                    "EXE={}".format(exe),
                ]
            )
        )
    load_dotenv(env_path)


if not load_dotenv():

    from sys import platform

    if platform == "linux" or platform == "linux2":
        # linux
        raise ValueError('Sofistik is not available on Linux')
    elif platform == "darwin":
        # OS X
        raise ValueError('Sofistik is not available on OS')
    elif platform == "win32":
        # Windows
        exe = 'C:/Program Files/SOFiSTiK/2024/SOFiSTiK 2024'
    else:
        raise ValueError('you must specify the location of the solver.')
    init_fea2_Sofistik(exe)

EXE = os.getenv("EXE")
