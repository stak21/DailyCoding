# Success: 12/11 12:30 AM
# Notes:  Becareful about where your index is
#       Make sure you know what conditions are required before making a helper function.
# Requirements:
#   Given an array of integers, return an object with the properties - (pos, peaks)
#   The first and last elements do not count as peaks
#   becareful of plateau peaks, can be considered one huge peak. Return the first pos and peak
# I/O:
#   [121] => {pos: [1], peak:[2]}
#   [12] => {pos: [], peak:[]}
#   [] => {pos: [], peak:[]}
#   [12221] => {pos: [1], peak:[2]}
#   [121342] => {pos: [1, 4], peak:[2, 4]}
# Process:
#   Thoughts - Iterate through the entire array with three pointers
#           if the 2 pointer is greater than the 1st and 3rd, add the index of the middle points and the value
#           if it is a plataeu, then move the third pointer up until it hits either a higher peak or lower number, which in that case it is a peak and add the 2 pointer index
#           at the end of the plataeu, move the 1st pointer down to the end

def pick_peaks(arr):
    def check_plataeu(m, l, right, arr):
        for idx, val in enumerate(arr[right:]):
            if l < m > val:
                return (True, idx)
            if m < val or m > val:
                return (False, idx)
        return (False, idx)

    def add_peak(pos, peak, ret):
        ret['pos'].append(pos)
        ret['peaks'].append(peak)

    arr_len = len(arr)
    ret_peaks = {'pos':[], 'peaks':[]}
    if arr_len < 3:
        return ret_peaks
    left, middle, right = 0, 1, 2
    while(right < arr_len):
        l = arr[left]
        m = arr[middle]
        r = arr[right]
        if l < m > r:
            add_peak(middle, m, ret_peaks)
        if m == r:
            peak, idx = check_plataeu(m, l, right, arr)
            if peak:
                add_peak(middle, m, ret_peaks)
            left += idx
            middle += idx
            right += idx
            if right == arr_len - 1:
                return ret_peaks
            continue
        left += 1
        middle += 1
        right += 1
    return ret_peaks