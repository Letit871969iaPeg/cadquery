"""
CadQuery - A parametric 3D CAD scripting framework

CadQuery is a Python library that allows you to build 3D models
using a fluent, chainable API built on top of OpenCASCADE Technology (OCCT).

Example usage::

    import cadquery as cq

    result = (
        cq.Workplane("XY")
        .box(10, 10, 5)
        .faces(">Z")
        .workplane()
        .hole(3)
    )

Personal fork notes:
- Added `cq` alias to __all__ so it shows up in tab-completion and help().
- Keeping track of upstream version for easy diffing.
- Added __author_email__ and __url__ metadata for quick reference.
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .occ_impl.geom import (
    Vector,
    Matrix,
    Plane,
    Location,
)
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from .occ_impl.assembly import (
    Assembly,
    Constraint,
)
from .selectors import (
    Selector,
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    RadiusNthSelector,
    CenterNthSelector,
    LengthNthSelector,
    SumSelector,
    SubtractSelector,
    AndSelector,
    InverseSelector,
    StringSyntaxSelector,
)
from .sketch import Sketch
from . import exporters
from . import importers

__version__ = "2.4.0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"
# Added for quick reference when inspecting the package interactively
__url__ = "https://github.com/CadQuery/cadquery"
__author_email__ = "cadquery@googlegroups.com"

# Convenience alias - also exposed in __all__ so it appears in tab-completion
cq = Workplane

__all__ = [
    # Core
    "Workplane",
    "CQContext",
    "CQObject",
    # Convenience alias
    "cq",
    # Geometry
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    # Shapes
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    # Assembly
    "Assembly",
    "Constraint",
    # Selectors
    "Selector",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "RadiusNthSelector",
    "CenterNthSelector",
    "LengthNthSelector",
    "SumSelector",
    "SubtractSelector",
    "AndSelector",
    "InverseSelector",
    "StringSyntaxSelector",
    # Sketch
    "Sketch",
    # Modules
    "exporters",
    "importers",
    # Version / metadata
    "__version__",
    "__url__",
    "__author_email__",
]
