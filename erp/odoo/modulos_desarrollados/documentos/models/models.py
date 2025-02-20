# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import PyPDF2
import io

class documentos(models.Model):
  _name = 'documentos.documentos'
  _description = 'documentos.documentos'

  file = fields.Binary(string="Sube tu archivo")
  file_name = fields.Char("Archivo")
  modified_file = fields.Binary(string="Archivo Modificado")
  descripcion_breve = fields.Text(string="Descripcion documento")


  def add_text_to_pdf(self, text="Texto agregado en Odoo"):
    if not self.file:
        return False

    pdf_data = io.BytesIO(base64.b64decode(self.file))
    reader = PyPDF2.PdfReader(pdf_data)
    writer = PyPDF2.PdfWriter()

    for page in reader.pages:
        page.merge_text(text, 100, 500)  # Posición X, Y
        writer.add_page(page)

    
    output_pdf = io.BytesIO()
    writer.write(output_pdf)
    output_pdf.seek(0)
    
    self.modified_file = base64.b64encode(output_pdf.read())  # Guardar archivo editado en Odoo
    return True