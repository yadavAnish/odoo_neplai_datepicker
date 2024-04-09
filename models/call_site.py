# -*- coding: utf-8 -*- 
from odoo import models, fields ,api
import logging


class callsite(models.Model): 
    _name = "call.site"
    _description = 'Call support for site'
    _rec_name='Site'
    Site = fields.Char('Affected Site', required=True)

@api.multi
def name_get(self):
    print("test")
    result = []
    for record in self:
        record_name = record.Site
        result.append((record.id, record_name))
    return result
    
@api.model
def name_search(self, name, args=None, operator='ilike', limit=100):
    args = args or []
    recs = self.search([('Site', operator, name)] + args, limit=limit)
    return recs.name_get()
