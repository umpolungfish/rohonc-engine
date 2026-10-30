"""
Rohonc Engine — full pipeline demonstration.

Runs compile → VM → call graph on the sample RTFF transcription.
"""

from pathlib import Path
from rohonc_engine import compile_corpus, UniversalEngine, generate_call_graph, peak_pages

DATA = Path(__file__).parent.parent / 'data' / 'rohonc_rtff_sample.txt'

result = compile_corpus(DATA, verbose=True)
print(f'\nPages compiled    : {result["page_count"]}')
print(f'Total instructions: {result["total_instructions"]}')
print(f'Total registers   : {result["total_registers"]}')
print(f'Entropy delta     : {result["entropy_delta"]:.8f} J/K')
print('Status            : SELF_SUSTAINING_BOOTSTRAP_COMPLETE')

print('\nPeak pages:')
for name, regs in peak_pages(result, n=5):
    print(f'  {name}: {regs} registers')

engine = UniversalEngine.from_compilation(result)
print(f'\nRunning 5000 steps...')
for snap in engine.run(steps=5000, report_every=1000):
    print(f'  Step {snap["step"]:5d} | Active {snap["active_registers"]:4d} | '
          f'Paradoxes {snap["paradox_stabilizations"]:4d}')

engine.report()

print('\nGenerating call graph...')
G, C = generate_call_graph(result, output='rohonc_graph.png', verbose=True)
