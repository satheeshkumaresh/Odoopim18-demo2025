from odoo import models, fields, api
import colorsys

class ChromaticSorting(models.Model):
    _name = 'chromatic.sorting'
    _description = 'Chromatic Sorting'

    name = fields.Char(string='Name', required=True)
    color_ids = fields.One2many('chromatic.color', 'sorting_id', string='Colors')
    sorted_color_ids = fields.One2many('chromatic.color', 'sorted_sorting_id', string='Sorted Colors', readonly=True)

    def sort_colors(self):
        for record in self:
            colors_rgb = [(color.red, color.green, color.blue) for color in record.color_ids]
            colors_hsv = [colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0) for r, g, b in colors_rgb]
            sorted_colors_hsv = sorted(colors_hsv, key=lambda x: (x[0], x[1], x[2]))
            sorted_colors_rgb = [colorsys.hsv_to_rgb(h, s, v) for h, s, v in sorted_colors_hsv]
            sorted_colors_rgb = [(round(r*255), round(g*255), round(b*255)) for r, g, b in sorted_colors_rgb]

            # Clear existing sorted colors
            record.sorted_color_ids.unlink()
            # Create new sorted colors
            for r, g, b in sorted_colors_rgb:
                color_name = self.env['chromatic.color'].search([('red', '=', r),
                                                                 ('green', '=', g), ('blue', '=', b)], order="id", limit=1).color_name
                self.env['chromatic.color'].create({
                    'color_name':color_name,
                    'red': r,
                    'green': g,
                    'blue': b,
                    'sorted_sorting_id': record.id,
                })

class ChromaticColor(models.Model):
    _name = 'chromatic.color'
    _description = 'Chromatic Color'

    red = fields.Integer(string='R', required=True)
    green = fields.Integer(string='G', required=True)
    blue = fields.Integer(string='B', required=True)
    color = fields.Char(compute='compute_color')
    color_name = fields.Char()

    sorting_id = fields.Many2one('chromatic.sorting', string='Sorting')
    sorted_sorting_id = fields.Many2one('chromatic.sorting', string='Sorted Sorting', readonly=True)

    def compute_color(self):
        for rec in self:
            rec.color = '#{:02x}{:02x}{:02x}'.format(rec.red, rec.green, rec.blue)
            print(rec.color)
