from odoo import models, fields, api, _ 

class Student(models.Model):
    _name= 'student.student'
    _description= 'Student'

    name= fields.Char(string="Student Name", requried= True)
    age= fields.Integer(string= "Age")
    course= fields.Char(string= "Course Name")
