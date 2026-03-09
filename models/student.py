from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Student(models.Model):
    _name = "student.student"
    _description = "Student"
    _order = "name"

    name = fields.Char(string="Student Name", required=True)
    student_code = fields.Char(string="Student Code", readonly=True, copy=False, default="New")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date of Birth")
    course = fields.Char(string="Course Name", required=True)
    email = fields.Char(string="Email")
    guardian_name = fields.Char(string="Guardian Name")
    guardian_phone = fields.Char(string="Guardian Phone")
    enrollment_date = fields.Date(string="Enrollment Date", default=fields.Date.context_today)
    attendance = fields.Float(string="Attendance (%)", digits=(5, 2), default=0.0)
    marks = fields.Float(string="Marks", digits=(5, 2), default=0.0)
    gpa = fields.Float(string="GPA", compute="_compute_gpa", store=True, digits=(2, 2))
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("enrolled", "Enrolled"),
            ("graduated", "Graduated"),
            ("inactive", "Inactive"),
        ],
        string="Status",
        default="draft",
    )
    partner_id = fields.Many2one("res.partner", string="Related Contact")

    _sql_constraints = [
        ("student_code_uniq", "unique(student_code)", "Student code must be unique."),
    ]

    @api.depends("marks")
    def _compute_gpa(self):
        for student in self:
            score = min(max(student.marks, 0), 100)
            student.gpa = round((score / 100) * 4, 2)

    @api.constrains("attendance")
    def _check_attendance(self):
        for student in self:
            if student.attendance < 0 or student.attendance > 100:
                raise ValidationError(_("Attendance must be between 0 and 100."))

    @api.constrains("marks")
    def _check_marks(self):
        for student in self:
            if student.marks < 0 or student.marks > 100:
                raise ValidationError(_("Marks must be between 0 and 100."))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("student_code", "New") == "New":
                vals["student_code"] = self.env["ir.sequence"].next_by_code("student.student") or "New"
        return super().create(vals_list)

    def action_enroll(self):
        self.write({"state": "enrolled"})

    def action_graduate(self):
        self.write({"state": "graduated"})

    def action_set_inactive(self):
        self.write({"state": "inactive"})

    def action_reset_to_draft(self):
        self.write({"state": "draft"})
