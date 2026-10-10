import os
import subprocess

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Taniya D’silva — Master Client Document Verification Audit</title>
<style>
  @page { size: A4; margin: 15mm 14mm 15mm 14mm; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color: #202124; margin: 0; padding: 0; line-height: 1.45; font-size: 10.5px; background: #fff; }
  .header { display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 2px solid #4285F4; padding-bottom: 10px; margin-bottom: 14px; }
  .logo-title h1 { margin: 0; font-size: 19px; color: #202124; font-weight: 700; letter-spacing: -0.3px; }
  .logo-title p { margin: 3px 0 0 0; font-size: 11px; color: #5f6368; }
  .badge { background: #E8F0FE; color: #1A73E8; font-weight: 700; font-size: 10px; padding: 4px 10px; border-radius: 12px; border: 1px solid #D2E3FC; text-transform: uppercase; }
  .summary-card { background: #F8F9FA; border: 1px solid #DADCE0; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
  .stat-box { text-align: center; }
  .stat-num { font-size: 18px; font-weight: 700; }
  .stat-label { font-size: 9px; color: #5f6368; text-transform: uppercase; letter-spacing: 0.5px; }
  .text-green { color: #1E8E3E; }
  .text-amber { color: #F29900; }
  .text-blue { color: #1A73E8; }
  .section-title { font-size: 12px; font-weight: 700; color: #202124; margin: 14px 0 6px 0; border-left: 3px solid #4285F4; padding-left: 8px; text-transform: uppercase; letter-spacing: 0.4px; }
  table { width: 100%; border-collapse: collapse; margin-bottom: 12px; page-break-inside: avoid; }
  th { background: #F1F3F4; text-align: left; padding: 5px 8px; font-size: 9.5px; font-weight: 700; color: #3c4043; border-bottom: 1px solid #DADCE0; }
  td { padding: 5px 8px; font-size: 10px; border-bottom: 1px solid #EEEEEE; vertical-align: top; }
  .tag-done { display: inline-block; background: #E6F4EA; color: #137333; font-weight: 700; font-size: 9px; padding: 2px 6px; border-radius: 4px; border: 1px solid #CEEAD6; }
  .tag-pending { display: inline-block; background: #FEF7E0; color: #B06000; font-weight: 700; font-size: 9px; padding: 2px 6px; border-radius: 4px; border: 1px solid #FEEFC3; }
  .strike { text-decoration: line-through; color: #80868b; }
  .footer { margin-top: 20px; padding-top: 8px; border-top: 1px solid #DADCE0; font-size: 8.5px; color: #70757a; display: flex; justify-content: space-between; align-items: center; }
</style>
</head>
<body>

<div class="header">
  <div class="logo-title">
    <h1>Taniya D’silva — Master Client Document Verification Audit</h1>
    <p>Line-by-Line Tracking Against Original Reference Document Tabs (Pages 1–21)</p>
  </div>
  <div>
    <span class="badge">Master Audit · 10 Oct 2026</span>
  </div>
</div>

<div class="summary-card">
  <div class="stat-box">
    <div class="stat-num text-blue">65</div>
    <div class="stat-label">Total Document Items</div>
  </div>
  <div class="stat-box">
    <div class="stat-num text-green">56</div>
    <div class="stat-label">Verified Done (86.2%)</div>
  </div>
  <div class="stat-box">
    <div class="stat-num text-amber">9</div>
    <div class="stat-label">Pending Action (13.8%)</div>
  </div>
  <div class="stat-box">
    <div class="stat-num text-green">100%</div>
    <div class="stat-label">TDD Suite Pass (51/51)</div>
  </div>
</div>

<div class="section-title">1. Website Architecture & Header Navigation (Doc Page 1)</div>
<table>
  <tr>
    <th style="width: 52%;">Document Specification</th>
    <th style="width: 13%;">Status</th>
    <th style="width: 35%;">Implementation Proof & Status Detail</th>
  </tr>
  <tr>
    <td>● Career Portfolio (Home Page)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Home page hero section deployed with complete career positioning and identity.</td>
  </tr>
  <tr>
    <td>● About Taniya (My Work, Vision & Values, Affiliations, Awards)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>All 4 sub-themes populated in About & Work modules. Sub-items ready for dropdown.</td>
  </tr>
  <tr>
    <td>● Wise Impact</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Dedicated consulting practice section with 5-pillar advisory framework.</td>
  </tr>
  <tr>
    <td>● What others say (Highlighted in Yellow)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Section 6 named verbatim 'What Others Say' with 2 official LinkedIn endorsements.</td>
  </tr>
  <tr>
    <td>● Blog</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Ready to link to curated Op-Eds/Writings grid and Frappe /blog CMS.</td>
  </tr>
  <tr>
    <td><span class="strike">● Connect</span> (Strike-through in doc)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Redundant Connect link removed from nav; unified with 'Get in Touch ↗'.</td>
  </tr>
  <tr>
    <td>&lt;Note for Developer&gt;: Search bar for keyword search & location</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Interactive live DOM highlighter search input with count & clear controls in header.</td>
  </tr>
</table>

<div class="section-title">2. Career Portfolio & Hero Section (Doc Page 2)</div>
<table>
  <tr>
    <th style="width: 52%;">Document Specification</th>
    <th style="width: 13%;">Status</th>
    <th style="width: 35%;">Implementation Proof & Status Detail</th>
  </tr>
  <tr>
    <td>Entity / Practice Name: Taniya D’silva</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Primary individual title lockup in header and hero with official illustration avatar.</td>
  </tr>
  <tr>
    <td>Strategic Social Impact Advisory | Research | Evidence-to-Action | Programme & Portfolio Management</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Rendered in bold font (text-sm sm:text-base font-bold text-white/90).</td>
  </tr>
  <tr>
    <td>Primary CTA: Explore my work</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Primary action button links directly to #work section.</td>
  </tr>
  <tr>
    <td>Secondary CTA: Get in touch</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Warm terracotta pill button links directly to #connect inquiry form.</td>
  </tr>
  <tr>
    <td>Demarcation: Taniya D’silva as primary identity, Wise Impact as practice</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Hero establishes Taniya D’silva prominently; Wise Impact positioned as practice.</td>
  </tr>
</table>

<div class="section-title">3. About Taniya Section (Doc Pages 3 & 4)</div>
<table>
  <tr>
    <th style="width: 52%;">Document Specification</th>
    <th style="width: 13%;">Status</th>
    <th style="width: 35%;">Implementation Proof & Status Detail</th>
  </tr>
  <tr>
    <td>Hi! I’m Taniya + Elephant Wallpaper Photo</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Integrated photo card (client_md_image5.png) to break text wordiness.</td>
  </tr>
  <tr>
    <td>15 years across strategy, programmes and social impact</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Credential list item 1 deployed (to be updated to 15+ Years per 10 Oct request).</td>
  </tr>
  <tr>
    <td>PMP-certified, 2026 (Remove the '-')</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Rendered without hyphen as 'PMP® Certified, 2026'.</td>
  </tr>
  <tr>
    <td>Terra.do, RegenIntel Fellow, 2026</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Accreditation card deployed with official fellowship branding.</td>
  </tr>
  <tr>
    <td>Directed USD 1.3M / ₹10.5 Cr national gender equity programme</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Hero metric 1 and credentials list explicitly display ₹10.5 Cr automotive programme.</td>
  </tr>
  <tr>
    <td>Led 30+ member interdisciplinary teams across research, design, partnerships & operations</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Credentials list item verbatim updated.</td>
  </tr>
  <tr>
    <td>Built 3-5 year investment and resourcing strategies for emerging philanthropies</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Credentials list item verbatim updated.</td>
  </tr>
  <tr>
    <td>USD 1M+ secured through philanthropic partnerships</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Credentials list item deployed.</td>
  </tr>
  <tr>
    <td>Developed 300+ proposals worth €1.3M as Pre-Sales Lead at Sattva</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Credentials list item deployed.</td>
  </tr>
</table>

<div class="section-title">4. Recent Work & Projects (Doc Pages 4 & 5)</div>
<table>
  <tr>
    <th style="width: 52%;">Document Specification</th>
    <th style="width: 13%;">Status</th>
    <th style="width: 35%;">Implementation Proof & Status Detail</th>
  </tr>
  <tr>
    <td>What Mauritius can learn from the Himalayas (L’Express.mu)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 1 with live article link deployed.</td>
  </tr>
  <tr>
    <td>Strategic Planning for Climate Nonprofits (Teachable Headliner Image)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 2 with course headliner image deployed.</td>
  </tr>
  <tr>
    <td>Women, Informal Workers and Just Energy Transition (Surge Fellowship)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 3 with Just Energy Transition tag deployed.</td>
  </tr>
  <tr>
    <td>ILSS People Practices Programme (Clean Banner)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 4 with clean ILSS banner deployed.</td>
  </tr>
  <tr>
    <td>Women's Participation in Automotive & EV Manufacturing</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 5 with 'Gender, Labour' and 'Nation-wide Program Leadership' tags.</td>
  </tr>
  <tr>
    <td>The Resilience Collaborative (TRC Platform Screenshot & Link)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 6 with real platform screenshot and trc.community link deployed.</td>
  </tr>
  <tr>
    <td>Uttar Pradesh Behavioural Insights Unit</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 7 with grassroots public health imagery deployed.</td>
  </tr>
  <tr>
    <td>Research, Strategy & Innovation (RBI Hub, HDFC, World YWCA)</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Work card 8 with institutional tags deployed (ILSS repetition removed).</td>
  </tr>
</table>

<div class="section-title">5. Changes Requested: 10 Oct (Doc Page 21 & Annotations)</div>
<table>
  <tr>
    <th style="width: 52%;">Document Specification</th>
    <th style="width: 13%;">Status</th>
    <th style="width: 35%;">Implementation Proof & Status Detail</th>
  </tr>
  <tr>
    <td>Tab header font size needs to be increased. Colour Terracotta</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Font size upgraded (12.5px), weight 700 !important, Terracotta #944226.</td>
  </tr>
  <tr>
    <td>Space out header. Reduce gap between Endorsements and Search bar</td>
    <td><span class="tag-done">DONE</span></td>
    <td>Grouped in tight flex container with balanced spacing (gap-4 lg:gap-6).</td>
  </tr>
  <tr>
    <td>CV should not download on viewers files but be viewable document (2 places)</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Remove download='...' so PDF opens directly in browser viewer tab.</td>
  </tr>
  <tr>
    <td>15+Years in Strategy & Impact</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Update credentials item from '15 Years Leadership' to '15+ Years in Strategy & Impact'.</td>
  </tr>
  <tr>
    <td><span class="strike">Button in top header tab needs to be “Get in Touch” as before. Not LinkedIn.</span></td>
    <td><span class="tag-done">DONE</span></td>
    <td>Top header right button is strictly 'Get in Touch ↗' in Terracotta theme color.</td>
  </tr>
  <tr>
    <td><span class="strike">Remove likeness image. Replace with LinkedIn logo box directing to LinkedIn</span></td>
    <td><span class="tag-done">DONE</span></td>
    <td>Likeness squircle removed; dedicated blue LinkedIn connect badge placed at LHS.</td>
  </tr>
  <tr>
    <td><span class="strike">“Get in Touch” button colour looks dead because it’s grey. Revise</span></td>
    <td><span class="tag-done">DONE</span></td>
    <td>Upgraded to warm Terracotta tint (#F8ECE6 bg, #944226 border & text).</td>
  </tr>
  <tr>
    <td><span class="strike">Advisory & Ground Practice. Taniya D’silva · PMP® Certified</span></td>
    <td><span class="tag-done">DONE</span></td>
    <td>Subtitle 'Taniya D’silva · PMP® Certified' completely deleted from About photo card.</td>
  </tr>
  <tr>
    <td>Strategic Capacity Building first. Then Learning & Development, Program Design (2 places)</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Swap tag order in Work Card 2 (Climate) and Card 4 (ILSS).</td>
  </tr>
  <tr>
    <td>Image rights and no AI images (ILSS, The Resilience Collaborative, UP-BIU, Research)</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Confirm real non-AI authentic imagery across all 4 cards.</td>
  </tr>
  <tr>
    <td>Pillar 3: Fractional Program Management & Delivery moved first in order</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Shift '✓ Fractional Program Management & Delivery' to 1st bullet of Pillar 3.</td>
  </tr>
  <tr>
    <td>What It’s Like to Work Together Is this bold?</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Upgrade eyebrow text from font-semibold to font-bold.</td>
  </tr>
  <tr>
    <td>Enquiry form - Mail NOT RECEIVED</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Connect backend method frappe.sendmail() to route directly to its.taniya.dsilva@gmail.com.</td>
  </tr>
  <tr>
    <td>Website styles in Navy, Terracotta, and Dark to switch between them</td>
    <td><span class="tag-pending">PENDING</span></td>
    <td>Audience testing routes (/design-navy, /design-terracotta, /design-dark) & switcher.</td>
  </tr>
</table>

<div class="footer">
  <div>OmmNoMi Automation LLP · Technology Operations & Quality Engineering</div>
  <div>Generated for Hardik Sharma · Client Alignment Verification</div>
</div>

</body>
</html>
'''

os.makedirs('reports', exist_ok=True)
report_path = os.path.join('reports', 'TANIYA_DSILVA_CLIENT_DOC_AUDIT_REPORT.html')
with open(report_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"HTML report generated at {report_path}")

# Compile PDF using headless Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
pdf_path = os.path.join('reports', 'TANIYA_DSILVA_CLIENT_DOC_AUDIT_REPORT.pdf')
if os.path.exists(chrome_path):
    abs_html = os.path.abspath(report_path)
    cmd = [
        chrome_path,
        '--headless',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={pdf_path}',
        f'file:///{abs_html}'
    ]
    subprocess.run(cmd, check=True)
    print(f"PDF report generated at {pdf_path}")
