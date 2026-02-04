import re

# Read the file
with open('StylisticFingerprintAnalyzer.jsx', 'r') as f:
    content = f.read()

# List of all chart sections that need buttons
charts = [
    ('Lexical First-Appearance Distribution', 'lexfirst', 'individual'),
    ('Stylometric Profile', 'stylometric', 'tier2'),
    ('Lexical Sophistication', 'lexsoph', 'tier2'),
    ('Syntactic Complexity', 'syntaxcomp', 'tier2'),
    ('Extended Metadiscourse (per 1,000 words)', 'extmetadiscourse', 'tier2'),
    ('Coherence Features', 'cohesion', 'tier2'),
    ('Advanced Lexical Diversity', 'lexdiversity', 'tier3'),
    ('Linguistic Style', 'lingstyle', 'tier4'),
    ('Academic Writing Features', 'academic', 'tier4'),
    ('Readability & Provenance', 'readability', 'tier6'),
    ('Micro-Syntax & Alternations', 'microsyntax', 'tier6'),
    ('Sentence Complexity Distribution', 'sentcomplex', 'individual'),
    ('Metric Scatterplot Matrix', 'scattermatrix', 'individual'),
    ('Burstiness Gauge', 'burstigauge', 'individual'),
]

# Pattern 1: Regular h3 with mb-4
pattern_mb4 = re.compile(r'<h3 className="text-xl font-semibold text-slate-700 mb-4">([^<]+)<\/h3>')

# Find all matches
for match in pattern_mb4.finditer(content):
    title = match.group(1)
    for chart_title, chart_id, _ in charts:
        if title == chart_title:
            # Replace this specific match
            old_text = match.group(0)
            new_text = f'''<div className="flex items-center justify-between mb-4">
                                                <h3 className="text-xl font-semibold text-slate-700">{title}</h3>
                                                <button onClick={{() => {{
                                                    const chartDiv = document.querySelector('[data-chart="{chart_id}"]');
                                                    downloadChartPNG(chartDiv, '{chart_id}.png');
                                                }}}} className="px-3 py-1 bg-blue-600 text-white rounded hover:bg-blue-700 text-sm font-semibold flex items-center gap-1">
                                                    📥 PNG
                                                </button>
                                            </div>
                                            <div data-chart="{chart_id}">'''
            content = content.replace(old_text, new_text, 1)
            print(f"✓ Added button to {title}")
            break

# Write back
with open('StylisticFingerprintAnalyzer.jsx', 'w') as f:
    f.write(content)

print("\nDone!")
