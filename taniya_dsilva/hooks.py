app_name = "taniya_dsilva"
app_title = "Taniya Dsilva Portfolio"
app_publisher = "OmmNoMi Automation LLP"
app_description = "Strategic Social Impact Advisory Portfolio for Taniya D'silva"
app_email = "nomeshwer@ommnomi.in"
app_license = "mit"

# Default Home Page for the entire website
home_page = "index"

# Dynamic Domain / Host-based routing (same architecture as bumping_into_bugs)
before_request = ["taniya_dsilva.routing.set_home_page"]

# Route rules for standalone routes
website_route_rules = [
    {"from_route": "/design-3", "to_route": "index"},
    {"from_route": "/index", "to_route": "index"},
]
