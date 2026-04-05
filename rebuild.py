import re

with open('index.html') as f:
    c = f.read()

# Add button
c = c.replace(
    '<button class="tab-btn" onclick="showTab(5)">📊 Appraisal Model</button>',
    '<button class="tab-btn" onclick="showTab(5)">📊 Appraisal Model</button>\n  <button class="tab-btn" onclick="showTab(6)">🏠 Home Appraisal</button>'
)

# Build tab-6 HTML (using unicode for ' and " to be safe, HTML entities for & and <, etc.)
tab6 = '''
<!-- HOME APPRAISAL TAB -->
<div class="tab-content" id="tab-6">
<div style="padding:24px;">

  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
    <div>
      <div style="font-size:1.2rem;font-weight:800;color:var(--text);">6705 Briarcroft St, Clifton VA 20124</div>
      <div style="font-size:0.82rem;color:var(--muted);margin-top:4px;">Primary Residence &middot; HELOC Assessment &middot; Full Custom Rebuild 2022 &middot; C2 Condition</div>
    </div>
    <div style="text-align:center;background:rgba(79,142,247,0.1);border:2px solid var(--accent);border-radius:10px;padding:14px 28px;">
      <div style="font-size:1.8rem;font-weight:900;color:var(--accent);">$2,700,000</div>
      <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;margin-top:2px;">Point Estimate</div>
      <div style="font-size:0.72rem;color:var(--muted);">Range: $2.60M &ndash; $2.85M</div>
    </div>
  </div>

  <div class="alert alert-blue" style="margin-bottom:20px;line-height:1.7;">
    <strong>Opinion of Value &mdash; April 2026.</strong> Sales Comparison Approach (primary) + Cost Approach (secondary). The 2022 full custom rebuild makes this effectively new construction. All public data (Zillow, Redfin, Fairfax County) reflects the <em>prior</em> structure &mdash; the prior $850K sale is not a valid comparable and must be excluded.
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Property Details</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Address</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">6705 Briarcroft St, Clifton VA 20124</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Total Finished Area</td><td style="padding:7px 0;font-weight:700;color:var(--accent);text-align:right;border-bottom:1px solid var(--border);">5,900 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Above Grade GLA</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">3,900 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Below Grade Finished</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">2,000 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Bedrooms</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">9 total (6 AG / 3 BG)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Bathrooms</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">5 full</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">In-Law Suite</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Yes &mdash; full kitchen</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">Lot Size</td><td style="padding:7px 0;font-weight:600;text-align:right;">&sim;5 acres, Clifton VA</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Construction &amp; Condition</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Year Built</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">2022 (full custom rebuild)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Age</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">~4 years</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Construction Quality</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Q1&ndash;Q2 (Custom Luxury)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Condition Rating</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">C2 &mdash; Excellent</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Depreciation</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Minimal (~2&ndash;3%)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Custom Glass</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Large expanses &mdash; est. +$100&ndash;150K</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">In-Law Suite Premium</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;">Est. +$40&ndash;60K value</td></tr>
      </table>
    </div>
  </div>

  <div class="card" style="margin-bottom:20px;">
    <div class="card-title">Sales Comparison Approach</div>
    <div style="overflow-x:auto;">
    <table>
      <thead><tr><th>Property</th><th>Sale Price</th><th>GLA</th><th>$/sqft</th><th>Condition</th><th>Adjusted Value</th></tr></thead>
      <tbody>
        <tr class="row-blue"><td><strong>SUBJECT: 6705 Briarcroft</strong></td><td class="col-blue fw-bold">Est. $2,700,000</td><td>3,900 AG / 2,000 BG</td><td>~$460 AG</td><td><span class="badge badge-green">C2</span></td><td>&mdash;</td></tr>
        <tr><td>6501 Clifton Rd, Clifton VA</td><td>$2,500,000</td><td>6,488 sqft</td><td>$385</td><td>C3</td><td class="col-green fw-bold">$2,650&ndash;2,700K</td></tr>
        <tr class="row-gold"><td>6500 Briarcroft St, Clifton VA</td><td>$2,999,900</td><td>13,850 sqft</td><td>$217</td><td>C2&ndash;C3</td><td class="col-green fw-bold">$2,500&ndash;2,800K</td></tr>
        <tr><td>Clifton Luxury Market (Active)</td><td>$2.4M&ndash;$4.75M</td><td>5,000&ndash;16,600</td><td>$280&ndash;$450+</td><td>C2&ndash;C3</td><td class="col-green fw-bold">$2,600&ndash;2,850K</td></tr>
      </tbody>
    </table>
    </div>
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Cost Approach</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Above Grade: 3,900 sqft @ $460/sqft</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$1,794,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Below Grade: 2,000 sqft @ $200/sqft</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$400,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Custom Glass + In-Law Premium</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">+$175,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Depreciation (~2.5%)</td><td style="padding:7px 0;color:var(--red);text-align:right;border-bottom:1px solid var(--border);">&minus;$59,225</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Land Value (~5 acres)</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">+$350,000&ndash;$500,000</td></tr>
        <tr><td style="padding:7px 0;font-weight:700;">Cost Approach Indicated Value</td><td style="padding:7px 0;font-weight:800;color:var(--green);text-align:right;">$2,660,000&ndash;$2,810,000</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">HELOC Capacity</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Estimated Market Value</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">$2,700,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">80% LTV Max Loan Basis</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$,160,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">85% LTV Max Loan Basis</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$,295,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Less First Mortgage Balance</td><td style="padding:7px 0;color:var(--gold);text-align:right;border-bottom:1px solid var(--border);">Subtract existing balance</td></tr>
        <tr><td style="padding:7px 0;font-weight:700;">Estimated Available HELOC</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;">Likely $500K&ndash;$1M+</td></tr>
      </table>
    </div>
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Reconciliation</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Sales Comparison (70% weight)</td><td style="padding:7px 0;color:var(--green);font-weight:600;text-align:right;border-bottom:1px solid var(--border);">$2,650,000&ndash;$2,750,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Cost Approach (30% weight)</td><td style="padding:7px 0;color:var(--green);font-weight:600;text-align:right;border-bottom:1px solid var(--border);">$,660,000&ndash;$2,810,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Conservative Floor</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$,600,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Optimistic Ceiling</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$,850,000</td></tr>
        <tr><td style="padding:7px 0;font-weight:700;">Point Estimate</td><td style="padding:7px 0;font-weight:900;color:var(--accent);text-align:right;font-size:1rem;">$2,700,000</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Market Context &mdash; Fairfax County / 20124</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Median Sale Price (20124)</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$880,860 (Feb 2026)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">YoY Trend (20124)</td><td style="padding:7px 0;color:var(--red);font-weight:600;text-align:right;border-bottom:1px solid var(--border);">&minus;5.9%</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Fairfax Co. Avg PSF</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$,374 (Nov 2024)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">Fairfax Co. Assessment Increase</td><td style="padding:7px 0;color:var(--green);font-weight:600;text-align:right;">+6.65% (2025)</td></tr>
      </table>
    </div>
  </div>

  <div class="alert alert-gold" style="line-height:1.8;">
    <strong>Critical Notes for HELOC Appraisal</strong><br><br>
    <strong>1. Brief the appraiser before they pull public records.</strong> Zillow, Redfin, and county records show the prior structure. Provide contractor invoices from 2022, current photos, and Fairfax County permit records.<br><br>
    <strong>2. The prior $850K sale is a comp trap.</strong> Reflects the old structure &mdash; must be excluded entirely.<br><br>
    <strong>3. Document C2 condition.</strong> Photos of finishes and custom glass justify the quality rating.<br><br>
    <strong>4. In-law suite documentation.</strong> Confirm permits and egress so the 2,000 BG sqft counts toward finished GLA.<br><br>
    <strong>5. HELOC math:</strong> At $2.7M value, 80% LTV = $2.16M loan basis. Subtract outstanding first mortgage to get available HELOC line.
  </div>

</div>
</div>
'''

# Insert tab-6 content before </body>
c = c.replace('</body>', tab6 + '\n</body>')

with open('index.html', 'w') as f:
    f.write(c)

# Validate the new file
c2 = ""
with open('index.html') as f:
    c2 = f.read()

# Check for unescaped apostrophes in JS strings (should be none in the original script)
script_start = c2.find('<script>')
script_end = c2.rfind('</script>')
script_content = c2[script_start:script_end]
js_errors = []
for i, line in enumerate(script_content.split('\n')):
    if line.count("'") % 2 != 0:
        js_errors.append(f'JS line {i+1}: {line.strip()[:100]}')

# Check div balance
div_opens = c2.count('<div')
div_closes = c2.count('</div>')

print(f"JS errors (should be 0): {len(js_errors)}")
print(f"Div balance (should be 1 from baseline): {div_opens - div_closes}")
print(f"Tab-6 content check: {'<div class="tab-content" id="tab-6">' in c2}")
