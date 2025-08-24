from fastapi import APIRouter, Response
from app.services.exports import export_pdf, export_rows_csv, export_rows_excel

router = APIRouter(prefix="/exports", tags=["exports"])

@router.post("/pdf")
def export_pdf_endpoint(name: str, context: dict):
    path = export_pdf(name, context)
    with open(path, "rb") as f:
        data = f.read()
    return Response(content=data, media_type="application/pdf", headers={
        "Content-Disposition": f'attachment; filename="{name}.pdf"'
    })

@router.post("/csv")
def export_csv_endpoint(name: str, rows: list[dict]):
    path = export_rows_csv(name, rows)
    with open(path, "rb") as f:
        data = f.read()
    return Response(content=data, media_type="text/csv",
                    headers={"Content-Disposition": f'attachment; filename="{name}.csv"'})

@router.post("/excel")
def export_excel_endpoint(name: str, rows: list[dict]):
    path = export_rows_excel(name, rows)
    with open(path, "rb") as f:
        data = f.read()
    return Response(content=data, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers={"Content-Disposition": f'attachment; filename="{name}.xlsx"'})
