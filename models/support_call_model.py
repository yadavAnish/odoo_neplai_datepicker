# -*- coding: utf-8 -*- 
from odoo import models, fields ,api
from datetime import datetime 
class supportCall(models.Model): 
    _name = "support.call"
    _description = 'Support Call Record'
    Caller = fields.Char('Caller Phone', required=True)
    Caller_name=fields.Char('Caller Name', required=True) 
    Date=fields.Date('Date')
    Duration=fields.Char('Time Duration')
    Site = fields.Many2one('call.site','Site Served', ondelete='set null',index=True, tracking=True, required=True)
    Remarks = fields.Many2one('support.type','Support Type',ondelete='set null',index=True, tracking=True, required=True) 
    current_user = fields.Many2one('res.users','Resolved By', default=lambda self: self.env.user)
    active=fields.Boolean("Active", default=True) 

