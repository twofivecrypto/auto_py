import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)  # Matches the part before the date
    ((0|1)?\d)-                     # Matches the month
    ((0|1|2|3)?\d)-                 # Matches the day
    ((19|20)\d\d)                   # Matches the year
    (.*)$                           # Matches the part after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1) 
    monthPart = mo.group(2) 
    dayPart = mo.group(4) 
    yearPart = mo.group(6) 
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + '-' + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files
    print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))
    # Uncomment the line below after testing to perform the actual renaming.
    # shutil.move(amerFilename, euroFilename)
