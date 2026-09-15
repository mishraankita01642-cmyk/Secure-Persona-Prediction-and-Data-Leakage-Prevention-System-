from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
def generate_report(
    customer_id,
    income,
    spending_score,
    persona,
    reason,
    recommendations
):
    filename = f"reports/{customer_id}_persona_report.pdf"
    document = SimpleDocTemplate(
        filename,
        pagesize=A4
    )
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]
    content = []
    content.append(
        Paragraph(
            "CUSTOMER PERSONA REPORT",
            title_style
        )
    )
    content.append(Spacer(1, 20))
    content.append(
        Paragraph(
            "Customer Information",
            heading_style
        )
    )
    content.append(
        Paragraph(
            f"Customer ID: {customer_id}",
            normal_style
        )
    )
    content.append(
        Paragraph(
            f"Income: Rs. {income:,.0f}",
            normal_style
        )
    )
    content.append(
        Paragraph(
            f"Spending Score: {spending_score}",
            normal_style
        )
    )
    content.append(Spacer(1, 15))
    content.append(
        Paragraph(
            "Predicted Persona",
            heading_style
        )
    )
    content.append(
        Paragraph(
            persona,
            normal_style
        )
    )
    content.append(Spacer(1, 15))
    content.append(
        Paragraph(
            "Why this persona?",
            heading_style
        )
    )
    content.append(
        Paragraph(
            reason,
            normal_style
        )
    )
    content.append(Spacer(1, 15))
    content.append(
        Paragraph(
            "Recommended Actions",
            heading_style
        )
    )
    for recommendation in recommendations:
        content.append(
            Paragraph(
                f"- {recommendation}",
                normal_style
            )
        )
        content.append(Spacer(1, 5))
    document.build(content)
    return filename