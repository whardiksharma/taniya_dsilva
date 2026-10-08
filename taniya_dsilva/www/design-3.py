# Copyright (c) 2026, OmmNoMi Automation LLP and contributors
# For license information, please see license.txt

import frappe

def get_context(context):
    context.no_cache = 1
    settings = None
    try:
        if frappe.db.exists("DocType", "Taniya Portfolio Settings"):
            settings = frappe.get_single("Taniya Portfolio Settings")
    except Exception:
        settings = None

    context.content = {
        "full_name": (settings.full_name if settings and settings.get("full_name") else "Taniya D’silva"),
        "tagline": (settings.tagline if settings and settings.get("tagline") else "Strategy and Programme/Portfolio Leadership for Social Impact"),
        "sub_descriptor": (settings.sub_descriptor if settings and settings.get("sub_descriptor") else "Strategic Social Impact Advisory | Research | Evidence-to-Action Programme & Portfolio Management"),
        "contact_email": (settings.contact_email if settings and settings.get("contact_email") else "its.taniya.dsilva@gmail.com"),
        "linkedin_url": (settings.linkedin_url if settings and settings.get("linkedin_url") else "https://www.linkedin.com/in/taniyadsilva"),
        "headshot_image": (settings.headshot_image if settings and settings.get("headshot_image") else "/assets/taniya_dsilva/images/taniya_headshot_2.png"),
        "headshot_alt": (settings.get("headshot_alt") if settings and settings.get("headshot_alt") else "/assets/taniya_dsilva/images/taniya_headshot_1.png"),
        "animated_likeness_image": (settings.animated_likeness_image if settings and settings.get("animated_likeness_image") else "/assets/taniya_dsilva/images/taniya_animated_likeness.png"),
        "hero_headline": (settings.hero_headline if settings and settings.get("hero_headline") else "Translating evidence and grand vision into ground reality."),
        "hero_subheadline": (settings.hero_subheadline if settings and settings.get("hero_subheadline") else "15 years driving organisational strategy, multi-stakeholder programmes, executive communications, and donor partnerships across climate, gender equity, labour markets and public health in LMIC contexts."),
        "pmp_year": (settings.pmp_year if settings and settings.get("pmp_year") else "2026"),
        "metric_years": (settings.metric_years if settings and settings.get("metric_years") else "15"),
        "metric_ev_fund": (settings.metric_ev_fund if settings and settings.get("metric_ev_fund") else "$1.3M"),
        "metric_team_size": (settings.metric_team_size if settings and settings.get("metric_team_size") else "30+"),
        "metric_philanthropy_capital": (settings.metric_philanthropy_capital if settings and settings.get("metric_philanthropy_capital") else "$1M+"),
        "metric_proposals_val": (settings.metric_proposals_val if settings and settings.get("metric_proposals_val") else "€1.3M"),
        "metric_proposals_count": (settings.metric_proposals_count if settings and settings.get("metric_proposals_count") else "300+"),
        "bio_text": (settings.bio_text if settings and settings.get("bio_text") else "Taniya D’silva is a strategy and programme leader with 15 years of experience driving organisational strategy, multi-stakeholder programmes, executive communications, and donor and government partnerships across climate, gender equity, labour markets and public health in LMIC contexts.\n\nShe works at the intersection of research, strategy and implementation, helping organisations translate evidence and strategic priorities into practical programmes, partnerships and organisational action. Her experience spans advisory work with nonprofits, foundations, private sector, government bodies and other social-impact organisations."),
        "approach_text": (settings.approach_text if settings and settings.get("approach_text") else "Her approach combines strategic thinking with practical execution: understanding the evidence, clarifying the strategic choices, aligning stakeholders and translating priorities into implementable programmes and systems."),
        "practice_positioning_note": (settings.practice_positioning_note if settings and settings.get("practice_positioning_note") else "Taniya D’silva as the primary professional/advisory identity, with Wise Impact Consulting Solutions presented as her current consulting practice."),
        "wise_impact_title": (settings.wise_impact_title if settings and settings.wise_impact_title else "Wise Impact Consulting Solutions"),
        "wise_impact_thesis": (settings.wise_impact_thesis if settings and settings.wise_impact_thesis else "WISE understands the demands made of social sector leaders to straddle the twin responsibilities of being the vision bearers of their ideas for a just and equitable world and that of rallying the team and the organization to translate the grand vision to programs on the ground."),
        "wise_impact_description": (settings.wise_impact_description if settings and settings.wise_impact_description else "Wise Impact Consulting Solutions provides actionable advisory solutions in research, strategy development, programme design, and organisational capability building to nonprofits and foundations to aid with bringing these visions to life."),
        "pillar_1_title": (settings.pillar_1_title if settings and settings.pillar_1_title else "Strategy & Organisational Advisory"),
        "pillar_1_desc": (settings.pillar_1_desc if settings and settings.pillar_1_desc else "Helping organisations translate ambition into clear strategic choices, priorities and roadmaps."),
        "pillar_2_title": (settings.pillar_2_title if settings and settings.pillar_2_title else "Research & Strategy"),
        "pillar_2_desc": (settings.pillar_2_desc if settings and settings.pillar_2_desc else "Turning evidence, research and stakeholder insights into actionable strategic direction."),
        "pillar_3_title": (settings.pillar_3_title if settings and settings.pillar_3_title else "Programme & Portfolio Design"),
        "pillar_3_desc": (settings.pillar_3_desc if settings and settings.pillar_3_desc else "Design and strengthen programmes that move from strategic intent to effective implementation."),
        "pillar_4_title": (settings.pillar_4_title if settings and settings.pillar_4_title else "Partnerships & Organisational Capability"),
        "pillar_4_desc": (settings.pillar_4_desc if settings and settings.pillar_4_desc else "Strengthening the relationships, capabilities and systems needed to deliver impact on the ground."),
        "recent_work_1_title": (settings.recent_work_1_title if settings and settings.recent_work_1_title else "What Mauritius can learn from the Himalayas"),
        "recent_work_1_url": (settings.recent_work_1_url if settings and settings.recent_work_1_url else "https://lexpress.mu/node/561910"),
        "recent_work_2_title": (settings.recent_work_2_title if settings and settings.recent_work_2_title else "Strategic Planning for Climate Nonprofits"),
        "recent_work_2_url": (settings.recent_work_2_url if settings and settings.recent_work_2_url else "https://strategic-planning-for-climate-nonprofits.teachable.com/p/strategic-planning-for-climate-change-organizations"),
    }
    return context
