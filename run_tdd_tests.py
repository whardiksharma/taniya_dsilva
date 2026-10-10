import os
import re
import sys

HTML_PATH = r"u:\home\hardi\frappe-bench\version-16\apps\taniya_dsilva\taniya_dsilva\www\index.html"
PUBLIC_DIR = r"u:\home\hardi\frappe-bench\version-16\apps\taniya_dsilva\taniya_dsilva\public"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

tests = []

def test(name, condition, details=""):
    tests.append({
        "name": name,
        "passed": bool(condition),
        "details": details
    })

# ═══════════════════════════════════════════════════════════════════════════
# 1. HEADER & GLOBAL NAVIGATION (BUTTONS, LINKS & CONTROLS)
# ═══════════════════════════════════════════════════════════════════════════
nav_block = content.split("<nav")[1].split("</nav>")[0] if "<nav" in content else ""
header_block = content.split("<header")[1].split("</header>")[0] if "<header" in content else ""

test("01. Nav: Medium Typography & Terracotta 'Ground Reality' Color", ("font-medium" in nav_block or "font-bold" in nav_block) and ("text-[#B65A3A]" in nav_block or "text-[#944226]" in nav_block))
test("02. Nav Link: About Section Target", 'href="#about"' in nav_block)
test("03. Nav Link: My Work Section Target", 'href="#work"' in nav_block)
test("04. Nav Link: Affiliations Section Target", 'href="#affiliations"' in nav_block)
test("05. Nav Link: Wise Impact Section Target", 'href="#pillars"' in nav_block)
test("06. Nav Link: 'What Others Say' Section Target", 'href="#endorsements"' in nav_block and "What Others Say" in nav_block)
test("07. Nav Link: Redundant Connect Removed", 'href="#connect"' not in nav_block)
test("08. Header: Brand Logo & Title Link to Hero", 'href="#hero"' in header_block and "Taniya D’silva" in header_block)
test("09. Header: 'Get in Touch' Theme CTA Button", 'href="#connect"' in header_block and "Get in Touch" in header_block and "bg-atlas-olive" in header_block)
test("10. Header: Interactive Search Input & Clear Control", 'id="pageSearchInput"' in header_block and 'id="searchClearBtn"' in header_block)

# ═══════════════════════════════════════════════════════════════════════════
# 2. HERO SECTION (BUTTONS, CTAs, METRICS & PORTRAIT COMPOSITION)
# ═══════════════════════════════════════════════════════════════════════════
hero_block = content.split('id="hero"')[1].split('id="about"')[0] if 'id="hero"' in content else ""

test("11. Hero CTA 1: 'Explore My Work' Button", 'href="#work"' in hero_block and "Explore My Work" in hero_block)
test("12. Hero CTA 2: 'View CV / Resume (PDF)' Browser Viewer Link", "View CV / Resume (PDF) ↗" in hero_block and "taniya_dsilva_resume.pdf" in hero_block and 'download=' not in hero_block)
test("13. Hero CTA 3: 'Get in Touch' Button", 'href="#connect"' in hero_block and "Get in Touch" in hero_block)
test("14. Hero Subtitle: Strategic Social Impact Descriptor (Bold)", "Strategic Social Impact Advisory | Research | Evidence-to-Action | Programme & Portfolio Management" in hero_block and "font-bold" in hero_block)
test("15. Hero Metric: ₹10.5 Cr Gender x Automotive Program", "₹10.5 Cr" in hero_block and "Program size managed in Gender x Automotive industry" in hero_block)
test("15b. Hero Metric: '15+ Years in Strategy & Impact'", "15+" in hero_block and (("Years in Strategy &amp; Impact" in hero_block) or ("Years in Strategy & Impact" in hero_block)))
test("16. Hero Portrait: RHS LinkedIn Direct Button Removed", 'class="absolute top-4 right-4' not in hero_block)
test("17. Hero Portrait: High-Contrast Frosted Nameplate", "Taniya D’silva" in hero_block and "Strategic Social Impact Advisory" in hero_block and "ssional & Advisory Identity" not in hero_block)
test("18. Hero Badge: LHS LinkedIn Direct Link & Official Logo (High-Contrast White Connect)", "https://www.linkedin.com/in/taniyadsilva" in hero_block and "Connect ↗" in hero_block and "color: #FFFFFF !important" in hero_block and "taniya_laptop_illustration.png" not in hero_block)

# ═══════════════════════════════════════════════════════════════════════════
# 3. ABOUT TANIYA SECTION (NARRATIVE, CREDENTIALS & CV LINK)
# ═══════════════════════════════════════════════════════════════════════════
about_block = content.split('id="about"')[1].split('id="work"')[0] if 'id="about"' in content else ""

