def tellTime(hours, mins):
    if any ([hours < 1, hours > 12, mins < 0, mins > 60]):
        return "Check Time again"
    elif mins == 30:
        return "half past " + numsToWords(hours)
    elif mins == 0:
        return numsToWords(hours) + " o'clock"
    elif mins == 60:
        return numsToWords(hours+1) + " o'clock"
    elif mins == 15:
        return "quarter after " + numsToWords(hours)
    elif mins == 45:
        return "quarter to " + numsToWords(hours+1)
    elif 0 < mins < 30:
        return numsToWords(mins) + " minutes past " + numsToWords(hours)
    elif 30 < mins < 60:
        time = 60 - mins
        return numsToWords(time) + " minutes to " + numsToWords(hours+1)



num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
             19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
             50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
             90: 'ninety', 0: 'zero'}
