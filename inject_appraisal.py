with open('dashboard.html', 'r') as f:
    content = f.read()

appraisal_tab = '''
<!-- HOME APPRAISAL TAB -->
<div class="tab-pane" id="tab-home-appraisal">
  <div class="market-header">
    <div class="market-flag">🏠</div>
    <div class="market-title">
      <h2>6705 Briarcroft St, Clifton VA 20124 <span style="font-size:14px;font-weight:400;color:#6b7280">— Primary Residence Appraisal</span></h2>
      <p>URAR-Methodology Assessment for HELOC · Full Custom Rebuild 2022 · Effective Age: 4 Years · C2 Condition Rating</p>
    </div>
    <div class="market-score"><div class="score-num" style="font-size:18px;">$2.60M–$2.85M</div><div class="score-label">Estimated Market Value</div></div>
  </div>

  <div class="verdict-box">
    <h3>Opinion of Value — As of April 2026</h3>
    <p class="verdict-text">
      <strong>Point Estimate: $2,700,000 &nbsp;|&nbsp; Range: $2,600,000 – $2,850,000</strong><br><br>
      This estimate uses the Sales Comparison Approach as the primary method, supported by a Cost Approach cross-check for luxury new construction in Fairfax County. The property is a fully custom 2022 rebuild — effectively functioning as new construction for appraisal purposes. All existing online data (Zillow, Redfin, public records) reflects the prior structure and is substantially understated. The prior sale at $850K / 3,902 sqft is not a relevant comparable. True comps are large custom luxury homes in Clifton and the Fairfax County estate market.
    </p>
    <div class="verdict-pros-cons">
      <div class="pros"><h4>Value Drivers</h4>
        <ul>
          <li>Full custom rebuild 2022 — effectively new construction</li>
          <li>5,900 total finished sqft (3,900 AG + 2,000 BG)</li>
          <li>Large expanses of custom glass — significant premium</li>
          <li>Luxury finishes throughout — Q1/Q2 construction quality</li>
          <li>9 bed / 5 bath total — exceptional for the market</li>
          <li>Full in-law suite with separate kitchen</li>
          <li>C2 condition — highest tier for existing homes</li>
          <li>Clifton, VA — one of Fairfax County's most desirable enclaves</li>
          <li>~5 acre lot, private, wooded setting</li>
        </ul>
      </div>
      <div class="cons"><h4>Limiting Factors</h4>
        <ul>
          <li>Below-grade GLA valued at ~50–60% of above-grade PSF</li>
          <li>Clifton micro-market is small — limited direct luxury comps</li>
          <li>Public records do not reflect 2022 rebuild — appraiser briefing critical</li>
          <li>20124 median down 5.9% YoY (Redfin Feb 2026) — market softening broadly</li>
          <li>HELOC lender will require licensed URAR appraisal — this is a pre-appraisal estimate</li>
        </ul>
      </div>
    </div>
  </div>

  <p class="section-title" style="margin-top:8px;">Subject Property — URAR Data Grid</p>
  <div class="detail-grid">
    <div class="detail-card">
      <h3>Property Identification</h3>
      <div class="stat-row"><span class="stat-label">Address</span><span class="stat-value">6705 Briarcroft St, Clifton VA 20124</span></div>
      <div class="stat-row"><span class="stat-label">County</span><span class="stat-value">Fairfax County, VA</span></div>
      <div class="stat-row"><span class="stat-label">Property Type</span><span class="stat-value">Single Family Residential</span></div>
      <div class="stat-row"><span class="stat-label">Lot Size (Est.)</span><span class="stat-value">~5 acres</span></div>
      <div class="stat-row"><span class="stat-label">Zoning (Est.)</span><span class="stat-value">RC — Rural Cluster / Residential</span></div>
      <div class="stat-row"><span class="stat-label">Neighborhood</span><span class="stat-value">Clifton / Briarcroft</span></div>
    </div>
    <div class="detail-card">
      <h3>Construction &amp; Condition</h3>
      <div class="stat-row"><span class="stat-label">Effective Year Built</span><span class="stat-value green">2022 (full custom rebuild)</span></div>
      <div class="stat-row"><span class="stat-label">Effective Age</span><span class="stat-value green">~4 years</span></div>
      <div class="stat-row"><span class="stat-label">Design / Style</span><span class="stat-value">Custom Contemporary Luxury</span></div>
      <div class="stat-row"><span class="stat-label">Construction Quality</span><span class="stat-value green">Q1–Q2 (Custom/Luxury)</span></div>
      <div class="stat-row"><span class="stat-label">Condition Rating</span><span class="stat-value green">C2 — Excellent (near-new)</span></div>
      <div class="stat-row"><span class="stat-label">Depreciation</span><span class="stat-value green">Minimal — ~2–3%</span></div>
    </div>
    <div class="detail-card">
      <h3>Room Count &amp; Area</h3>
      <div class="stat-row"><span class="stat-label">Above Grade GLA</span><span class="stat-value">3,900 sqft</span></div>
      <div class="stat-row"><span class="stat-label">Below Grade Finished</span><span class="stat-value">2,000 sqft (half-below grade)</span></div>
      <div class="stat-row"><span class="stat-label">Total Finished Area</span><span class="stat-value">5,900 sqft</span></div>
      <div class="stat-row"><span class="stat-label">Bedrooms (Above / Below)</span><span class="stat-value">6 AG + 3 BG = 9 total</span></div>
      <div class="stat-row"><span class="stat-label">Bathrooms (Above / Below)</span><span class="stat-value">3 full AG + 2 full BG = 5 total</span></div>
      <div class="stat-row"><span class="stat-label">In-Law Suite</span><span class="stat-value green">Yes — full kitchen, half-below grade</span></div>
    </div>
    <div class="detail-card">
      <h3>Special Features</h3>
      <div class="stat-row"><span class="stat-label">Custom Glass</span><span class="stat-value green">Large expanses — est. +$100–150K</span></div>
      <div class="stat-row"><span class="stat-label">Luxury Finishes</span><span class="stat-value green">Throughout — Q1 quality</span></div>
      <div class="stat-row"><span class="stat-label">In-Law Suite Kitchen</span><span class="stat-value green">Full kitchen — est. +$40–60K</span></div>
      <div class="stat-row"><span class="stat-label">Acreage Premium</span><span class="stat-value green">~5 acres — privacy, land value</span></div>
      <div class="stat-row"><span class="stat-label">Deferred Maintenance</span><span class="stat-value green">Minimal — 2022 rebuild</span></div>
    </div>
  </div>

  <p class="section-title" style="margin-top:8px;">Sales Comparison Approach — Comparable Sales Grid</p>
  <div class="full-width-card">
    <h3>Adjusted Comparable Sales</h3>
    <table class="overview-table">
      <thead>
        <tr>
          <th>Property</th>
          <th>Sale Price</th>
          <th>GLA</th>
          <th>$/sqft</th>
          <th>Yr Built</th>
          <th>Condition</th>
          <th>Adjustment to Subject</th>
          <th>Adj. Value</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#0c1a3a22;">
          <td><strong>SUBJECT: 6705 Briarcroft St</strong></td>
          <td><span class="badge badge-blue">Est. $2,700,000</span></td>
          <td>3,900 AG / 2,000 BG</td>
          <td>~$460 (AG)</td>
          <td>2022 (rebuild)</td>
          <td><span class="badge badge-green">C2</span></td>
          <td>—</td>
          <td>—</td>
        </tr>
        <tr>
          <td>Comp 1: 6501 Clifton Rd, Clifton</td>
          <td>$2,500,000</td>
          <td>6,488 sqft</td>
          <td>$385</td>
          <td>1997</td>
          <td>C3 (est.)</td>
          <td><span class="badge badge-green">+$150–200K: newer age, C2 vs C3, custom finishes</span></td>
          <td>$2,650–2,700K</td>
        </tr>
        <tr>
          <td>Comp 2: 6500 Briarcroft St, Clifton</td>
          <td>$2,999,900</td>
          <td>13,850 sqft</td>
          <td>$217</td>
          <td>2010</td>
          <td>C2–C3</td>
          <td><span class="badge badge-yellow">Larger sq footage pulls PSF down; adj for size</span></td>
          <td>$2,500–2,800K</td>
        </tr>
        <tr>
          <td>Comp 3: Clifton Luxury Active Listings</td>
          <td>$2,400K–$4,750K</td>
          <td>5,000–16,600 sqft</td>
          <td>$280–$450+</td>
          <td>Varies</td>
          <td>C2–C3</td>
          <td><span class="badge badge-blue">Subject in mid-range of active luxury inventory</span></td>
          <td>$2,600–2,850K</td>
        </tr>
        <tr>
          <td>Comp 4: Fairfax Co. Custom New Build (Cost)</td>
          <td>—</td>
          <td>5,900 sqft equiv.</td>
          <td>$340–520/sqft build</td>
          <td>2022</td>
          <td>C2</td>
          <td><span class="badge badge-green">Cost approach corroborates sales comparison</span></td>
          <td>$2,580–2,930K</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="section-title" style="margin-top:8px;">Cost Approach &amp; HELOC Analysis</p>
  <div class="detail-grid">
    <div class="detail-card">
      <h3>Replacement Cost New (RCN)</h3>
      <div class="stat-row"><span class="stat-label">Above Grade: 3,900 sqft @ $460/sqft</span><span class="stat-value">$1,794,000</span></div>
      <div class="stat-row"><span class="stat-label">Below Grade: 2,000 sqft @ $200/sqft</span><span class="stat-value">$400,000</span></div>
      <div class="stat-row"><span class="stat-label">Custom Glass Premium</span><span class="stat-value">+$125,000 (est.)</span></div>
      <div class="stat-row"><span class="stat-label">In-Law Suite Premium</span><span class="stat-value">+$50,000 (est.)</span></div>
      <div class="stat-row"><span class="stat-label">Total RCN</span><span class="stat-value green">~$2,369,000</span></div>
      <div class="stat-row"><span class="stat-label">Less Depreciation (~2.5%)</span><span class="stat-value green">-$59,225</span></div>
      <div class="stat-row"><span class="stat-label">Depreciated Improvement Value</span><span class="stat-value green">~$2,310,000</span></div>
      <div class="stat-row"><span class="stat-label">Plus Land Value (~5 acres Clifton)</span><span class="stat-value">+$350,000–$500,000</span></div>
      <div class="stat-row"><span class="stat-label">Cost Approach Indicated Value</span><span class="stat-value green">$2,660,000–$2,810,000</span></div>
    </div>
    <div class="detail-card">
      <h3>HELOC Borrowing Capacity</h3>
      <div class="stat-row"><span class="stat-label">Estimated Market Value</span><span class="stat-value green">$2,700,000</span></div>
      <div class="stat-row"><span class="stat-label">HELOC LTV @ 80%</span><span class="stat-value">$2,160,000 max basis</span></div>
      <div class="stat-row"><span class="stat-label">HELOC LTV @ 85%</span><span class="stat-value">$2,295,000 max basis</span></div>
      <div class="stat-row"><span class="stat-label">Less First Mortgage Balance</span><span class="stat-value yellow">Subtract existing balance</span></div>
      <div class="stat-row"><span class="stat-label">Available HELOC Line (Est.)</span><span class="stat-value green">Substantial — likely $500K–$1M+</span></div>
      <div class="stat-row"><span class="stat-label">Lender Requirement</span><span class="stat-value red">Licensed URAR appraisal required</span></div>
      <div class="stat-row"><span class="stat-label">Key Action</span><span class="stat-value yellow">Brief appraiser before records pull</span></div>
    </div>
    <div class="detail-card">
      <h3>Market Context — Fairfax County 2026</h3>
      <div class="stat-row"><span class="stat-label">Median Sale Price (20124)</span><span class="stat-value">$880,860 (all types, Feb 2026)</span></div>
      <div class="stat-row"><span class="stat-label">20124 YoY Trend</span><span class="stat-value red">-5.9% — broad market softening</span></div>
      <div class="stat-row"><span class="stat-label">Fairfax Co. Avg PSF (all homes)</span><span class="stat-value">$374 (Nov 2024)</span></div>
      <div class="stat-row"><span class="stat-label">Luxury PSF (custom/new)</span><span class="stat-value green">$420–$480+ (est.)</span></div>
      <div class="stat-row"><span class="stat-label">Fairfax Co. Assessment Increase</span><span class="stat-value green">+6.65% avg (2025 cycle)</span></div>
      <div class="stat-row"><span class="stat-label">Active Luxury Inventory (20124)</span><span class="stat-value">14 listings; days on market: 28</span></div>
    </div>
    <div class="detail-card">
      <h3>Reconciliation</h3>
      <div class="stat-row"><span class="stat-label">Sales Comparison (70% weight)</span><span class="stat-value green">$2,650,000–$2,750,000</span></div>
      <div class="stat-row"><span class="stat-label">Cost Approach (30% weight)</span><span class="stat-value green">$2,660,000–$2,810,000</span></div>
      <div class="stat-row"><span class="stat-label">Reconciled Point Estimate</span><span class="stat-value green" style="font-size:15px;font-weight:800;">$2,700,000</span></div>
      <div class="stat-row"><span class="stat-label">Conservative Floor</span><span class="stat-value">$2,600,000</span></div>
      <div class="stat-row"><span class="stat-label">Optimistic Ceiling</span><span class="stat-value">$2,850,000</span></div>
      <div class="stat-row"><span class="stat-label">Assessment Date</span><span class="stat-value">April 2026</span></div>
    </div>
  </div>

  <div class="verdict-box" style="margin-top:8px; border-color:#f59e0b44;">
    <h3>⚠️ Critical Notes for HELOC Appraisal Process</h3>
    <p class="verdict-text">
      <strong>1. Brief the appraiser before they pull public records.</strong> Zillow, Redfin, and Fairfax County assessments all show the prior structure — not the 2022 rebuild. Provide: (a) a scope summary or contractor invoice showing the rebuild, (b) current interior photos, (c) Fairfax County permit records for the rebuild scope. If the appraiser anchors on the prior $850K sale or old sqft data, they will massively undervalue the property.<br><br>
      <strong>2. The prior $850K sale is a comp trap.</strong> It reflects the old structure and must be excluded entirely from the comparable analysis.<br><br>
      <strong>3. Document the C2 condition rating.</strong> If you have prior appraisal documentation establishing C2, bring it. Photos of custom finishes and glass help the appraiser justify the quality rating.<br><br>
      <strong>4. In-law suite documentation.</strong> Confirm permits, egress windows, and that finished below-grade space meets code — this determines how much of the 2,000 sqft counts toward GLA vs. bonus area.<br><br>
      <strong>5. HELOC math: at $2.7M value, 80% LTV = $2.16M loan basis.</strong> Subtract your outstanding first mortgage balance to get your maximum available HELOC line.
    </p>
  </div>
</div>
'''

target = '</div><!-- /content -->'
if target in content:
    new_content = content.replace(target, appraisal_tab + '\n' + target, 1)
    with open('dashboard.html', 'w') as f:
        f.write(new_content)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
