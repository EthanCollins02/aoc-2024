def validateReport(report):
    if not (report == sorted(report) or report == sorted(report, reverse=True)) or len(set(report)) != len(report):
            return False
    else:
        invalidChange = False
        for x, num in enumerate(report):
            if x != len(report)-1:
                if abs(num-report[x+1]) > 3:
                    invalidChange = True
                    return False
        if invalidChange == False:
            return True

report = ""
safe = 0
while report is not None:
    try:
        report = [int(x) for x in input().split()]
        valid = validateReport(report)
        if not valid:
            for x in range(len(report)):
                new_report = report.copy()
                new_report.pop(x)
                valid = validateReport(new_report)
                if valid:
                    break
        if valid:
            safe += 1
            
    except:
        report = None
print(safe)

