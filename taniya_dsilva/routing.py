import frappe

def set_home_page():
	"""Pick the homepage per request based on the Host header.
	Mirrors the Bumping Into Bugs multi-tenant pattern on Frappe Cloud / ommnomi.in.
	"""
	request = getattr(frappe.local, "request", None)
	if not request or frappe.session.user != "Guest":
		return

	host = (request.host or "").lower()
	# Check if incoming host is taniyadsilva or dedicated subdomain
	if "taniyadsilva" in host or "taniya.ommnomi" in host:
		frappe.local.flags.home_page = "index"
		return
