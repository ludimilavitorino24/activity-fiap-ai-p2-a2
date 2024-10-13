from pathlib import Path
from jinja2 import Template
from typings import ReportData
from config import reportOutDir

def save_report(date: str, data: ReportData):
    """
    Save the report to a file.

    Args:
        date (str): The date of the report in the format 'YYYY-MM-DD'.
        data (ReportData): The report data to be saved.

    Returns:
        None
    """
    filename = f"daily_report_{date.replace('-', '')}.md"
    filepath = Path(reportOutDir) / filename

    with open(Path('assets') / 'template.jinja2.md') as file_:
        template = Template(file_.read())

        content = template.render(
            date=date,
            species_list=data
        )

    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"Report saved to {filepath}")
