#Password List reformer 

Reforms existing passowrds lists with "munged" or 1337 charaters. 

##Examples 

Use the list provided or use the basic generator or 

Input| Output
------------ | -------------
Munged
passwordgenertor | p@$$2u0r693n3r+0r
13375p34k
passwordgenertor| |24zzw0rd63n3r70r 

edit the dictionary file to adjust the tolerance of character conversion. 

Please fork my repo or contribute to the repo to make it better.

includes simple list generator to generate keywords and dates

Will update with more refined options....
 

```python 
python main.py -h
usage: main.py [-h] [-s INPUT_STRING] [-f INPUT_FILE] [-m] [-1337] [-v]

Convert dictionary to 1337 or munged passwords

optional arguments:
  -h, --help            show this help message and exit
  -s INPUT_STRING, --input_string INPUT_STRING
                        pass string into converter
  -f INPUT_FILE, --input_file INPUT_FILE
                        pass text file into program
  -m, --munged_dict     <Required> Select munged dictionary
  -1337, --l337_dict    <Required> Select 1337 5p34k dictionary
  -v, --verbose         increase output verbosity

This application converts inputted strings or text files to munged characters
or into 1337 speak. The output filename will be requested when running. If you
input a large file it say take some time to complete. Modify dictionary.py to
change the input characters to custom output characters
```

