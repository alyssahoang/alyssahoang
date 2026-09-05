import random, sys
random.seed(7)
W, H = 1000, 300
out = []
a = out.append
a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Fira Code, JetBrains Mono, Cascadia Code, Consolas, Menlo, monospace">')
import os
_css=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fira-code.css'),encoding='utf-8').read()
a('''<defs>
  <style>'''+_css+'''</style>
  <linearGradient id="room" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0B1220"/><stop offset="1" stop-color="#111827"/></linearGradient>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F172A"/><stop offset="0.6" stop-color="#172554"/><stop offset="1" stop-color="#1D4ED8"/></linearGradient>
  <radialGradient id="lamp" cx="0.5" cy="0.3" r="0.6"><stop offset="0" stop-color="#FF9A3C" stop-opacity="0.55"/><stop offset="0.5" stop-color="#F27D0D" stop-opacity="0.18"/><stop offset="1" stop-color="#F27D0D" stop-opacity="0"/></radialGradient>
  <radialGradient id="screenglow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#3B82F6" stop-opacity="0.35"/><stop offset="1" stop-color="#3B82F6" stop-opacity="0"/></radialGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A3A1A"/><stop offset="1" stop-color="#3F2A14"/></linearGradient>
  <clipPath id="win"><rect x="60" y="34" width="360" height="176" rx="8"/></clipPath>
  <clipPath id="scr"><rect x="512" y="126" width="196" height="118" rx="4"/></clipPath>
  <filter id="blur"><feGaussianBlur stdDeviation="6"/></filter>
</defs>''')
# room
a(f'<rect width="{W}" height="{H}" fill="url(#room)"/>')
# lamp glow
a('<ellipse cx="840" cy="170" rx="230" ry="170" fill="url(#lamp)"><animate attributeName="opacity" values="0.85;1;0.9;1;0.85" dur="6s" repeatCount="indefinite"/></ellipse>')
# window
a('<rect x="54" y="28" width="372" height="188" rx="12" fill="#1F2937"/>')
a('<g clip-path="url(#win)">')
a('<rect x="60" y="34" width="360" height="176" fill="url(#sky)"/>')
for i in range(26):
    x = random.randint(66, 414); y = random.randint(40, 120); r = random.choice([1, 1, 1.4, 1.8]); d = random.uniform(1.8, 4.5); b = random.uniform(0, 3)
    a(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#E0F2FE"><animate attributeName="opacity" values="0.25;1;0.25" dur="{d:.1f}s" begin="{b:.1f}s" repeatCount="indefinite"/></circle>')
a('<circle cx="356" cy="72" r="20" fill="#FDE68A" opacity="0.95"/><circle cx="366" cy="64" r="17" fill="#172554" opacity="0.92"/>')
sky = [(60,150,22),(82,138,30),(112,158,18),(130,128,36),(166,146,26),(192,120,40),(232,140,24),(256,132,34),(290,152,20),(310,124,44),(354,144,28),(382,136,38)]
for x, y, w in sky:
    a(f'<rect x="{x}" y="{y}" width="{w}" height="{210-y}" fill="#0B1220"/>')
    for wy in range(y+8, 204, 10):
        for wx in range(x+4, x+w-4, 8):
            if random.random() < 0.35:
                d = random.uniform(3, 9); b = random.uniform(0, 6)
                a(f'<rect x="{wx}" y="{wy}" width="3" height="4" fill="#FBBF24" opacity="0.7"><animate attributeName="opacity" values="0.7;0.15;0.7" dur="{d:.1f}s" begin="{b:.1f}s" repeatCount="indefinite"/></rect>')
for i in range(70):
    x = random.randint(60, 420); y = random.randint(-60, 200); L = random.randint(10, 18); d = random.uniform(0.7, 1.3); b = random.uniform(0, 1.3)
    a(f'<line x1="{x}" y1="{y}" x2="{x-3}" y2="{y+L}" stroke="#93C5FD" stroke-opacity="0.45" stroke-width="1.2" stroke-linecap="round"><animateTransform attributeName="transform" type="translate" from="0 0" to="-40 220" dur="{d:.2f}s" begin="-{b:.2f}s" repeatCount="indefinite"/></line>')
a('</g>')
a('<rect x="238" y="34" width="4" height="176" fill="#1F2937"/><rect x="60" y="120" width="360" height="4" fill="#1F2937"/>')
a('<rect x="46" y="214" width="388" height="10" rx="3" fill="#374151"/>')
# plant
a('<rect x="90" y="196" width="26" height="22" rx="3" fill="#431407"/>')
for cx, cy, r in [(96,190,9),(110,186,10),(103,178,8),(118,194,7),(88,200,6)]:
    a(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#22C55E" opacity="0.9"><animateTransform attributeName="transform" type="rotate" values="-2 103 200;2 103 200;-2 103 200" dur="5s" repeatCount="indefinite"/></circle>')
# desk
a(f'<rect x="0" y="252" width="{W}" height="30" fill="url(#wood)"/><rect x="0" y="252" width="{W}" height="3" fill="#7C4A1E" opacity="0.7"/>')
a(f'<rect x="0" y="282" width="{W}" height="{H-282}" fill="#0B1220"/>')
a('<ellipse cx="610" cy="256" rx="150" ry="26" fill="url(#screenglow)"/>')
# laptop
a('<rect x="504" y="118" width="212" height="134" rx="8" fill="#374151"/>')
a('<rect x="512" y="126" width="196" height="118" rx="4" fill="#0D1117"/>')
a('<g clip-path="url(#scr)">')
a('<rect x="512" y="126" width="196" height="14" fill="#161B22"/><circle cx="521" cy="133" r="2.5" fill="#F27D0D"/><circle cx="529" cy="133" r="2.5" fill="#FBBF24"/><circle cx="537" cy="133" r="2.5" fill="#22C55E"/>')
a('<text x="524" y="156" font-size="8" fill="#9CA3AF" >which markets actually make money?</text>')
bars = [18, 30, 22, 40, 34, 52, 44]
for i, h in enumerate(bars):
    x = 524 + i*10
    a(f'<rect x="{x}" y="{232-h}" width="6" height="{h}" rx="1" fill="#1D4ED8"><animate attributeName="height" values="{h};{h*0.6:.0f};{h}" dur="{2.4+i*0.3:.1f}s" repeatCount="indefinite"/><animate attributeName="y" values="{232-h};{232-h*0.6:.0f};{232-h}" dur="{2.4+i*0.3:.1f}s" repeatCount="indefinite"/></rect>')
a('<polyline points="606,226 620,214 634,220 648,200 662,206 676,186 690,190 700,176" fill="none" stroke="#3B82F6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="160" stroke-dashoffset="160"><animate attributeName="stroke-dashoffset" values="160;0;0;160" keyTimes="0;0.5;0.85;1" dur="6s" repeatCount="indefinite"/></polyline>')
a('<circle cx="700" cy="176" r="3" fill="#F27D0D"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.45;0.55;0.85;1" dur="6s" repeatCount="indefinite"/></circle>')
a('<rect x="612" y="234" width="5" height="7" fill="#93C5FD"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
a('</g>')
a('<path d="M480 252 L740 252 L730 262 Q610 266 490 262 Z" fill="#4B5563"/>')
# mug + steam
a('<rect x="780" y="214" width="34" height="38" rx="5" fill="#E5E7EB"/><path d="M814 224 q16 0 16 12 q0 12 -16 12" fill="none" stroke="#E5E7EB" stroke-width="5"/><rect x="784" y="222" width="26" height="4" fill="#3F2A14" opacity="0.8"/>')
for i, x in enumerate([789, 797, 805]):
    a(f'<path d="M{x} 208 q-4 -6 0 -12 q4 -6 0 -12" fill="none" stroke="#E5E7EB" stroke-width="2" stroke-linecap="round" opacity="0"><animate attributeName="opacity" values="0;0.7;0" dur="2.6s" begin="{i*0.6:.1f}s" repeatCount="indefinite"/><animateTransform attributeName="transform" type="translate" from="0 6" to="0 -14" dur="2.6s" begin="{i*0.6:.1f}s" repeatCount="indefinite"/></path>')
# lamp
a('<rect x="906" y="150" width="6" height="102" fill="#374151"/><rect x="884" y="246" width="50" height="8" rx="3" fill="#374151"/>')
a('<path d="M872 152 L946 152 L932 122 L886 122 Z" fill="#F27D0D"/><ellipse cx="909" cy="152" rx="37" ry="5" fill="#FF9A3C"/>')
a('<ellipse cx="909" cy="180" rx="60" ry="26" fill="#FF9A3C" opacity="0.18" filter="url(#blur)"><animate attributeName="opacity" values="0.14;0.24;0.14" dur="4s" repeatCount="indefinite"/></ellipse>')
# headphones + notes
a('<path d="M732 250 q0 -22 22 -22 q22 0 22 22" fill="none" stroke="#9CA3AF" stroke-width="4"/><rect x="726" y="240" width="10" height="14" rx="3" fill="#F27D0D"/><rect x="772" y="240" width="10" height="14" rx="3" fill="#F27D0D"/>')
for i, (x, y) in enumerate([(760,224),(772,232),(748,230)]):
    a(f'<text x="{x}" y="{y}" font-size="12" fill="#93C5FD" opacity="0"><animate attributeName="opacity" values="0;0.9;0" dur="3s" begin="{i*1.0:.1f}s" repeatCount="indefinite"/><animateTransform attributeName="transform" type="translate" from="0 0" to="{-6+i*6} -34" dur="3s" begin="{i*1.0:.1f}s" repeatCount="indefinite"/>&#9834;</text>')
# cat
a('<g><ellipse cx="300" cy="240" rx="34" ry="14" fill="#F27D0D"/><circle cx="332" cy="230" r="13" fill="#F27D0D"/><path d="M322 220 l2 -10 l8 7 Z M342 220 l-2 -10 l-8 7 Z" fill="#F27D0D"/><path d="M325 231 q4 3 8 0 M336 231 q4 3 8 0" fill="none" stroke="#431407" stroke-width="1.6" stroke-linecap="round"/><circle cx="333" cy="236" r="1.2" fill="#431407"/>')
a('<path d="M268 244 q-20 -4 -22 -22" fill="none" stroke="#F27D0D" stroke-width="6" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" values="0 268 244;14 268 244;0 268 244" dur="3.2s" repeatCount="indefinite"/></path></g>')
a('<text x="300" y="214" font-size="10" fill="#9CA3AF" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0" keyTimes="0;0.5;0.7;1" dur="4s" repeatCount="indefinite"/>z</text><text x="310" y="204" font-size="12" fill="#9CA3AF" opacity="0"><animate attributeName="opacity" values="0;0;0.9;0" keyTimes="0;0.55;0.8;1" dur="4s" repeatCount="indefinite"/>z</text>')
# text (name, title and slogan match alyssatramnia.com)
a('<text x="500" y="52" font-size="30" font-weight="700" fill="#F9FAFB">Alyssa Tram Anh H.</text>')
a('<text x="500" y="74" font-size="14" font-weight="600" fill="#F27D0D" letter-spacing="1">DATA &amp; INSIGHTS ANALYST</text>')
a('<text x="500" y="94" font-size="12" fill="#93C5FD">I help teams uncover the story behind their data</text>')
a('<text x="500" y="111" font-size="12" fill="#93C5FD">and turn it into action.</text>')
a('</svg>')
svg = '\n'.join(out)
open(sys.argv[1], 'w', encoding='utf-8', newline='\n').write(svg)
print("bytes:", len(svg))
