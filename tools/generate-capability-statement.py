from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "publications" / "africa-rising-investments-capability-statement.pdf"
SYSTEM_FONT_DIR = Path("C:/Windows/Fonts")

W, H = A4
FOREST = HexColor("#123C32")
DEEP = HexColor("#082820")
GOLD = HexColor("#C4A35A")
IVORY = HexColor("#F5F1E8")
WHITE = HexColor("#FFFFFF")
INK = HexColor("#1A2823")
MUTED = HexColor("#56645E")
RULE = HexColor("#D8D3C7")


def register_fonts():
    # The website fonts are WOFF2 files, which ReportLab cannot embed directly.
    # Arial provides a stable local sans-serif fallback for the downloadable PDF.
    pdfmetrics.registerFont(TTFont("Manrope", SYSTEM_FONT_DIR / "arial.ttf"))
    pdfmetrics.registerFont(TTFont("ManropeBold", SYSTEM_FONT_DIR / "arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("DMSans", SYSTEM_FONT_DIR / "arial.ttf"))
    pdfmetrics.registerFont(TTFont("DMSansMedium", SYSTEM_FONT_DIR / "arialbd.ttf"))


def draw_mark(c, x, y, scale=1.0, light=False):
    c.saveState()
    c.translate(x, y)
    c.scale(scale, scale)
    c.setFillColor(WHITE if light else FOREST)
    p = c.beginPath()
    p.moveTo(32, 5)
    p.lineTo(55, 57)
    p.lineTo(44.4, 57)
    p.lineTo(32, 27.5)
    p.lineTo(19.6, 57)
    p.lineTo(9, 57)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(GOLD)
    p = c.beginPath()
    p.moveTo(16, 44)
    p.lineTo(54, 38.5)
    p.lineTo(58, 41.6)
    p.lineTo(54, 44.7)
    p.lineTo(16, 50.5)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


def brand(c, x, y, light=False):
    draw_mark(c, x, y - 17, 0.55, light)
    c.setFillColor(WHITE if light else FOREST)
    c.setFont("ManropeBold", 15)
    c.drawString(x + 43, y + 7, "AFRICA RISING")
    c.setFillColor(GOLD if light else MUTED)
    c.setFont("DMSansMedium", 6.8)
    c.drawString(x + 44, y - 4, "I N V E S T M E N T S")


def para(c, text, x, y, width, style):
    p = Paragraph(text, style)
    _, height = p.wrap(width, H)
    p.drawOn(c, x, y - height)
    return y - height


def label(c, text, x, y, color=GOLD):
    c.setFillColor(color)
    c.setFont("DMSansMedium", 7.2)
    c.drawString(x, y, text.upper())


def footer(c, page):
    c.setStrokeColor(RULE)
    c.setLineWidth(0.5)
    c.line(18 * mm, 15 * mm, W - 18 * mm, 15 * mm)
    c.setFont("DMSans", 7)
    c.setFillColor(MUTED)
    c.drawString(18 * mm, 10.5 * mm, "Africa Rising Investments · Capability statement · 29 August 2026")
    c.drawRightString(W - 18 * mm, 10.5 * mm, str(page))


def page_one(c, body, small, h2, card_head):
    c.setFillColor(DEEP)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    brand(c, 18 * mm, H - 22 * mm, light=True)
    label(c, "Capability statement", 18 * mm, H - 52 * mm)
    y = para(
        c,
        "Turning African opportunity into <font color='#C4A35A'>investable strategy.</font>",
        18 * mm,
        H - 61 * mm,
        155 * mm,
        ParagraphStyle("hero", parent=h2, fontSize=27, leading=31, textColor=WHITE),
    )
    y = para(
        c,
        "Africa-focused investment advisory for investors, companies, governments and development partners. We clarify market opportunity, map the institutions a decision depends on, identify credible partners and support practical execution.",
        18 * mm,
        y - 8 * mm,
        154 * mm,
        ParagraphStyle("intro", parent=body, fontSize=11.2, leading=16, textColor=IVORY),
    )

    c.setFillColor(IVORY)
    c.roundRect(18 * mm, 89 * mm, 174 * mm, 77 * mm, 2 * mm, fill=1, stroke=0)
    label(c, "Our working method", 25 * mm, 154 * mm, FOREST)
    c.setFillColor(INK)
    c.setFont("ManropeBold", 15)
    c.drawString(25 * mm, 144 * mm, "Four lenses, applied in order.")

    lenses = [
        ("01", "Market", "Is the opportunity real?", "Demand, competition, costs and commercial logic."),
        ("02", "Institutions", "Who has to say yes?", "Approvals, incentives, regulators and promotion channels."),
        ("03", "Partners", "Who do you need beside you?", "Operators, public counterparts, financiers and associations."),
        ("04", "Execution", "What actually gets it built?", "Sequencing, land, permits, people and practical delivery."),
    ]
    x_positions = [25, 67.5, 110, 152.5]
    for (num, title, question, detail), x_mm in zip(lenses, x_positions):
        x = x_mm * mm
        c.setFillColor(GOLD)
        c.setFont("ManropeBold", 11)
        c.drawString(x, 131 * mm, num)
        c.setFillColor(FOREST)
        c.setFont("ManropeBold", 9)
        c.drawString(x, 123 * mm, title)
        para(c, f"<b>{question}</b><br/>{detail}", x, 117 * mm, 35 * mm, small)

    label(c, "Advisory services", 18 * mm, 75 * mm)
    c.setFillColor(WHITE)
    c.setFont("ManropeBold", 15)
    c.drawString(18 * mm, 65 * mm, "Built around the decision in front of you.")
    services = [
        "Investment strategy and opportunity assessment",
        "Market intelligence and sector research",
        "Market-entry strategy",
        "Investor facilitation",
        "Investment-climate reform",
        "Policy and institutional advisory",
        "Partnership and stakeholder alignment",
        "Rapporteur, moderation and conference services",
    ]
    for i, service in enumerate(services):
        col = i // 4
        row = i % 4
        x = (18 + col * 88) * mm
        y0 = (53 - row * 9.1) * mm
        c.setFillColor(GOLD)
        c.circle(x + 1.5 * mm, y0 + 1.2 * mm, 1.2 * mm, fill=1, stroke=0)
        c.setFillColor(IVORY)
        c.setFont("DMSans", 8.3)
        c.drawString(x + 5 * mm, y0, service)
    footer(c, 1)


def page_two(c, body, small, h2, card_head):
    c.setFillColor(IVORY)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    brand(c, 18 * mm, H - 22 * mm)
    label(c, "Regional depth", 18 * mm, H - 49 * mm, FOREST)
    c.setFillColor(INK)
    c.setFont("ManropeBold", 20)
    c.drawString(18 * mm, H - 61 * mm, "East Africa at the core. Africa in view.")
    para(
        c,
        "The practice is grounded in East African markets and the institutions that shape investment across the region. Continent-wide comparisons are taken on where regional choice is the decision.",
        18 * mm,
        H - 70 * mm,
        172 * mm,
        body,
    )

    sectors = ["Agriculture & agro-processing", "Infrastructure", "Energy", "Manufacturing", "Tourism & hospitality", "Trade & financial services"]
    c.setFillColor(WHITE)
    c.roundRect(18 * mm, 174 * mm, 174 * mm, 40 * mm, 2 * mm, fill=1, stroke=0)
    label(c, "Sector perspectives", 25 * mm, 204 * mm, GOLD)
    for i, sector in enumerate(sectors):
        col = i % 3
        row = i // 3
        x = (25 + col * 55) * mm
        y = (192 - row * 10) * mm
        c.setFillColor(FOREST)
        c.setFont("DMSansMedium", 8.2)
        c.drawString(x, y, sector)

    label(c, "Lead consultant", 18 * mm, 160 * mm, FOREST)
    c.setFillColor(INK)
    c.setFont("ManropeBold", 16)
    c.drawString(18 * mm, 150 * mm, "Robert Bwire")
    para(
        c,
        "An investment strategist and researcher whose work sits where market opportunity meets the institutions that govern it. Robert previously served as Head of Strategy and Research at the Kenya Investment Authority.",
        18 * mm,
        143 * mm,
        92 * mm,
        body,
    )

    c.setFillColor(FOREST)
    c.roundRect(119 * mm, 126 * mm, 73 * mm, 39 * mm, 2 * mm, fill=1, stroke=0)
    label(c, "Engagement formats", 126 * mm, 154 * mm)
    para(
        c,
        "A focused research question<br/>A defined advisory assignment<br/>A sustained advisory relationship<br/>An institutional or conference brief",
        126 * mm,
        146 * mm,
        58 * mm,
        ParagraphStyle("white-list", parent=small, textColor=WHITE, leading=13),
    )

    label(c, "Selected experience", 18 * mm, 113 * mm, FOREST)
    experiences = [
        ("COMESA Regional Investment Agency", "Rapporteur for the National Investment Promotion Agencies Annual Meeting, Nairobi, 22-23 March 2022."),
        ("Renaissance Development Advisors / DFID BERF", "Consulting services connected to programmes designed to initiate, improve and scale investment-climate reform."),
        ("Kenya Investment Authority", "Former Head of Strategy and Research, bringing national investment-promotion experience to commercial advisory work."),
    ]
    y = 104 * mm
    for title, desc in experiences:
        c.setFillColor(WHITE)
        c.roundRect(18 * mm, y - 17 * mm, 174 * mm, 14 * mm, 1.5 * mm, fill=1, stroke=0)
        c.setFillColor(FOREST)
        c.setFont("ManropeBold", 8.7)
        c.drawString(23 * mm, y - 7.5 * mm, title)
        para(c, desc, 23 * mm, y - 10 * mm, 160 * mm, small)
        y -= 17 * mm

    c.setFillColor(DEEP)
    c.roundRect(18 * mm, 23 * mm, 174 * mm, 27 * mm, 2 * mm, fill=1, stroke=0)
    label(c, "Start a conversation", 25 * mm, 41 * mm)
    c.setFillColor(WHITE)
    c.setFont("ManropeBold", 10)
    c.drawString(25 * mm, 32 * mm, "africa@africa.or.ke")
    c.setFont("DMSans", 8)
    c.drawRightString(184 * mm, 32 * mm, "Nairobi, Kenya  ·  africarisinginvestment.com")
    footer(c, 2)


def main():
    register_fonts()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    body = ParagraphStyle("body", fontName="DMSans", fontSize=9, leading=13, textColor=INK, alignment=TA_LEFT)
    small = ParagraphStyle("small", parent=body, fontSize=7.3, leading=9.7, textColor=MUTED)
    h2 = ParagraphStyle("h2", fontName="ManropeBold", fontSize=19, leading=23, textColor=INK)
    card_head = ParagraphStyle("card-head", fontName="ManropeBold", fontSize=9, leading=11, textColor=FOREST)

    c = Canvas(str(OUT), pagesize=A4, pageCompression=1)
    c.setTitle("Africa Rising Investments - Capability Statement")
    c.setAuthor("Africa Rising Investments")
    c.setSubject("Investment advisory capability statement")
    page_one(c, body, small, h2, card_head)
    c.showPage()
    page_two(c, body, small, h2, card_head)
    c.showPage()
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
