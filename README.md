# Data Transformation

This is a collection of scripts and sample data used to transform data from and
into different structres and formats.

## data

This directory has a set of example data, there is nothing particular about
these examples, except that they work well the scripts in this repository.

## scripts

This directory contains a set of example scripts that transform data, in this
case from the `data` directory, into JSON format that
[Tidal Tools](https://get.tidal.sh) accepts.


## Examples

You can checkout `example.sh` for a quick set of commands to get you started.

An example command would be:

`cat ./data/apps.csv | ./scripts/csv_transform.rb | tidal sync apps`

This reads the data file, transforms it via script, and sends the data to the
[Tidal Migrations Platform](https://tidalmigrations.com/product).

You could also do:

`./cat ./data/apps.csv | ./scripts/csv_transform.rb`

or

`./cat ./data/apps.csv | ./scripts/csv_transform.rb | jq .`

Which reads the data from the file, transforms it and displays it for you to
inspect. Optionally you can use [jq](https://stedolan.github.io/jq/) to pretty
print the JSON data.


## Questions or Help

If you have any issues with the data or code you can create an issue here in
the repository.

If your issue isn't related directly to the code or data; feel free to
email us at info@tidalmigrations.com.
