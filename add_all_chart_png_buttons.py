#!/usr/bin/env python3
"""
Add PNG download buttons to ALL chart sections in StylisticFingerprintAnalyzer.jsx
Safely handles the JSX structure by matching exact patterns.
"""

import re

with open('src/StylisticFingerprintAnalyzer.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Charts that need PNG buttons - these are all h3 titles with mb-4 class
# that represent actual chart/metric sections
charts_to_update = {
    'Lexical First-Appearance Distribution': 'lexicalFirstAppearance',
    'Stylometric Profile': 'stylometricProfile',
    'Lexical Sophistication': 'lexicalSophistication',
    'Syntactic Complexity': 'syntacticComplexity',
    'Extended Metadiscourse (per 1,000 words)': 'extendedMetadiscourse',
    'Cohesion Features': 'cohesionFeatures',
    'Advanced Lexical Diversity': 'advancedLexicalDiversity',
    'Linguistic Style': 'linguisticStyle',
    'Academic Writing Features': 'academicWritingFeatures',
    'Readability Indices': 'readabilityIndices',
    'Clause-Level Analysis': 'clauseLevelAnalysis',
    'Syntactic Constructions': 'syntacticConstructions',
    'Discourse & Paragraph Metrics': 'discourseMetrics',
    'Discourse Patterns': 'discoursePatterns',
    'Stance & Rhetoric': 'stanceRhetoric',
    'Functional Grammar (Hallidayan)': 'functionalGrammar',
    'Readability & Provenance': 'readabilityProvenance',
    'Micro-Syntax & Alternations': 'microSyntax',
    'Sentence-Length Heat-Strip': 'sentenceLengthHeatStrip',
}

count = 0
for title, chart_id in charts_to_update.items():
    # Try to find this chart - look for the h3 with mb-4 or without
    patterns = [
        # Pattern 1: h3 with mb-4 inside a white div
        (f'<h3 className="text-xl font-semibold text-slate-700 mb-4">{re.escape(title)}</h3>',
         f'''<div className="flex items-center justify-between mb-4">
                                                <h3 className="text-xl font-semibold text-slate-700">{title}</h3>
                                                <button onClick={{() => {{
                                                    const chartDiv = document.querySelector('[data-chart="{chart_id}"]');
                                                    downloadChartPNG(chartDiv, '{chart_id}.png');
                                                }}}} className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm font-semibold flex items-center gap-1">
                                                    📥 PNG
                                                </button>
                                            </div>'''),
    ]
    
    for old_pattern, new_pattern in patterns:
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            count += 1
            print(f"✓ {title}")
            break
    else:
        print(f"✗ {title} - not found or already has button")

with open('src/StylisticFingerprintAnalyzer.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Updated {count} charts with PNG buttons")
