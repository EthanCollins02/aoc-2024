report = ""
safe = 0
unsafe = 0
while report is not None:
    try:
        report = [int(x) for x in input().split()]
        if not (report == sorted(report) or report == sorted(report, reverse=True)) or len(set(report)) != len(report):
            unsafe += 1
        else:
            invalidChange = False
            for x, num in enumerate(report):
                if x != len(report)-1:
                    if abs(num-report[x+1]) > 3:
                        invalidChange = True
                        unsafe +=1
                        break
            if invalidChange == False:
                safe += 1
            
    except:
        report = None
print(safe)

