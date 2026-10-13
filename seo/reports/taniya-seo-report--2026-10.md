# Taniya D’silva — SEO Baseline Audit & Launch Report (October 2026)

**Month 0 · Cycle date 12 October 2026 · Technical Infrastructure & Telemetry Baseline**

---

## 0. Header

| Field | Value |
|---|---|
| Client / brand | Taniya D’silva (Wise Impact Consulting Solutions) |
| Domain(s) | `https://taniyadsilva.com` · `taniyadsilva.com` |
| Industry / vertical | Strategic Social Impact Advisory · Evidence-to-Action Research · Portfolio Management |
| Practice focus | Climate Resilience · Gender Equity in Industry · Informal Labour Markets · Rural Public Health |
| Target geography | India (Primary) · Global Development Sector (US, UK, Switzerland, Singapore) |
| Platform | Frappe Cloud (app `taniya_dsilva`) |
| Report date | 12 October 2026 |
| Month | Month 0 (Baseline) |
| Agency team | Nomeshwer Sharma (SEO & Admin Lead) · Hardik Sharma (Technical Architect) |

---

## 1. Executive Summary

> **The one-line read:** Month 0 baseline successfully deployed — `robots.txt` and `sitemap.xml` established, Google Analytics 4 (GA4) with custom event conversion telemetry active for all "Get in Touch", "My Work", and both CV buttons, Schema.org JSON-LD structured data live, and Google Search Console property ready for Nomeshwer Sharma (`nomeshwer@ommnomi.in`).

### At-a-Glance Scorecard

| Dimension | Baseline State (12 Oct 2026) | Target for Month 1 (Nov 2026) | Action Item |
|---|---|---|---|
| **Crawl Directives** | ✅ `robots.txt` deployed | Verified by Googlebot | Pointer to `sitemap.xml` active |
| **Indexation Map** | ✅ `sitemap.xml` deployed (6 URLs) | Indexed in GSC | Submit sitemap in Search Console |
| **Structured Data** | ✅ Schema.org `Person` & `ProfessionalService` | Rich result eligibility | Entity disambiguation active |
| **Search Console** | 🔄 Verification meta deployed | Property verified with Admin access | Grant `nomeshwer@ommnomi.in` owner rights |
| **GA4 Telemetry** | ✅ `gtag.js` engine + 4 custom events | Accumulating baseline users | Track conversions in GA4 reports |
| **Conversion: Get in Touch** | ✅ Header, Hero, and Footer tracked | Baseline CTR measurement | Event: `get_in_touch_click` |
| **Conversion: My Work** | ✅ Dropdown and Hero buttons tracked | Baseline interest rate | Event: `my_work_click` |
| **Conversion: CV Viewer** | ✅ Hero & Credentials CV buttons tracked | Baseline credentials audit | Event: `cv_button_click` |
| **Lead Submissions** | ✅ `#inquiry-form` tracked | Direct inquiry capture | Event: `contact_form_submit` |
| **Performance (CWV)** | ✅ Fast Sandstone CDN & WebP images | Mobile > 90, Desktop > 95 | Sub-200ms TTFB |

---

## 2. Key Telemetry Events Deployed

The GA4 telemetry engine is injected into `apps/taniya_dsilva/taniya_dsilva/www/index.html` with safe error-handling (never interrupts UI or form submissions).

| Event Name | Monitored Element | Location Contexts | Primary Metric |
|---|---|---|---|
| `get_in_touch_click` | `<a href="#connect">` | `header_nav`, `hero_cta`, `footer_link` | Lead intent velocity |
| `my_work_click` | `<a href="#work">` | `header_dropdown`, `hero_cta` | Portfolio exploration depth |
| `cv_button_click` | `<a onclick="openCvViewer()">` | `hero_cta`, `credentials_section` | Professional credentials review rate |
| `contact_form_submit` | `<form id="inquiry-form">` | `#connect` section | Hard lead conversion |

---

## 3. Crawler Discovery Architecture

1. **`robots.txt`**:
   - URL: `https://taniyadsilva.com/robots.txt`
   - Directs crawlers to root, allows asset indexing for high-resolution portfolio images, and points directly to the XML sitemap.
2. **`sitemap.xml`**:
   - URL: `https://taniyadsilva.com/sitemap.xml`
   - Maps core single-page anchor sections (`#about`, `#work`, `#pillars`, `#endorsements`, `#connect`) to facilitate deep section indexing in Google SERP sitelinks.

---

## 4. Keyword Universe v1.0 Overview

- Total Tracked Queries: **42 keywords** across 6 strategic clusters:
  1. **Branded (10):** `taniya d'silva`, `wise impact consulting solutions`, `taniya d'silva resume`, etc.
  2. **Social Impact Advisory (10):** `strategic social impact advisory`, `evidence to action research`, etc.
  3. **Climate & Agrarian (8):** `climate resilience consultant india`, `agrarian transitions advisory`, etc.
  4. **Gender Equity & Labour (8):** `gender equity in industry consultant`, `informal labour markets research`, etc.
  5. **Public Health (6):** `rural public health consultant india`, `evidence to action public health`, etc.
  6. **Portfolio Leadership (6):** `pmp certified social impact`, `fractional social impact director`, etc.

---

## 5. Google Search Console & GA4 Setup Walkthrough for Nomeshwer

### Search Console Setup:
1. Navigate to [Google Search Console](https://search.google.com/search-console).
2. Select **Add Property**:
   - **Option A (Recommended):** URL prefix: `https://taniyadsilva.com`.
   - Verification Method: **HTML tag** (the meta tag is already present in `<head>`).
3. Under **Settings → Users and permissions**:
   - Add **`nomeshwer@ommnomi.in`** with **Owner** permissions.
4. Go to **Sitemaps**:
   - Enter `sitemap.xml` and click **Submit**.

### Google Analytics 4 Setup:
1. Navigate to [Google Analytics](https://analytics.google.com/).
2. Create property: `Taniya D'silva Portfolio (taniyadsilva.com)`.
3. Under **Admin → Property Access Management**:
   - Add **`nomeshwer@ommnomi.in`** as **Administrator**.
4. In **Admin → Data Streams → Web Stream**:
   - Copy the Measurement ID (`G-XXXXXXXXXX`).
5. In **Admin → Events → Key Events**:
   - Mark `contact_form_submit`, `get_in_touch_click`, `cv_button_click`, and `my_work_click` as **Key Events (Conversions)**.
