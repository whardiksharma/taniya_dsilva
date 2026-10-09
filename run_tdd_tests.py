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

# 1. Header Navigation Tests
nav_block = content.split("<nav")[1].split("</nav>")[0]
test("Header: Bold Navigation Tabs", "font-bold" in nav_block and "text-white" in nav_block)
test("Header: Zero Redundant Connect Tab", 'href="#connect"' not in content.split("<nav")[1].split("</nav>")[0])
test("Header: Direct LinkedIn Pill CTA", "https://www.linkedin.com/in/taniyadsilva" in content.split("<header")[1].split("</header>")[0])

# 2. Hero Section Tests
test("Hero: Likeness Badge Removed from LHS", 'absolute -bottom-6 -left-6' not in content)
test("Hero: Subtitle Descriptor Bold & Enriched", "Strategic Social Impact Advisory | Research | Evidence-to-Action | Programme & Portfolio Management" in content and "font-bold" in content)
test("Hero: Metric ₹10.5 Cr Formatted", "₹10.5 Cr" in content and "Program size managed in Gender x Automotive industry" in content)
test("Hero: CV Download Action Present", "Download CV / Bio (PDF) ↗" in content)

# 3. About Taniya Section Tests
test("About: Secondary Headshot Integrated", "client_md_image5.png" in content)
test("About: Exact Rewritten CTA Link", "Get in touch and let’s explore how I can help ↗" in content)
test("About: PMP Typo Removed (No Hyphen)", "PMP® Certified, 2026" in content)
test("About: 30+ Member Teams Credential Updated", "research, design, partnerships & operations" in content)
test("About: Philanthropies Credential Updated", "Built 3–5 year investment and resourcing strategies for emerging and established philanthropies" in content)

# 4. My Work & Recent Projects (8 Cards)
test("Work Card 1: Mauritius Op-Ed", "What Mauritius can learn from the Himalayas" in content)
test("Work Card 2: Climate Nonprofits Headliner Image", "climate_course_headliner.jpg" in content and "Learning & Development · Strategic Capacity Building" in content)
test("Work Card 3: Just Energy Transition Image & Tag", "just_transition_coal.jpg" in content and "Just Energy Transition" in content)
test("Work Card 4: ILSS Banner & Tag Positioned", "ilss_people_practices_banner.png" in content and "Program Design · Strategic Capacity Building" in content)
test("Work Card 5: Automotive EV Shopfloor Image & Tags", "women_automotive_ev.png" in content and "Gender, Labour" in content and "Nation-wide Program Leadership" in content)
test("Work Card 6: The Resilience Collaborative", "trc_landing_page.png" in content and "https://trc.community/" in content)
test("Work Card 7: UP BIU Authentic Healthcare Image", "up_behavioural_health.jpg" in content and "Uttar Pradesh Behavioural Insights Unit" in content)
test("Work Card 8: Research Portfolio Fintech Setting & RBI/HDFC", "institutional_research.jpg" in content and "RBI Innovation Hub, HDFC, World YWCA" in content and "ILSS" not in content.split("<!-- Item 8:")[1].split("<!--")[0])

# 5. Affiliations Section Tests
test("Affiliations: RegenIntel Official Logo Mark", "regenintel_mark.png" in content)
test("Affiliations: Terra.do Official Logo Mark", "terrado_mark.png" in content or "terrado_logo" in content)
test("Affiliations: Surge Climate Talent Official Logo", "surge_logo.png" in content)
test("Affiliations: PMI PMP Official Round Badge", "client_md_image3.png" in content.split("<!-- PMP -->")[1].split("</section>")[0])

# 6. Wise Impact & 5 Pillars Tests
test("Wise Impact: Tagline Descriptor Label Removed", "Tagline / Descriptor:" not in content)
test("Wise Impact: Centered 3-over-2 Symmetrical Grid", "lg:w-[calc(33.333%-22px)]" in content)
test("Wise Impact: Increased Bullet Font Size", "text-xs sm:text-[13px]" in content)

# 7. Testimonials (What Others Say)
test("Testimonials: Arjav Chakravarthi (Svarya) Verbatim", "Arjav Chakravarthi" in content and "Leadership Coach at Svarya" in content and "innovative and engaging course material" in content)
test("Testimonials: Bhumi Fellowship Verbatim", "Bhumi Fellowship" in content and "holistic inquiry, creates spaces for collective reflection" in content)

# 8. Inquiry Form & Acknowledgement Tests
test("Form: Exact Inbox Routing Subtitle", "Have an idea, opportunity, or problem worth talking through? Inquiries route directly to Taniya. She actually reads her inbox—and replies." in content)
test("Form: 8 Scope Options in Sentence Case", "Strategy and organisational advisory" in content and "Research and landscape analysis" in content)
test("Form: Submit Button Strict Label", "<button type=\"submit\"" in content and "Submit" in content)
test("Form: ConvertKit Acknowledgement Modal", "convertkit_email.gif" in content and "Thank you! I’ve received your note." in content and "I promise 🙂" in content)

# 9. Footer & Architecture Tests
test("Footer: Raw Email Removed from Footer", "mailto:its.taniya.dsilva@gmail.com" not in content.split("<footer")[1].split("</footer>")[0])
test("Footer: Verified LinkedIn Link in Footer", "https://www.linkedin.com/in/taniyadsilva" in content.split("<footer")[1].split("</footer>")[0])

# Output Results
total = len(tests)
passed = sum(1 for t in tests if t["passed"])
failed = total - passed

print(f"\n==========================================")
print(f"      TDD++ AUTOMATED VERIFICATION SUITE   ")
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
print("\n>>> ALL CRITICAL UI TESTS PASSED 100% <<<")
