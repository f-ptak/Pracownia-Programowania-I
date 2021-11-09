def disp_month(d):
    year = ("January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December")
    return year[d-1]


print(disp_month(7))