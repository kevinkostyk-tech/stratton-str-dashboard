with open('index.html', 'r') as f:
    content = f.read()

# Remove everything from the old tab-6 div
start = content.find('<!-- ===== TAB 7: HOME APPRAISAL ===== -->')
end = content.find('</body>')

if start == -1:
    print("ERROR: tab-6 start not found")
    exit(1)

appraisal_html = '''<!-- ===== TAB 7: HOME APPRAISAL ===== -->
<div class="tab-content" id="tab-6">
<div style="max-width:1100px;margin:0 auto;">

  <!-- Header -->
  <div style="background:var(--card);border:1px solid var(--border);border-radius:12px;padding:24px;margin-bottom:20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
    <div>
      <div style="font-size:1.2rem;font-weight:800;color:var(--text);">6705 Briarcroft St, Clifton VA 20124</div>
      <div style="font-size:0.82rem;color:var(--muted);margin-top:4px;">Primary Residence · URAR-Methodology HELOC Assessment · Full Custom Rebuild 2022 · C2 Condition</div>
    </div>
    <div style="text-align:center;background:rgba(79,142,247,0.1);border:1px solid var(--accent);border-radius:10px;padding:14px 24px;">
      <div style="font-size:1.8rem;font-weight:900;color:var(--accent);">$2,700,000</div>
      <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;margin-top:2px;">Estimated Market Value</div>
      <div style="font-size:0.72rem;color:var(--muted);margin-top:2px;">Range: $2.60M – $2.85M</div>
    </div>
  </div>

  <!-- Opinion of Value -->
  <div class="alert alert-blue" style="margin-bottom:20px;line-height:1.7;">
    <strong>Opinion of Value — April 2026</strong><br>
    Point estimate <strong>$2,700,000</strong> (range $2.60M–$2.85M). Primary method: Sales Comparison Approach, supported by Cost Approach cross-check for luxury new construction in Fairfax County. The 2022 full custom rebuild makes this effectively new construction for appraisal purposes. All existing public data (Zillow, Redfin, Fairfax County records) reflects the <em>prior</em> structure — the prior $850K / 3,902 sqft sale is not a valid comparable. True comps are large custom luxury homes in the Clifton / Fairfax County estate market.
  </div>

  <!-- Property Details Grid -->
  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Property Identification</div>
      <table style="width:100%;font-size:0.82rem;">
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Address</td><td style="padding:6px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">6705 Briarcroft St, Clifton VA 20124</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">County</td><td style="padding:6px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">Fairfax County, VA</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Lot Size (Est.)</td><td style="padding:6px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">~5 acres</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Zoning (Est.)</td><td style="padding:6px 0;font-weight:600;text-align:right;border-bottom:1px solid var(--border);">RC — Rural Cluster / Residential</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);">Neighborhood</td><td style="padding:6px 0;font-weight:600;text-align:right;">Clifton / Briarcroft</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">Construction &amp; Condition</div>
      <table style="width:100%;font-size:0.82rem;">
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Year Built</td><td style="padding:6px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">2022 (full custom rebuild)</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Effective Age</td><td style="padding:6px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">~4 years</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Construction Quality</td><td style="padding:6px 0;font-weight:600;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Q1–Q2 (Custom / Luxury)</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Condition Rating</td><td style="padding:6px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">C2 — Excellent (near-new)</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);">Depreciation</td><td style="padding:6px 0;font-weight:600;color:var(--green);text-align:right;">Minimal — ~2–3%</td></tr>
      </table>
    </div>
  </div>

  <!-- Room Count Grid -->
  <div class="grid-4" style="margin-bottom:20px;">
    <div class="stat-box">
      <div class="stat-label">Total Finished Area</div>
      <div class="stat-val col-blue">5,900 sqft</div>
      <div class="stat-sub">3,900 AG + 2,000 BG</div>
    </div>
    <div class="stat-box">
      <div class="stat-label">Bedrooms</div>
      <div class="stat-val col-green">9 Total</div>
      <div class="stat-sub">6 above / 3 below grade</div>
    </div>
    <div class="stat-box">
      <div class="stat-label">Bathrooms</div>
      <div class="stat-val col-green">5 Full</div>
      <div class="stat-sub">3 above / 2 below grade</div>
    </div>
    <div class="stat-box">
      <div class="stat-label">In-Law Suite</div>
      <div class="stat-val col-green">Full</div>
      <div class="stat-sub">Separate kitchen, half-below grade</div>
    </div>
  </div>

  <!-- Special Features -->
  <div class="card" style="margin-bottom:20px;">
    <div class="card-title">Special Features &amp; Value Drivers</div>
    <div class="grid-4">
      <div style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;padding:12px;text-align:center;">
        <div style="font-size:1.4rem;margin-bottom:4px;">🪟</div>
        <div style="font-weight:700;color:var(--text);font-size:0.82rem;">Custom Glass</div>
        <div style="font-size:0.7rem;color:var(--muted);margin-top:4px;">Large expanses throughout · est. +$100–150K premium</div>
      </div>
      <div style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;padding:12px;text-align:center;">
        <div style="font-size:1.4rem;margin-bottom:4px;">✨</div>
        <div style="font-weight:700;color:var(--text);font-size:0.82rem;">Luxury Finishes</div>
        <div style="font-size:0.7rem;color:var(--muted);margin-top:4px;">Throughout — Q1 quality materials and workmanship</div>
      </div>
      <div style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;padding:12px;text-align:center;">
        <div style="font-size:1.4rem;margin-bottom:4px;">🏠</div>
        <div style="font-weight:700;color:var(--text);font-size:0.82rem;">In-Law Suite</div>
        <div style="font-size:0.7rem;color:var(--muted);margin-top:4px;">Full kitchen · est. +$40–60K value · half-below grade</div>
      </div>
      <div style="background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;padding:12px;text-align:center;">
        <div style="font-size:1.4rem;margin-bottom:4px;">🌲</div>
        <div style="font-weight:700;color:var(--text);font-size:0.82rem;">~5 Acre Lot</div>
        <div style="font-size:0.7rem;color:var(--muted);margin-top:4px;">Private, wooded setting · Clifton land premium</div>
      </div>
    </div>
  </div>

  <!-- Comps Table -->
  <div class="card" style="margin-bottom:20px;">
    <div class="card-title">Sales Comparison Approach — Comparable Sales Grid</div>
    <div style="overflow-x:auto;">
    <table>
      <thead>
        <tr>
          <th>Property</th>
          <th>Sale Price</th>
          <th>GLA (sqft)</th>
          <th>$/sqft</th>
          <th>Yr Built</th>
          <th>Condition</th>
          <th>Adjustment to Subject</th>
          <th>Adj. Value</th>
        </tr>
      </thead>
      <tbody>
        <tr class="row-blue">
          <td><strong>Subject: 6705 Briarcroft St</strong></td>
          <td class="col-blue fw-bold">Est. $2,700,000</td>
          <td>3,900 AG / 2,000 BG</td>
          <td>~$460 (AG)</td>
          <td>2022 rebuild</td>
          <td><span class="badge badge-green">C2</span></td>
          <td>—</td>
          <td>—</td>
        </tr>
        <tr>
          <td>Comp 1: 6501 Clifton Rd</td>
          <td>$2,500,000</td>
          <td>6,488</td>
          <td>$385</td>
          <td>1997</td>
          <td>C3 (est.)</td>
          <td class="col-green">+$150–200K: newer age, C2 vs C3, custom finishes</td>
          <td class="col-green fw-bold">$2,650–2,700K</td>
        </tr>
        <tr class="row-gold">
          <td>Comp 2: 6500 Briarcroft St</td>
          <td>$2,999,900</td>
          <td>13,850</td>
          <td>$217</td>
          <td>2010</td>
          <td>C2–C3</td>
          <td class="col-gold">Adj. down for size — still validates $2.5M+ floor</td>
          <td class="col-green fw-bold">$2,500–2,800K</td>
        </tr>
        <tr>
          <td>Comp 3: Clifton / Fairfax Co. Luxury (Active)</td>
          <td>$2.4M–$4.75M</td>
          <td>5,000–16,600</td>
          <td>$280–$450+</td>
          <td>Varies</td>
          <td>C2–C3</td>
          <td class="col-blue">Subject falls mid-range of active luxury inventory</td>
          <td class="col-green fw-bold">$2,600–2,850K</td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>

  <!-- Cost Approach + HELOC -->
  <div class="grid-2" style="margin-bottom:20px;">
    <div class="card">
      <div class="card-title">Cost Approach — Replacement Cost New</div>
      <table style="width:100%;font-size:0.82rem;">
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Above Grade: 3,900 sqft @ $460/sqft</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">$1,794,000</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Below Grade: 2,000 sqft @ $200/sqft</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">$400,000</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Custom Glass Premium</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">+$125,000</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">In-Law Suite Premium</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">+$50,000</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Depreciation (~2.5%)</td><td style="padding:6px 0;text-align:right;color:var(--red);border-bottom:1px solid var(--border);">−$59,225</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Land Value (~5 acres, Clifton)</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">+$350,000–$500,000</td></tr>
        <tr><td style="padding:6px 0;font-weight:700;color:var(--text);">Cost Approach Indicated Value</td><td style="padding:6px 0;font-weight:800;color:var(--green);text-align:right;">$2,660,000–$2,810,000</td></tr>
      </table>
    </div>
    <div class="card">
      <div class="card-title">HELOC Borrowing Capacity</div>
      <table style="width:100%;font-size:0.82rem;">
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Estimated Market Value</td><td style="padding:6px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">$2,700,000</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">HELOC LTV @ 80%</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">$2,160,000 max basis</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">HELOC LTV @ 85%</td><td style="padding:6px 0;text-align:right;border-bottom:1px solid var(--border);">$2,295,000 max basis</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Less First Mortgage Balance</td><td style="padding:6px 0;color:var(--gold);text-align:right;border-bottom:1px solid var(--border);">Subtract existing balance</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);border-bottom:1px solid var(--border);">Available HELOC (est.)</td><td style="padding:6px 0;font-weight:700;color:var(--green);text-align:right;border-bottom:1px solid var(--border);">Likely $500K–$1M+ depending on balance</td></tr>
        <tr><td style="padding:6px 0;color:var(--muted);">Lender Requirement</td><td style="padding:6px 0;color:var(--red);font-weight:600;text-align:right;">Licensed URAR appraisal required</td></tr>
      </table>
    </div>
  </div>

  <!-- Market Context -->
  <div class="card" style="margin-bottom:20px;">
    <div class="card-title">Market Context — Fairfax County / 20124</div>
    <div class="grid-4">
      <div class="stat-box">
        <div class="stat-label">Median Sale Price (20124)</div>
        <div class="stat-val" style="font-size:1.2rem;">$880,860</div>
        <div class="stat-sub">All types, Redfin Feb 2026</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">YoY Trend (20124)</div>
        <div class="stat-val col-red" style="font-size:1.2rem;">−5.9%</div>
        <div class="stat-sub">Broad market softening</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Fairfax Co. Avg PSF</div>
        <div class="stat-val" style="font-size:1.2rem;">$374</div>
        <div class="stat-sub">All homes, Nov 2024</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Fairfax Co. Assessment</div>
        <div class="stat-val col-green" style="font-size:1.2rem;">+6.65%</div>
        <div class="stat-sub">2025 avg residential increase</div>
      </div>
    </div>
  </div>

  <!-- Reconciliation -->
  <div class="card" style="margin-bottom:20px;border-color:var(--accent);">
    <div class="card-title">Reconciliation</div>
    <div class="grid-4">
      <div style="padding:12px;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;text-align:center;">
        <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;margin-bottom:6px;">Sales Comparison<br>(70% weight)</div>
        <div style="font-size:1.2rem;font-weight:800;color:var(--green);">$2,650K–$2,750K</div>
      </div>
      <div style="padding:12px;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;text-align:center;">
        <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;margin-bottom:6px;">Cost Approach<br>(30% weight)</div>
        <div style="font-size:1.2rem;font-weight:800;color:var(--green);">$2,660K–$2,810K</div>
      </div>
      <div style="padding:12px;background:rgba(79,142,247,0.1);border:2px solid var(--accent);border-radius:8px;text-align:center;">
        <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;margin-bottom:6px;">Point Estimate</div>
        <div style="font-size:1.4rem;font-weight:900;color:var(--accent);">$2,700,000</div>
      </div>
      <div style="padding:12px;background:rgba(34,197,94,0.08);border:1px solid rgba(34,197,94,0.2);border-radius:8px;text-align:center;">
        <div style="font-size:0.68rem;color:var(--muted);text-transform:uppercase;margin-bottom:6px;">Full Range</div>
        <div style="font-size:1.1rem;font-weight:800;color:var(--green);">$2.60M–$2.85M</div>
      </div>
    </div>
  </div>

  <!-- Critical Notes -->
  <div class="alert alert-gold" style="line-height:1.8;">
    <strong>⚠️ Critical Notes for HELOC Appraisal Process</strong><br><br>
    <strong>1. Brief the appraiser before they pull public records.</strong> Zillow, Redfin, and Fairfax County assessments all show the prior structure. Provide: (a) contractor scope summary or invoices from the 2022 rebuild, (b) current interior photos, (c) Fairfax County permit records. If the appraiser anchors on the prior $850K sale, they will massively undervalue the property.<br><br>
    <strong>2. The prior $850K sale is a comp trap.</strong> It reflects the old structure — must be excluded entirely.<br><br>
    <strong>3. Document C2 condition.</strong> Prior appraisal documentation + photos of finishes and custom glass help the appraiser justify the quality rating.<br><br>
    <strong>4. In-law suite documentation.</strong> Confirm permits and egress windows so the 2,000 sqft below grade counts toward finished GLA.<br><br>
    <strong>5. HELOC math at $2.7M:</strong> 80% LTV = $2.16M loan basis. Subtract your outstanding first mortgage to get maximum HELOC line.
  </div>

</div>
</div>

'''

new_content = content[:start] + appraisal_html + '</body>'
with open('index.html', 'w') as f:
    f.write(new_content)

# Verify
with open('index.html', 'r') as f:
    verify = f.read()
if 'tab-6' in verify and 'Briarcroft' in verify:
    print("SUCCESS - tab-6 written with correct classes")
else:
    print("FAIL")
