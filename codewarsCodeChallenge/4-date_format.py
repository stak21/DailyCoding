# Start: 12/16/19 10:32 PM
#   Prep: 10:51 PM
#   Attempt: 11:15 PM
# Requirements:
#   Given a non negative integer
#   return a string with the date in human readable format
#   each component should have a comma and a space between and the last one should have an 'and'
#   
# I/O:
#   61 => 1 minute and 1 second
#   121 => 2 minutes and 1 second
#   6061 => 1 hour, 41 minutes and 1 second 
# Process:
#   Times_dict = {second: 1, minute: 60, hour: 3600, day: 3600*24, year: 3600*24*365 }
#   components = [0,0,0,0]
#   times = ['year', 'day', hours, minute', 'second']
#   iterate through times and use the dict to find the number to divide by 
#   find the remainder of time / year
#   store the dividend into an array
#   the array will use the index of the current times
#   do the same for the remaining
#   year / 60 => 60 // day / 60 => 60 // hour / 60 => 60 // minute / 60 => 0 store 1 minute
#   iterate through the components
#       if time > 1:
#           append an s 
#       return string

def format_duration(seconds):
    times_dict = {second: 1, minute: 60, hour: 3600, day: 3600*24, year: 3600*24*365 }
    components = [0,0,0,0, 0]
    times = ['year', 'day', 'hour', 'minute', 'second']
    formatted_time = ''
    for index, time in enuemrate(times):
        components[index] = seconds // times_dict[time] 
        seconds %= times_dict[time]
    if components[4] > 0:
        if components[4] > 1:
            times[4] += 's'
        formatted_time += '{} second'.format(components[4], times[4])
    if components[3] > 0:
        attatchment = 'and '
        formatted_time = attatchment + formatted_time
    for index in range(3, -1, -1):
        count = components[index]
        if  count == 0:
            continue
        if count > 1:
            times[index] += 's'
        formatted_time += '{} {}, '.format(count, times[index])
            