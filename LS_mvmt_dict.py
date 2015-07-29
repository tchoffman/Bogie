ls_command = {}
for deg in range(180,-185,-5):
    ls_command[deg] = {"L":0,"R":0}
    if 0 <= deg <= 90:
        ls_command[deg]["R"] = 100
        ls_command[deg]["L"] = 100 * (45 - deg) / 45
    if 0 >= deg >= -90:
        ls_command[deg]["L"] = 100
        ls_command[deg]["R"] = 100 * (45 + deg) / 45

    
    print deg, ls_command[deg]
