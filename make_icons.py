#!/usr/bin/env python3
import os

os.makedirs('icons', exist_ok=True)

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192">
  <rect width="192" height="192" fill="#0f0e0d" rx="32"/>
  <text x="96" y="72" font-family="serif" font-weight="bold" font-size="48" fill="#e8a230" text-anchor="middle">OV</text>
  <rect x="32" y="90" width="128" height="6" rx="3" fill="#e8a230" opacity="0.6"/>
  <rect x="40" y="108" width="112" height="8" rx="4" fill="#3a3835"/>
  <rect x="40" y="122" width="112" height="8" rx="4" fill="#3a3835"/>
  <rect x="40" y="136" width="80" height="8" rx="4" fill="#3a3835"/>
  <rect x="32" y="106" width="6" height="42" rx="3" fill="#e8a230"/>
</svg>'''

with open('icons/icon-192.svg', 'w') as f:
    f.write(svg)

# Write a minimal placeholder PNG using base64-encoded 1x1 pixel scaled up
# For real deployment, replace icons/icon-192.png and icons/icon-512.png
# with proper PNG files generated from the SVG above.
print("SVG icon written to icons/icon-192.svg")
print("For deployment, convert to PNG using: inkscape icon-192.svg -w 192 -h 192 -o icon-192.png")
print("Or use any online SVG-to-PNG converter.")
