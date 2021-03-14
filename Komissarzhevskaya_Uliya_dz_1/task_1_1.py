duration = int(input('Duration(in sec): '))
duration_in_sec = duration % 60
duration_in_min = duration // 60  # 60 - количество секунд в 1-ой минуте
duration_in_hours = duration // 3600  # 3600 - количество секунд в 1 часе
duration_in_days = duration // 86400  # 86400 - количество секунд в 1-х сутках
if duration < 60:
    print(f'{duration} sec')
elif 60 <= duration < 3600:
    print(f'{duration_in_min} min {duration_in_sec} sec')
elif 3600 <= duration < 86400:
    duration_in_min = duration % 3600 // 60
    print(f'{duration_in_hours} hour(s) {duration_in_min} min {duration_in_sec} sec')
else:
    duration_in_hours = duration % 86400 // 3600
    duration_in_min = duration % 86400 % 3600 // 60
    print(f'{duration_in_days} day(s) {duration_in_hours} hour(s) {duration_in_min} min {duration_in_sec} sec')
