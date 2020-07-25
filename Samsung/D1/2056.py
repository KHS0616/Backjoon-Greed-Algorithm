# 연월일 달력
def cal_date(date):
    yyyy = date[0:4]
    mm = date[4:6]
    dd = date[6:]
    if mm not in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
        return -1
    if mm in ["01", "03", "05", "07", "08", "10", "12"] and int(dd) not in list(range(0, 32, 1)):
        return -1
    if mm in ["04", "06", "09", "10"] and int(dd) not in list(range(0, 31, 1)):
        return -1
    if mm == "02" and int(dd) not in list(range(0, 29, 1)):
        return -1
    return "{}/{}/{}".format(yyyy, mm, dd)

T = int(input())
for test_case in range(1, T + 1):
	print("#{} {}".format(test_case, cal_date(input())))
    