# Taniya D’silva SEO — THE FROZEN METHOD

**Version 1.0 — Adopted October 2026**

This document specifies the exact measurement sources, methodologies, and calculation formulas used across all monthly SEO reports for `taniyadsilva.com`. Changing any method here breaks historical comparability across the OmmNoMi agency portfolio.

---

## 1. Geographic & Vertical Scope

- **Primary Domain:** `https://taniyadsilva.com`
- **Secondary Routing:** Root domain redirect `http://taniyadsilva.com` → `https://taniyadsilva.com`
- **Core Industry / Vertical:** Strategic Social Impact Advisory, Evidence-to-Action Research, Programme & Portfolio Leadership (Climate Resilience, Gender Equity in Industry, Informal Labour, Rural Public Health).
- **Geographic Focus:** 
  - **India** (New Delhi, Bengaluru, Mumbai, rural agrarian belts)
  - **Global Impact Hubs** (London, Geneva, Washington DC, Singapore, Nairobi)

---

## 2. Measurement Instruments & Sources of Truth

| Dimension | Primary Tool | Secondary / Fallback | Definition of Record |
|---|---|---|---|
| **Organic Clicks & Impressions** | Google Search Console (GSC) | — | 28-day rolling window ending on the 24th of the report month. |
| **Average Keyword Position** | GSC Performance Export | Manual Incognito SERP | Weighted average position reported by GSC for tracked queries. |
| **Site Users & Engagement** | Google Analytics 4 (GA4) | — | Total users, engagement rate, average session duration. |
| **Key Conversions** | GA4 Custom Events | Form Desk Submissions | 4 Conversion Events: `get_in_touch_click`, `my_work_click`, `cv_button_click`, `contact_form_submit`. |
| **Leads & Inquiries** | `#inquiry-form` submissions | GA4 `contact_form_submit` | Inquiries received via desk or direct notification. |
| **Core Web Vitals** | Lighthouse (Mobile & Desktop) | PageSpeed Insights | Lab performance scores measured against `https://taniyadsilva.com`. |
| **Indexation Status** | GSC Page Indexing Report | `site:taniyadsilva.com` query | Number of valid indexed URLs vs sitemap submitted URLs. |

---

## 3. The 4 Key Conversion Telemetry Events

| Event Name | Trigger Condition | Parameters Captured | Business Impact |
|---|---|---|---|
| `get_in_touch_click` | Visitor clicks any "Get in Touch" CTA button | `button_name`, `button_location` (`header_nav`, `hero_cta`, `footer_link`), `target` | High-intent lead indicator |
| `my_work_click` | Visitor clicks "My Work" navigation or hero button | `button_name`, `button_location` (`header_dropdown`, `hero_cta`), `target` | Portfolio engagement indicator |
| `cv_button_click` | Visitor opens the in-website PDF CV / Resume modal | `button_name`, `button_location` (`hero_cta`, `credentials_section`), `action` | Credentials scrutiny / recruitment signal |
| `contact_form_submit` | Visitor submits the `#inquiry-form` contact note | `form_id`, `form_name` | Direct advisory engagement enquiry |

---

## 4. Cadence & Review Rules

- **Measurement Date:** 25th of each month (matching OmmNoMi agency standard).
- **Comparison Baseline:** Month 0 (October 2026).
- **Reporting Period:** Full calendar month or rolling 28-day window ending on the 24th.
- **Delta Notation:** ▲ (improvement / positive), ▼ (regression / decline), — (unchanged).
- **Missing Data Codes:** `NEEDS ACCESS` (missing account credentials), `NOT INSTALLED` (tag missing), `NO DATA` (source empty).
