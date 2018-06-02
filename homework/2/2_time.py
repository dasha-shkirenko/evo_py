# Даны числа h и m , где h - количество часов, m - количество минут некоторого момента времени.
# Найдите угол между часовой и минутной стрелками в этот момент времени.

hour = int(input('print hours: '))
minute = int(input('print minutes: '))

hour_arrow_speed = 360 / (12 * 60)
minute_arrow_speed = 360 / (1 * 60)

if hour > 12:
    hour -= 12
else:
    hour = hour

hour_arrow_angle = ((hour * 60) + minute) * hour_arrow_speed
minute_arrow_angle = minute * minute_arrow_speed

arrows_angle_v1 = abs(hour_arrow_angle - minute_arrow_angle)
arrows_angle_v2 = 360 - abs(hour_arrow_angle - minute_arrow_angle)

print('ANGLE BETWEEN ARROWS IS {}° OR {}°'.format(
    arrows_angle_v1, arrows_angle_v2
))


