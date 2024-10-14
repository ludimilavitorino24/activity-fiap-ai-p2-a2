

# clear database
import clear_database
# generate-data
from generate_data import populate_db
populate_db()
# generate-report
from generate_report import generate_report

generate_report()