# Taniya D’silva — Technical SEO Fix Backlog

Prioritized backlog of technical, structural, and semantic SEO items for `https://taniyadsilva.com`, mapped to repo files and lines.

---

## Priority Scale
- **P0 — Critical:** Blocking indexation, analytics outage, crawl blocking.
- **P1 — High:** Rich snippet eligibility, core ranking signal, conversion tracking gap.
- **P2 — Medium:** Performance optimization, asset size reduction, OpenGraph enhancements.
- **P3 — Low:** Cosmetic or progressive enhancement.

---

## Backlog

| ID | Priority | Status | Component | Description | File:Line | Shipped Date |
|---|---|---|---|---|---|---|
| FIX-01 | **P0** | **DONE** | Crawlability | Missing `robots.txt` preventing explicit crawler directives. Deployed with Sitemap pointer. | `www/robots.txt` | 2026-10-12 |
| FIX-02 | **P0** | **DONE** | Crawlability | Missing XML Sitemap for search engine indexation. Deployed 6-route sitemap. | `www/sitemap.xml` | 2026-10-12 |
| FIX-03 | **P0** | **DONE** | Telemetry | Missing Google Analytics 4 tracking. Deployed `gtag.js` engine. | `www/index.html:12` | 2026-10-12 |
| FIX-04 | **P0** | **DONE** | Conversions | Set GA4 event tracking for "Get in Touch" buttons across header, hero, footer. | `www/index.html:1630` | 2026-10-12 |
| FIX-05 | **P0** | **DONE** | Conversions | Set GA4 event tracking for "My Work" buttons across nav dropdown and hero. | `www/index.html:1644` | 2026-10-12 |
| FIX-06 | **P0** | **DONE** | Conversions | Set GA4 event tracking for both CV buttons (Hero & Credentials modal openers). | `www/index.html:1618` | 2026-10-12 |
| FIX-07 | **P1** | **DONE** | Structured Data | Added Schema.org `Person` & `ProfessionalService` JSON-LD graph. | `www/index.html:20` | 2026-10-12 |
| FIX-08 | **P1** | **IN PROGRESS**| GSC Verification | Deploy Search Console property and verify via meta tag / DNS record for Nomeshwer (`nomeshwer@ommnomi.in`). | `www/index.html:10` | 2026-10-12 |
| FIX-09 | **P2** | **OPEN** | Social Sharing | OpenGraph (`og:image`, `og:title`, `og:description`) and Twitter card meta tags for LinkedIn sharing preview. | `www/index.html:8` | Next Cycle |
| FIX-10 | **P2** | **OPEN** | Asset Compression | Optimize remaining PNG assets in `public/images/` to AVIF / WebP formats to shave ~300KB off total payload. | `public/images/` | Next Cycle |
