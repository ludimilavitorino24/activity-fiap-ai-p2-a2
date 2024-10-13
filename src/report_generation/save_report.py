from pathlib import Path
from jinja2 import Template
from typings import ReportData
from config import reportOutDir, templatePath
from typing import List

def save_report(date: str, data: List[ReportData]):
    """
    Save the report to a file.

    Args:
        date (str): The date of the report in the format 'YYYY-MM-DD'.
        data (List[ReportData]): The data to include in the report.

    Returns:
        None
    """
    filename = f"daily_report_{date.replace('-', '')}.md"
    filepath = Path(reportOutDir) / filename

    with open(templatePath) as file_:
        template = Template(file_.read())

        content = template.render(
            date=date,
            species_list=data
        )

    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"Report saved to {filepath}")
