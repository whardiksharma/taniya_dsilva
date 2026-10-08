app_name = "taniya_dsilva"
app_title = "Taniya Dsilva Portfolio"
app_publisher = "OmmNoMi Automation LLP"
app_description = "Strategic Social Impact Advisory Portfolio for Taniya D'silva"
app_email = "info@ommnomi.in"
app_license = "mit"

# Dynamic Domain / Host-based routing (same architecture as bumping_into_bugs)
before_request = ["taniya_dsilva.routing.set_home_page"]

# Route rules for standalone routes if needed
website_route_rules = [
    {"from_route": "/design-3", "to_route": "design-3"},
]
