#!/usr/bin/env python3
import re

# Read the JSX file
with open('src/StylisticFingerprintAnalyzer.jsx', 'r') as f:
    content = f.read()

# List of charts to modify with their titles and IDs
charts = [
    ('Lexical Sophistication', 'lexicalSophistication'),
    ('Syntactic Complexity', 'syntacticComplexity'),
    ('Extended Metadiscourse (per 1,000 words)', 'extendedMetadiscourse'),
    ('Cohesion Features', 'cohesionFeatures'),
    ('Advanced Lexical Diversity', 'advancedLexicalDiversity'),
    ('Linguistic Style', 'linguisticStyle'),
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

# Pattern to find chart titles
for title, chart_id in charts:
    # Find the pattern with the h3 tag
    pattern = rf'(<h3 className="text-xl font-semibold text-slate-700 mb-4">{re.escape(title)}</h3>)'
    
    # Check if this pattern needs fixing
    if re.search(pattern, content):
        # Check if it already has the flex/button structure
        # Look for the h3 within a flex container
        flex_pattern = rf'(<div className="flex items-center justify-between mb-4">\s*<h3 className="text-xl font-semibold text-slate-700">{re.escape(title)}</h3>)'
        
        if not re.search(flex_pattern, content):
            # Replace the standalone h3 with flex container + button
            replacement = f'''<div className="flex items-center justify-between mb-4">
                                                <h3 className="text-xl font-semibold text-slate-700">{title}</h3>
                                                <button onClick={{() => {{
                                                    const chartDiv = document.querySelector('[data-chart="{chart_id}"]');
                                                    downloadChartPNG(chartDiv, '{chart_id}.png');
                                                }}}} className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm font-semibold flex items-center gap-1">
                                                    📥 PNG
                                                </button>
                                            </div>'''
            
            content = re.sub(pattern, replacement, content)
            print(f"✓ Added PNG button to {title}")
        else:
            print(f"✓ {title} already has PNG button")
    else:
        print(f"! Could not find pattern for {title}")

# Write the modified content back
with open('src/StylisticFingerprintAnalyzer.jsx', 'w') as f:
    f.write(content)

print("\nDone! PNG buttons have been added to all charts.")
