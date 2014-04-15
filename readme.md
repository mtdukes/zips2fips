#zips2fips
Simple script to read in a CSV with the column "full_address" and append FIPS codes with confidence scores to a new CSV.

##Requirements
To run zips2fips, you'll need to import the [Data Science Toolkit](http://www.datasciencetoolkit.org/developerdocs#street2coordinates).

```
pip install dstk
```

You'll also need an existing CSV with addresses in a column marked "full_address." The script will search for this column before running geolocation.

##Running it
Run zips2fips by passing in the path to your CSV as an argument.

```
python zips2fips.py SOURCE_DATA.csv
```
