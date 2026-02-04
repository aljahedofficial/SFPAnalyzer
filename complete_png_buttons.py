#!/usr/bin/env python3
import re

# Chart titles and their IDs - remaining ones
charts = [
    ('Academic Writing Features', 'academicWritingFeatures'),
    ('Readability Indices', 'readabilityIndices'),
    ('Clause-Level Analysis', 'clauseLevelAnalysis'),
    ('Syntactic Constructions', 'syntacticConstructions'),
    ('Discourse & Paragraph Metrics', 'discourseMetrics'),
    ('Discourse Patterns', 'discoursePatterns'),
    ('Stance & Rhetoric', 'stanceRhetoric'),
    ('Functional Grammar (Hallidayan)', 'functionalGrammar'),
    ('Readability & Provenance', 'readabilityProvenance'),
    ('Micro-Syntax & Alternations', 'microSyntax'),
    ('Sentence-Length Heat-Strip', 'sentenceLengthHeatStrip'),
]

with open('src/StylisticFingerprintAnalyzer.jsx', 'r') as f:
    content = f.read()

for title, chart_id in charts:
    # Pattern 1: With mb-4
    pattern = f'<h3 className="text-xl font-semibold text-slate-700 mb-4">{title}</h3>'
    
    if pattern in content:
        replacement = f'''<div className="flex items-center justify-between mb-4">
                                                <h3 className="text-xl font-semibold text-slate-700">{title}</h3>
                                                <button onClick={{() => {{
                                                    const chartDiv = document.querySelector('[data-chart="{chart_id}"]');
                                                    downloadChartPNG(chartDiv, '{chart_id}.png');
                                                }}}} className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm font-semibold flex items-center gap-1">
                                                    📥 PNG
                                                </button>
                                            </div>'''
        
        content = content.replace(pattern, replacement)
        print(f"✓ {title}")
    else:
        print(f"✗ {title} not found")

with open('src/StylisticFingerprintAnalyzer.jsx', 'w') as f:
    f.write(content)

print("\nAll PNG buttons added!")
