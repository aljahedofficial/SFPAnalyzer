import re

with open('src/StylisticFingerprintAnalyzer.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# List of remaining replacements needed
replacements = [
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

for title, chart_id in replacements:
    # Find and replace the pattern
    old_pattern = f'<h3 className="text-xl font-semibold text-slate-700 mb-4">{title}</h3>'
    if old_pattern in content:
        new_pattern = f'''<div className="flex items-center justify-between mb-4">
                                                <h3 className="text-xl font-semibold text-slate-700">{title}</h3>
                                                <button onClick={{() => {{
                                                    const chartDiv = document.querySelector('[data-chart="{chart_id}"]');
                                                    downloadChartPNG(chartDiv, '{chart_id}.png');
                                                }}}} className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm font-semibold flex items-center gap-1">
                                                    📥 PNG
                                                </button>
                                            </div>'''
        content = content.replace(old_pattern, new_pattern)
        print(f"✓ {title}")
    else:
        print(f"✗ {title}")

with open('src/StylisticFingerprintAnalyzer.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone!")
