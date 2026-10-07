import frappe

def set_home_page():
	"""Pick the homepage per request based on the Host header, driven by
	Taniya Portfolio Settings or host matching.
	Mirrors the Bumping Into Bugs multi-tenant pattern on Frappe Cloud / ommnomi.in.
	"""
	request = getattr(frappe.local, "request", None)
	if not request or frappe.session.user != "Guest":
		return

	host = (request.host or "").lower()
	if "taniyadsilva" in host or "biz-taniya" in host or "taniya.ommnomi" in host:
		frappe.local.flags.home_page = "index"
		return

	try:
		settings = frappe.get_cached_doc("Taniya Portfolio Settings")
		if not settings.enabled:
			return

		domain = (settings.landing_domain or "").lower()
		if domain and domain in host:
			frappe.local.flags.home_page = settings.landing_route or "index"
	except Exception:
		pass
