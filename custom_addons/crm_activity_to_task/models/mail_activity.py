from odoo import api, models, _


class MailActivity(models.Model):
    _inherit = "mail.activity"

    @api.model_create_multi
    def create(self, vals_list):
        activities = super().create(vals_list)

        for act in activities:
            # Chỉ xử lý Activity gắn với CRM Opportunity
            if act.res_model != "crm.lead" or not act.res_id:
                continue

            lead = self.env["crm.lead"].browse(act.res_id)
            if not lead.exists():
                continue

            # Tìm hoặc tạo Project CRM Follow-up
            project = self.env["project.project"].search(
                [("name", "=", "CRM Follow-up")],
                limit=1
            )
            if not project:
                project = self.env["project.project"].create({
                    "name": "CRM Follow-up"
                })

            # Tên task
            activity_type = act.activity_type_id.display_name or _("Activity")
            title = f"[{activity_type}] {lead.name}"

            # User được giao task (Odoo 15 dùng user_ids)
            user_id = act.user_id.id or self.env.user.id

            # Nội dung task
            description_lines = []
            if act.summary:
                description_lines.append(f"Summary: {act.summary}")
            if act.note:
                description_lines.append("")
                description_lines.append("Notes:")
                description_lines.append(act.note)

            description = "\n".join(description_lines)

            # Tạo task trong Project
            self.env["project.task"].create({
                "name": title,
                "project_id": project.id,
                "user_ids": [(6, 0, [user_id])],
                "partner_id": lead.partner_id.id if lead.partner_id else False,
                "description": description,
                "x_crm_lead_id": lead.id,
            })

        return activities
