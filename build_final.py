with open('index_clean.html') as f:
    c = f.read()

# Add the Home Appraisal button to the tab bar
c = c.replace(
    '<button class="tab-btn" onclick="showTab(5)">📊 Appraisal Model</button>',
    '<button class="tab-btn" onclick="showTab(5)">📊 Appraisal Model</button>\n  <button class="tab-btn" onclick="showTab(6)">🏠 Home Appraisal</button>'
)

# Build the appraisal tab HTML - uses only classes confirmed to exist in this file
tab6 = '''
<!-- ===== TAB 7: HOME APPRAISAL ===== -->
<div class="tab-content" id="tab-6">
<div style="padding:0 24px 40px;">

  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
    <div>
      <div style="font-size:1.2rem;font-weight:800;color:var(--text);">6705 Briarcroft St, Clifton VA 20124</div>
      <div style="font-size:0.82rem;color:var(--muted);margin-top:4px;">Primary Residence · HELOC Assessment · Full Custom Rebuild 2022 · C2 Condition</div>
    </div>
    <div style="text-align:center;background:rgba(79,142,247,0.1);border:2px solid var(--accent);border-radius:10px;padding:14px 28px;">
      <div style="font-size:1.8rem;font-weight:900;color:var(--accent);">$2,700,000</div>
      <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;margin-top:2px;">Point Estimate</div>
      <div style="font-size:0.72rem;color:var(--muted);">Range: $2.60M – $2.85M</div>
    </div>
  </div>

  <div class="alert alert-blue" style="margin-bottom:20px;line-height:1.7;">
    <strong>Opinion of Value — April 2026.</strong> Sales Comparison Approach (primary) + Cost Approach (secondary). The 2022 full custom rebuild makes this effectively new construction. All public data (Zillow, Redfin, Fairfax County) reflects the <em>prior</em> structure — the prior $850K / 3,902 sqft sale is not a valid comparable and must be excluded.
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Property Details</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Address</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">6705 Briarcroft St, Clifton VA 20124</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">County</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">Fairfax County, VA</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Total Finished Area</td><td style="padding:7px 0;font-weight:700;color:var(--accent);text-align:right;border-bottom:1px solid var(--border);">5,900 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Above Grade GLA</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">3,900 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Below Grade Finished</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">2,000 sqft</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Bedrooms</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">9 total (6 AG / 3 BG)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Bathrooms</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">5 full (3 AG / 2 BG)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">In-Law Suite</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Yes — full kitchen, half-below grade</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Lot Size (est.)</td><td style="padding:7px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">~5 acres</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">Zoning</td><td style="padding:7px 0;font-weight:600;text-align:right;">RC — Rural Cluster / Residential</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Construction &amp; Condition</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Year Built</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">2022 (full custom rebuild)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Age</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">~4 years</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Construction Quality</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Q1–Q2 (Custom / Luxury)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Condition Rating</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">C2 — Excellent</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Depreciation</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Minimal (~2–3%)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Custom Glass</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Large expanses — est. +$100–150K</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Luxury Finishes</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Throughout — Q1 materials</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">In-Law Suite Premium</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;">Est. +$40–60K value</td></tr>
      </table>
    </div>
  </div>

  <div class="card" style="margin-bottom:20px;">
    <div class="card-title">Sales Comparison Approach — Comparable Sales</div>
    <div style="overflow-x:auto;">
    <table>
      <thead>
        <tr>
          <th>Property</th><th>Sale Price</th><th>GLA</th><th>$/sqft</th><th>Yr Built</th><th>Condition</th><th>Adjustment</th><th>Adj. Value</th>
        </tr>
      </thead>
      <tbody>
        <tr class="row-blue">
          <td><strong>SUBJECT: 6705 Briarcroft St</strong></td>
          <td class="col-blue fw-bold">Est. $2,700,000</td>
          <td>3,900 AG / 2,000 BG</td>
          <td>~$460 AG</td>
          <td>2022 rebuild</td>
          <td><span class="badge badge-green">C2</span></td>
          <td>—</td><td>—</td>
        </tr>
        <tr>
          <td>6501 Clifton Rd, Clifton VA</td>
          <td>$2,500,000</td><td>6,488 sqft</td><td>$385</td><td>1997</td><td>C3 (est.)</td>
          <td class="col-green">+$150–200K: newer, C2 vs C3, custom finishes</td>
          <td class="col-green fw-bold">$2,650–2,700K</td>
        </tr>
        <tr class="row-gold">
          <td>6500 Briarcroft St, Clifton VA</td>
          <td>$2,999,900</td><td>13,850 sqft</td><td>$217</td><td>2010</td><td>C2–C3</td>
          <td class="col-gold">Adj. down for size — validates $2.5M+ floor</td>
          <td class="col-green fw-bold">$2,500–2,800K</td>
        </tr>
        <tr>
          <td>Clifton / Fairfax Co. Luxury (Active)</td>
          <td>$2.4M–$4.75M</td><td>5,000–16,600</td><td>$280–$450+</td><td>Varies</td><td>C2–C3</td>
          <td class="col-blue">Subject falls mid-range of active luxury inventory</td>
          <td class="col-green fw-bold">$2,600–2,850K</td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Cost Approach — Replacement Cost New</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Above Grade: 3,900 sqft @ $460/sqft</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$1,794,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Below Grade: 2,000 sqft @ $200/sqft</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$400,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Custom Glass + In-Law Suite Premium</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">+$175,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Depreciation (~2.5%)</td><td style="padding:7px 0;color:var(--red);text-align:right;border-bottom:1px solid var(--border);">−$59,225</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Land Value (~5 acres, Clifton)</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">+$350,000–$500,000</td></tr>
        <tr><td style="padding:7px 0;font-weight:700;color:var(--text);">Cost Approach Indicated Value</td><td style="padding:7px 0;font-weight:800;color:var(--green);text-align:right;">$2,660,000–$2,810,000</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">HELOC Borrowing Capacity</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Estimated Market Value</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">$2,700,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Max Loan Basis @ 80% LTV</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$2,160,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Max Loan Basis @ 85% LTV</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$2,295,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Less First Mortgage Balance</td><td style="padding:7px 0;color:var(--gold);text-align:right;border-bottom:1px solid var(--border);">Subtract existing balance</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Estimated Available HELOC</td><td style="padding:7px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Likely $500K–$1M+ depending on balance</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">Lender Requirement</td><td style="padding:7px 0;color:var(--red);font-weight:600;text-align:right;">Licensed URAR appraisal required</td></tr>
      </table>
    </div>
  </div>

  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Reconciliation</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Sales Comparison (70% weight)</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">$2,650,000–$2,750,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Cost Approach (30% weight)</td><td style="padding:7px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">$2,660,000–$2,810,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Conservative Floor</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$2,600,000</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Optimistic Ceiling</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$2,850,000</td></tr>
        <tr><td style="padding:7px 0;font-weight:700;color:var(--text);">Point Estimate</td><td style="padding:7px 0;font-weight:900;color:var(--accent);text-align:right;font-size:1rem;">$2,700,000</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Market Context — Fairfax County / 20124</div>
      <table style="width:100%;font-size:0.82rem;border-collapse:collapse;">
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Median Sale Price (20124, all types)</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$880,860 (Redfin Feb 2026)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">YoY Trend (20124)</td><td style="padding:7px 0;color:var(--red);font-weight:600;text-align:right;border-bottom:1px solid var(--border);">−5.9% (broad softening)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Fairfax Co. Avg PSF (all homes)</td><td style="padding:7px 0;text-align:right;border-bottom:1px solid var(--border);">$374 (Nov 2024)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);border-bottom:1px solid var(--border);">Fairfax Co. Assessment Increase</td><td style="padding:7px 0;color:var(--green);font-weight:600;text-align:right;border-bottom:1px solid var(--border);">+6.65% (2025 cycle)</td></tr>
        <tr><td style="padding:7px 0;color:var(--muted);">Luxury Active Listings (20124)</td><td style="padding:7px 0;text-align:right;">14 listings; 28 avg DOM</td></tr>
      </table>
    </div>
  </div>

  <div class="alert alert-gold" style="line-height:1.8;">
    <strong>⚠️ Critical Notes for HELOC Appraisal</strong><br><br>
    <strong>1. Brief the appraiser before they pull public records.</strong> Zillow, Redfin, and county records show the prior structure. Provide contractor scope/invoices from 2022, current photos, and Fairfax County permit records. If appraiser anchors on the prior $850K sale, they will massively undervalue.<br><br>
    <strong>2. The prior $850K sale is a comp trap.</strong> Reflects the old structure — must be excluded entirely.<br><br>
    <strong>3. Document C2 condition.</strong> Prior appraisal docs + photos of finishes and custom glass justify the quality rating.<br><br>
    <strong>4. In-law suite documentation.</strong> Confirm permits and egress so the 2,000 BG sqft counts toward finished GLA.<br><br>
    <strong>5. HELOC math:</strong> At $2.7M value, 80% LTV = $2.16M loan basis. Subtract outstanding first mortgage balance to get your available HELOC line.
  </div>

</div>
</div>
'''

# Insert tab-6 right before </body>
c = c.replace('</body>', tab6 + '\n</body>')

with open('index.html', 'w') as f:
    f.write(c)

import re
depth = sum(-1 if m.group(1) else 1 for m in re.finditer(r'<(/?)div', c))
tabs = re.findall(r'class="tab-content[^"]*" id="tab-(\d+)"', c)
btns = re.findall(r'onclick="showTab\((\d+)\)"', c)
print(f'Div balance: {depth} (must be 0)')
print(f'Tabs: {tabs}')
print(f'Buttons: {btns}')
print(f'Counts match: {len(tabs) == len(btns)}')
