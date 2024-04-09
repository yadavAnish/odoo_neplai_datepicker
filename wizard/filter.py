from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
class SupportCallWizard(models.TransientModel):
    _name = 'support.call.wizard'

    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End Date")

    @api.multi
    def check_report(self):
        _logger.error("Inside check_report")
        data = {}
        data['form'] = self.read(['date_start', 'date_end'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        _logger.error("Inside _print_report")
        data['form'].update(self.read(['date_start', 'date_end'])[0])
        return self.env['report'].get_action(self, 'support_call.report_support_call', data=data)


class SupportCallReport(models.AbstractModel):
    _name = 'report.support_call.report_support_call'

    @api.model
    def _get_report_values(self, docids, data=None):
        _logger.error("Inside _get_report_values")
        date_start = data['form']['date_start']
        date_end = data['form']['date_end']
        support_calls = self.env['support.call'].search([('Date', '>=', date_start), ('Date', '<=', date_end)])

        return {
            'doc_ids': docids,
            'doc_model': 'support.call',
            'date_start': date_start,
            'date_end': date_end,
            'support_calls': support_calls,
        }

    @api.multi
    def render_html(self, docids, data=None):
        _logger.error("Inside render_html")
        report_obj = self.env['report']
        report_name = 'support_call.report_support_call_summary'
        docargs = {
            'doc_ids': docids,
            'doc_model': self._name,
            'docs': self._get_report_values(docids, data),
        }
        return report_obj.render(report_name, docargs)






