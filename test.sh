# test.sh
#!/bin/bash

# clean output folder
#rm -r test_output || true

# convert the example notebook to a script
jupyter nbconvert --to script gons_test_cli.ipynb

# and disable Jupyter display handle output
sed -i -e 's/jupyter=True/jupyter=False/g' gons_test_cli.py

# run script
python gons_test_cli.py

# clean up
rm gons_test_cli.py
