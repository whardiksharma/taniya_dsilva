app_name = "taniya_dsilva"
app_title = "Taniya Dsilva Portfolio"
app_publisher = "OmmNoMi Automation LLP"
app_description = "Strategic Social Impact Advisory Portfolio for Taniya D'silva"
app_email = "info@ommnomi.in"
app_license = "mit"

# Dynamic Domain / Host-based routing (same architecture as bumping_into_bugs)
before_request = ["taniya_dsilva.routing.set_home_page"]

website_route_rules = [
    {"from_route": "/design-2", "to_route": "design-2"},
    {"from_route": "/design-3", "to_route": "design-3"},
    {"from_route": "/design-4", "to_route": "design-4"},
    {"from_route": "/work", "to_route": "work"},
    {"from_route": "/pillars", "to_route": "pillars"},
    {"from_route": "/ledger", "to_route": "ledger"},
    {"from_route": "/connect", "to_route": "connect"},
    {"from_route": "/about", "to_route": "about"},
    {"from_route": "/wise-impact", "to_route": "wise-impact"},
    {"from_route": "/what-others-say", "to_route": "what-others-say"},
    {"from_route": "/blog", "to_route": "blog"},
]
