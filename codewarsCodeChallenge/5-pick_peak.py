In this kata, you will write a function that returns the positions and the values of the "peaks" (or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] does not. In case of a plateau-peak, please only return the position and value of the beginning of the plateau. For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)

Have fun!

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

def pick_peak(arr):
    def check_plataeu(m, right, arr):
        for idx, val in enumerate(arr[right:]):
            if val < m:
                return (True, idx)
            if val > m:
                return (False, idx)
        return (False, idx)

    def add_peak(pos, peak, ret):
        ret['pos'].append(pos)
        ret['peaks'].append(peak)

    arr_len = len(arr)
    ret_peaks = {pos:[], peaks:[]}
    if arr_len < 3:
        return ret_peaks
    left, middle, right = 0, 1, 2
    while(right <= arr_len):
    l = arr[left]
    m = arr[middle]
    r = arr[right]
    if l < m > r:
        add_peak(middle, m, ret_peaks)
    if m == r:
        peak, idx = check_plataeu(m, right, arr)
        if peak:
            add_peak(middle, m, ret_peaks)
        left = idx
        middle = idx + 1
        right = idx + 2
        continue
    left += 1
    middle += 1
    right += 1




        
