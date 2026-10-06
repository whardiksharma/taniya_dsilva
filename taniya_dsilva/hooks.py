app_name = "taniya_dsilva"
app_title = "Taniya Dsilva Portfolio"
app_publisher = "OmmNoMi Automation LLP"
app_description = "Strategic Social Impact Advisory Portfolio for Taniya D'silva"
app_email = "info@ommnomi.in"
app_license = "mit"

# Dynamic Domain / Host-based routing (same architecture as bumping_into_bugs)
before_request = ["taniya_dsilva.routing.set_home_page"]

website_route_rules = [
    {"from_route": "/monograph", "to_route": "designs/design-1-editorial-monograph"},
    {"from_route": "/nordic", "to_route": "designs/design-2-nordic-warm-minimal"},
    {"from_route": "/bento", "to_route": "designs/design-3-evidence-bento"},
    {"from_route": "/swiss", "to_route": "designs/design-4-swiss-high-grid"},
    {"from_route": "/split-canvas", "to_route": "designs/design-5-split-canvas"},
    {"from_route": "/dossier", "to_route": "designs/design-6-strategic-dossier"},
]
