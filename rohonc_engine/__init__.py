"""Rohonc Engine — Universal Imscriptive Grammar compilation of the Rohonc Codex."""

from .compiler import compile_corpus, peak_pages, write_log
from .runtime import UniversalEngine
from .callgraph import generate_call_graph
from .sectional import generate_sectional_graphs, classify_page
from .primitives import PRIMITIVES, FLUX, BOOTSTRAP_SEQUENCE, SECTIONS

__all__ = [
    'compile_corpus',
    'peak_pages',
    'write_log',
    'UniversalEngine',
    'generate_call_graph',
    'generate_sectional_graphs',
    'classify_page',
    'PRIMITIVES',
    'FLUX',
    'BOOTSTRAP_SEQUENCE',
    'SECTIONS',
]
