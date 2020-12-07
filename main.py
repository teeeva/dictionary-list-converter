#!/usr/bin/env python
#

# import modules used here -- sys is a very standard one
import sys, argparse, logging
from dictionary import my_dict, my_munged_dict
from translate import translate


# Gather our code in a main() function
def main(args, loglevel):
  logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)
  
  # TODO Replace this with your actual code.
  print ("Hello there.")
  logging.info("Started")
  logging.debug("Your Argument: %s" % args.input_string)

  inputdict = args.input_file


  while args.input_string: 

    if args.l337_dict == True:

      newstring = translate(args.input_string, my_dict)
      print(newstring)


    else: 

      newstring = translate(args.input_string, my_munged_dict)
      print(newstring)

    break

  while args.input_file:
    
    if args.l337_dict  == True:
        input_file = open(args.input_file)
        inputdict = input_file.read() 
        newfile = (input("Enter new file name:"))
        output_file = open(newfile,"x+")

        new_file = translate(inputdict, my_dict)
        output_file.write(new_file)
        break 

    else:
        input_file = open(args.input_file)
        inputdict = input_file.read() 
        newfile = (input("Enter new file name:"))
        output_file = open(newfile,"x+")

        new_file = translate(inputdict, my_munged_dict) 
        output_file.write(new_file)

        break 
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  parser = argparse.ArgumentParser( 
                                    description = "Convert dictionary to 1337 or munged passwords",
                                    epilog = "This application converts inputted strings or text files to munged characters or into 1337 speak.\n The output filename will be requested when running. If you input a large file it say take some time to complete. Modify dictionary.py to change the input characters to custom output characters"
                                    )
  # TODO Specify your real parameters here.
  parser.add_argument(  
                      "-s",
                      "--input_string",
                      type=str,
                      help="pass string into converter"
                      )
  parser.add_argument(
                      "-f",
                      "--input_file",
                      type=str,
                      help = "pass text file into program",
                      )
  parser.add_argument(
                      "-m",
                      "--munged_dict",
                      action="store_true",  
                      help='<Required> Select munged dictionary', 
                      )
  parser.add_argument(
                      "-1337",
                      "--l337_dict",
                      action="store_true",  
                      help='<Required> Select 1337 5p34k dictionary', 
                      )                    
  parser.add_argument(
                      "-v",
                      "--verbose",
                      help="increase output verbosity",
                      action="store_true")
  args = parser.parse_args()

  # Setup logging
  if args.verbose:
    loglevel = logging.DEBUG
  else:
    loglevel = logging.INFO
  
  main(args, loglevel)