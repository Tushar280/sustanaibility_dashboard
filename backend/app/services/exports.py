import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML
import pandas as pd
from datetime import datetime
from app.core.config import settings

templates = Environment(
    loader=FileSystemLoader(searchpath="app/templates"),
    autoescape=select_autoescape(["html", "xml"])
)

def export_pdf(report_name: str, context: dict) -> str:
    tpl = templates.get_template("report.html")
    html = tpl.render(**context)
    out_dir = settings.EXPORTS_DIR
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{report_name}_{datetime.utcnow().isoformat()}.pdf")
    HTML(string=html, base_url=settings.PDF_BASE_URL).write_pdf(out_path)
    return out_path

def export_rows_csv(report_name: str, rows: list[dict]) -> str:
    out_dir = settings.EXPORTS_DIR
    os.makedirs(out_dir, exist_ok=True)
    df = pd.DataFrame(rows)
    out_path = os.path.join(out_dir, f"{report_name}_{datetime.utcnow().isoformat()}.csv")
    df.to_csv(out_path, index=False)
    return out_path

def export_rows_excel(report_name: str, rows: list[dict]) -> str:
    out_dir = settings.EXPORTS_DIR
    os.makedirs(out_dir, exist_ok=True)
    df = pd.DataFrame(rows)
    out_path = os.path.join(out_dir, f"{report_name}_{datetime.utcnow().isoformat()}.xlsx")
    df.to_excel(out_path, index=False)
    return out_path
