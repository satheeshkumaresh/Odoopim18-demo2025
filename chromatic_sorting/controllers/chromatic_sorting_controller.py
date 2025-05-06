from odoo import http

class ChromaticSortingController(http.Controller):
    @http.route('/chromatic_sorting/sort', auth='public', website=True)
    def sort(self, **kw):
        # Implement any web interface functionality here if needed
        return "Chromatic Sorting"
