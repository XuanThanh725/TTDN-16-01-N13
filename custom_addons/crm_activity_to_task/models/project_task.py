from odoo import fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    x_crm_lead_id = fields.Many2one(
        "crm.lead",
        string="CRM Opportunity",
        ondelete="set null",
    )