test("19. About: Secondary Desk Headshot Integrated", "client_md_image5.png" in about_block)
test("20. About CTA: Exact Rewritten Collaboration Link", "Get in touch and let’s explore how I can help ↗" in about_block and 'href="#connect"' in about_block)
test("21. About: PMP Typo Removed (No Hyphen)", "PMP® Certified, 2026" in about_block)
test("22. About: 30+ Member Teams Interdisciplinary Credential", "research, design, partnerships & operations" in about_block)
test("23. About: Philanthropies 3-5 Year Investment Strategy", "Built 3–5 year investment and resourcing strategies for emerging and established philanthropies" in about_block)
test("24. About: Direct Complete CV & Resume Browser Viewer Link", ("View Complete CV" in about_block) and "taniya_dsilva_resume.pdf" in about_block and 'download=' not in about_block)
test("24b. About: '15+ Years in Strategy & Impact' Credential Title", ("15+ Years in Strategy &amp; Impact" in about_block) or ("15+ Years in Strategy & Impact" in about_block))

# ═══════════════════════════════════════════════════════════════════════════
# 4. MY WORK & RECENT PROJECTS (ALL 8 CARDS & LINKS)
# ═══════════════════════════════════════════════════════════════════════════
work_block = content.split('id="work"')[1].split('id="affiliations"')[0] if 'id="work"' in content else ""

test("25. Work Card 1: Mauritius Op-Ed Article & Link", "What Mauritius can learn from the Himalayas" in work_block and "lexpress.mu" in work_block)
test("26. Work Card 2: Climate Nonprofits Headline Image & Tags", "climate_course_headliner.jpg" in work_block and (("Strategic Capacity Building · Learning &amp; Development" in work_block) or ("Strategic Capacity Building · Learning & Development" in work_block)))
test("27. Work Card 3: Just Energy Transition Image & Tag", "just_transition_coal.jpg" in work_block and "Just Energy Transition" in work_block)
test("28. Work Card 4: ILSS People Practices Banner & Tag", "ilss_people_practices_banner.png" in work_block and "Strategic Capacity Building · Program Design" in work_block)
test("29. Work Card 5: Automotive & EV Sector Leadership", "women_automotive_ev.png" in work_block and "Gender, Labour" in work_block and "Nation-wide Program Leadership" in work_block)
test("30. Work Card 6: The Resilience Collaborative", "trc_landing_page.png" in work_block and "https://trc.community/" in work_block)
test("31. Work Card 7: UP BIU Grassroots Healthcare Image", "up_behavioural_health.jpg" in work_block and "Uttar Pradesh Behavioural Insights Unit" in work_block)
test("32. Work Card 8: Research Portfolio (RBI / HDFC & ILSS Removed)", "institutional_research.jpg" in work_block and "RBI Innovation Hub, HDFC, World YWCA" in work_block and "ILSS" not in work_block.split("<!-- Item 8:")[1].split("<!--")[0])

# ═══════════════════════════════════════════════════════════════════════════
# 5. AFFILIATIONS SECTION (AUTHENTIC LOGOS & MARKS)
# ═══════════════════════════════════════════════════════════════════════════
aff_block = content.split('id="affiliations"')[1].split('id="pillars"')[0] if 'id="affiliations"' in content else ""

test("33. Affiliations: RegenIntel Official Logo Mark", "regenintel_mark.png" in aff_block)
test("34. Affiliations: Terra.do Official Logo Mark", "terrado_mark.png" in aff_block or "terrado_logo" in aff_block)
test("35. Affiliations: Surge Climate Talent Official Logo", "surge_logo.png" in aff_block)
test("36. Affiliations: PMI PMP Official Round Badge", "client_md_image3.png" in aff_block)

# ═══════════════════════════════════════════════════════════════════════════
# 6. WISE IMPACT SOLUTIONS & 5 PRACTICE PILLARS
# ═══════════════════════════════════════════════════════════════════════════
pillars_block = content.split('id="pillars"')[1].split('id="endorsements"')[0] if 'id="pillars"' in content else ""

test("37. Wise Impact: Tagline Descriptor Label Removed", "Tagline / Descriptor:" not in pillars_block)
test("38. Wise Impact: Centered 3-over-2 Symmetrical Grid", "lg:w-[calc(33.333%-22px)]" in pillars_block)
test("39. Wise Impact: Bullet Font Size Improved", "text-xs sm:text-[13px]" in pillars_block)
test("39b. Wise Impact Pillar 3: 'Fractional Program Management & Delivery' 1st Bullet", "Fractional Program Management" in pillars_block.split("Programme & Portfolio Design")[1].split("<li>")[1])
test("40. Wise Impact Pillar 5: Speaking & Thought Leadership", "Speaking, Facilitation & Thought Leadership" in pillars_block and (("Panel discussions &amp; moderated conversations" in pillars_block) or ("Panel discussions & moderated conversations" in pillars_block)))

