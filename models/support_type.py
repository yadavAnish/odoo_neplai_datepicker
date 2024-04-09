# -*- coding: utf-8 -*- 
from odoo import models, fields ,api
from datetime import datetime 


class supporttype(models.Model): 
    _name = "support.type"
    _description = 'Type of support'
    _rec_name='remarks'
    remarks = fields.Char('Support Type', required=True)

@api.multi
def name_get(self):
    result = []
    for record in self:
        record_name = record.remarks
        result.append((record.id, record_name))
    return result
    
@api.model
def name_search(self, name, args=None, operator='ilike', limit=100):
    args = args or []
    recs = self.search([('remarks', operator, name)] + args, limit=limit)
    return recs.name_get()
