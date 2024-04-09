from odoo import models, fields

class MyTestModel(models.Model):
    _name = 'my.nepali.date.model'
    _description = 'My Test Model'

    nepali_date = fields.Char(string="Nepali Date")
    ad_date = fields.Date(string="Anno Domini Date")
    test_field=fields.Char(string="test filed ")



    # ad_date = fields.Date(string="Anno Domini Date", compute='_compute_ad_date', store=True)

    # def _compute_ad_date(self):
    #     for record in self:
    #         if record.nepali_date:
    #             # Convert Nepali date to Anno Domini (AD) date
    #             ad_date = self._convert_bs_to_ad(record.nepali_date)
    #             record.ad_date = ad_date
    #
    # def _convert_bs_to_ad(self, bs_date):
    #     # Perform the BS to AD conversion using nepali_datetime package
    #     nepali_date = nepali_datetime.date.from_string(bs_date)
    #     ad_date = nepali_date.to_datetime_date()
    #     return ad_date
