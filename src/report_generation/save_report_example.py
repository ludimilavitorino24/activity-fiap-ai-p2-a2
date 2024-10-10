from report_generation.save_report import save_report
report_data = [
        ReportData(
            "Dog",
            "Golden Retriever",
            3,
            25.0,
            30.0,
            20.0,
            100.0,
            33.33,
            50.0,
            10.0
        ),
        ReportData(
            "Cat",
            "Siamese",
            3,
            25.0,
            30.0,
            20.0,
            100.0,
            33.33,
            50.0,
            10.0
        )
    ]
save_report("24-10-09", report_data)