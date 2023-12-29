from datetime import datetime

def log_exception(ex, headless_mode, page, page_name):
    print(ex)
    date_time_str = datetime.now().strftime("%m-%d-%Y, %H-%M-%S")

    # Log error info
    with open('results\\report.txt', 'a') as report_file:
        report_file.write('============ ' + date_time_str + ' ============\n' + str(ex) + "\n\n")

    if not headless_mode:
        page.take_screenshot(f"results\{date_time_str}_{page_name}.png")