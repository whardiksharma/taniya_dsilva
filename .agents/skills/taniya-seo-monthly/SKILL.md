---
name: taniya-seo-monthly
description: >
  Standard Operating Procedure for the Taniya D'silva monthly SEO programme —
  baseline audit, organic keyword tracking, conversion telemetry monitoring,
  Search Console verification, and executive consulting brief. Activate whenever working on
  Taniya D'silva SEO reports, keyword tracking, the monthly cycle, site audits, or anything
  under `apps/taniya_dsilva/seo/`.
---

# Taniya D’silva SEO — Standard Operating Procedure

> 💡 **AGENT DIRECTIVE:** You MUST actively update and improve this SOP file (`SKILL.md`) after every
> new task, feedback, or operational learning, so the knowledge repository grows continuously.
> Record durable learnings in the **Learning Log** at the bottom.

---

## 1. Scope — Locked

| Setting | Value |
|---|---|
| **Client** | Taniya D’silva (Wise Impact Consulting Solutions) |
| **Live site** | `https://taniyadsilva.com` |
| **Platform** | Frappe / Frappe Cloud (app `taniya_dsilva`) |
| **Core Verticals** | Strategic Social Impact Advisory · Evidence-to-Action Research · Climate Resilience · Gender Equity · Informal Labour · Public Health |
| **Target Geography** | **India** (Primary) & **Global Development Sector** (US, UK, Switzerland, Singapore). |
| **Cadence** | 25th of each month |
| **Baseline** | Month 0 — October 2026 (site/technical). **Month 1 — November 2026 is the traffic baseline**. |

---

## 2. Where Everything Lives

Everything is plain files in this repo. No DocType, no database record:

```
apps/taniya_dsilva/seo/
├── README.md                              folder map
├── METHOD.md                              THE FROZEN METHOD — the authority on how to measure
├── keywords/keyword-universe-v1.csv       42+ keywords across 6 clusters, add-only
├── reports/taniya-seo-report--YYYY-MM.md  one per month (Markdown ONLY - client docs saved in Drive)
├── templates/monthly-report-template.md   copy this each cycle
├── tracker/taniya-tracker.csv             one row per month, 36 columns (OmmNoMi standard)
├── fixes/fix-backlog.md                   prioritized fixes, mapped to file:line
└── evidence/                              dated raw captures, never overwritten
```

> ⛔ **`seo/` is internal.** It contains competitive intelligence, client conversion metrics, and agency
> commercial strategy. It must never be served by the website or linked publicly.

---

## 3. The Monthly Cycle — Run on the 25th

1. `cp seo/templates/monthly-report-template.md seo/reports/taniya-seo-report--YYYY-MM.md`
2. Fill every table using **exactly** the methods in `seo/METHOD.md`. Never substitute a method.
3. Mark every value ▲ / ▼ / — against **last month** and against **Month 0**.
4. Never leave a cell blank. Use `NEEDS ACCESS`, `NO TOOL`, or `NOT INSTALLED`.
5. Append one row to `seo/tracker/taniya-tracker.csv`.
6. Update fix statuses in `seo/fixes/fix-backlog.md`.
7. Finish with section 6, "Priorities for next cycle".
8. Add any new learning to the **Learning Log** below.

### Deliverable Naming — Frozen

```
TD_SEO-Report_YYYY-MM[_v<N>][_DRAFT].<ext>
```

| Field | Rule |
|---|---|
| `CODE` | Client code: **`TD`** (Taniya D’silva). |
| `Deliverable` | `SEO-Report` |
| `YYYY-MM` | ISO, zero-padded report month (e.g. `2026-10`). |
| `_v<N>` | Only when superseding a file already sent. |

---

## 4. Telemetry & GA4 Invariants

The 4 core conversions tracked in `taniyadsilva.com`:
1. `get_in_touch_click` — Clicks on any "Get in Touch" button (header, hero, footer).
2. `my_work_click` — Clicks on "My Work" buttons (nav dropdown, hero CTA).
3. `cv_button_click` — In-website CV/Resume PDF modal inspections (hero CTA, credentials section).
4. `contact_form_submit` — Direct advisory inquiries sent via `#inquiry-form`.

> ⚠️ **Strict Text Lockdown Invariant:** Never modify any user-facing text, button labels, headings, or bios when editing templates. Telemetry listeners must attach via event delegation or data attributes only.

---

## 5. Learning Log

| Date | Learning / Incident | Preventive Rule Adopted |
|---|---|---|
| 2026-10-12 | Initial SEO program instantiation for Taniya D'silva | Standardized 36-column tracker structure matching Gaonhae for portfolio concatenation. Injected GA4 conversion tracking across 3 button groups (Get in Touch, My Work, 2 CV buttons) without touching live page text. |
