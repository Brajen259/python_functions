## Dtescription: A Python module that can create bins based on the bin size values passed.


## binning function
## Yet to modified
def bins4(percentage):
    if percentage <25.0:
        return 'Below 25%'
    elif percentage >=25.0 and percentage <50.0:
        return '25% - 50%'
    elif percentage >=50.0 and percentage <75.0:
        return '50% - 75%'
    elif percentage >=75.0 and percentage <100.0:
        return '75% - 100%'
    else:
        return 'Above 100%'