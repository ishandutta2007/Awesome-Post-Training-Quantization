import os
import re

base_dir = r'C:\Users\ishan\Documents\Projects\Awesome-Post-Training-Quantization'
details_dir = os.path.join(base_dir, 'details')
assets_dir = os.path.join(base_dir, 'assets')
os.makedirs(details_dir, exist_ok=True)
os.makedirs(assets_dir, exist_ok=True)

svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="#1e1e2e"/>
    <text x="50%" y="50%" font-family="Arial" font-size="36" fill="#cba6f7" text-anchor="middle" dominant-baseline="middle">Awesome Post-Training Quantization</text>
    <text x="50%" y="75%" font-family="Arial" font-size="18" fill="#a6e3a1" text-anchor="middle" dominant-baseline="middle">Evolution, Variants, and Applications</text>
</svg>'''
with open(os.path.join(assets_dir, 'banner.svg'), 'w') as f:
    f.write(svg_content)

readme_path = os.path.join(base_dir, 'README.md')
with open(readme_path, 'r', encoding='utf-8') as f:
    readme = f.read()

bullets = [
    ('The Flat Heuristic Era (Pre-2022)', 'flat_heuristic_era'),
    ('The Activation-Aware & Hessian Optimization Era (~2022–2024)', 'activation_aware_hessian'),
    ('Modern Low-Precision Hardware Convergence (~2025–Present)', 'hardware_convergence'),
    ('Weight-Only Quantization (W4A16 / W8A16)', 'weight_only'),
    ('Weight-Activation Quantization (W8A8 / W4A4)', 'weight_activation'),
    ('Per-Tensor Quantization', 'per_tensor'),
    ('Per-Channel Quantization', 'per_channel'),
    ('Group-Wise (Block) Quantization', 'group_wise'),
    ('GPTQ (Generalized Post-Training Quantization)', 'gptq'),
    ('AWQ (Activation-Aware Weight Quantization)', 'awq'),
    ('SmoothQuant', 'smoothquant'),
    ('Edge & Mobile Device Engine Execution', 'edge_mobile'),
    ('High-Volume Production LLM Serving Pipelines', 'high_volume_llm'),
    ('Automotive TinyML Microcontrollers', 'automotive_tinyml')
]

for title, filename in bullets:
    filepath = os.path.join(details_dir, f'{filename}.md')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n## Overview\nThis page provides detailed information about {title}.\n\n## Diagram\n```mermaid\ngraph TD;\n    A[{title}] --> B[Details and Application];\n```\n\n[Back to README](../README.md)\n')
    
    pattern = re.compile(re.escape(f'**{title}**'))
    readme = pattern.sub(f'**[{title}](details/{filename}.md)**', readme)

badges = '''<div align="center">
<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>
</div>'''
banner = '''<div align="center">\n<img src="assets/banner.svg" alt="Banner" />\n</div>'''

if '# Awesome-Post-Training-Quantization' in readme:
    readme = readme.replace('# Awesome-Post-Training-Quantization', f'{banner}\n\n# 🌟 Awesome-Post-Training-Quantization 🚀\n\n{badges}\n')
else:
    readme = f'{banner}\n\n# 🌟 Awesome-Post-Training-Quantization 🚀\n\n{badges}\n\n' + readme

readme = readme.replace('## Post-Training Quantization (PTQ): Evolution, Variants, & Applications', '## 📚 Post-Training Quantization (PTQ): Evolution, Variants, & Applications ✨')
readme = readme.replace('## 1. The Chronological Evolution', '## ⏳ 1. The Chronological Evolution')
readme = readme.replace('## 2. Parameter Scope Variants', '## 🎯 2. Parameter Scope Variants')
readme = readme.replace('## 3. Mathematical Matrix Granularities', '## 📐 3. Mathematical Matrix Granularities')
readme = readme.replace('## 4. Modern Core Algorithmic Frameworks', '## 🧠 4. Modern Core Algorithmic Frameworks')
readme = readme.replace('## 5. Production Infrastructure Deployments', '## 🏭 5. Production Infrastructure Deployments')

star_history = '''
## ⭐ Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Post-Training-Quantization&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Post-Training-Quantization&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Post-Training-Quantization&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Post-Training-Quantization&type=date&legend=bottom-right" />
</picture>
</a>
</div>
'''
if '## ⭐ Star History' not in readme:
    readme += star_history

readme = readme.replace('chartrepos', 'chart?repos')
readme = readme.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme)