# ═══════════════════════════════════════════════════════════════════════════
# 7. ENDORSEMENTS & TESTIMONIALS
# ═══════════════════════════════════════════════════════════════════════════
endorse_block = content.split('id="endorsements"')[1].split('id="connect"')[0] if 'id="endorsements"' in content else ""

test("40b. Endorsements: 'What It’s Like to Work Together' Bold Eyebrow", "What It’s Like to Work Together" in endorse_block and "font-bold" in endorse_block)
test("41. Testimonial 1: Arjav Chakravarthi (Svarya) Verbatim", "Arjav Chakravarthi" in endorse_block and "Leadership Coach at Svarya" in endorse_block and "innovative and engaging course material" in endorse_block)
test("42. Testimonial 2: Bhumi Fellowship (2020) Verbatim", "Bhumi Fellowship" in endorse_block and "holistic inquiry, creates spaces for collective reflection" in endorse_block)
test("43. Testimonials CTA: 'See more recommendations on LinkedIn ↗'", "https://www.linkedin.com/in/taniyadsilva" in endorse_block and "See more recommendations on LinkedIn ↗" in endorse_block)

# ═══════════════════════════════════════════════════════════════════════════
# 8. CONTACT FORM & INSTANT ACKNOWLEDGEMENT MODAL
# ═══════════════════════════════════════════════════════════════════════════
form_block = content.split('id="connect"')[1].split("<footer")[0] if 'id="connect"' in content else ""

test("44. Form: Direct Inbox Routing Subtitle", "Have an idea, opportunity, or problem worth talking through? Inquiries route directly to Taniya. She actually reads her inbox—and replies." in form_block)
test("45. Form: 8 Scope Dropdown Options in Sentence Case", "Strategy and organisational advisory" in form_block and "Research and landscape analysis" in form_block and "Programme and portfolio management" in form_block)
test("46. Form: Submit Button Strict Label", "<button type=\"submit\"" in form_block and "Submit" in form_block)
test("47. Form: ConvertKit Acknowledgement Modal & Animation", "convertkit_email.gif" in form_block and "Thank you! I’ve received your note." in form_block and "I promise 🙂" in form_block)

# ═══════════════════════════════════════════════════════════════════════════
# 9. FOOTER & UI INTERACTION GUARDS
# ═══════════════════════════════════════════════════════════════════════════
footer_block = content.split("<footer")[1].split("</footer>")[0] if "<footer" in content else ""

test("48. Footer: Raw Email Address Removed", "mailto:its.taniya.dsilva@gmail.com" not in footer_block)
test("49. Footer: Verified LinkedIn & Get in Touch Links", "https://www.linkedin.com/in/taniyadsilva" in footer_block and 'href="#connect"' in footer_block)
test("50. UI Guard: .btn-resume Hover White Text CSS Enforced", ".btn-resume:hover *" in content and "color: #FFFFFF !important" in content)
test("51. Asset Guard: Valid Resume PDF File on Disk", os.path.exists(os.path.join(PUBLIC_DIR, "taniya_dsilva_resume.pdf")) and open(os.path.join(PUBLIC_DIR, "taniya_dsilva_resume.pdf"), "rb").read(4) == b"%PDF")
test("52. CV In-Website Viewer: Modal, Back to Website CTA & No-Download Guard", 'id="cvViewerModal"' in content and "← Back to Website" in content and "openCvViewer" in content and "#toolbar=0&navpanes=0" in content)

# ═══════════════════════════════════════════════════════════════════════════
# OUTPUT RESULTS
# ═══════════════════════════════════════════════════════════════════════════
total = len(tests)
passed = sum(1 for t in tests if t["passed"])
failed = total - passed

print(f"\n==========================================")
print(f"      TDD++ COMPREHENSIVE UI VERIFICATION ")
print(f"==========================================")
print(f"Total Test Cases : {total}")
print(f"Passed           : {passed}")
print(f"Failed           : {failed}")
print(f"Success Rate     : {(passed/total)*100:.1f}%\n")

for i, t in enumerate(tests, 1):
    status = "[PASS]" if t["passed"] else "[FAIL]"
    print(f"{i:02d}. {status} {t['name']}")

if failed > 0:
    sys.exit(1)
print("\n>>> ALL 51 UI BUTTON, LINK & INTERACTION TESTS PASSED 100% <<<")
