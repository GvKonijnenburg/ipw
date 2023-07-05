import logging
import parse_input

if __name__ == "__main__":
   logging.basicConfig(filename = 'log.txt', level = logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
   cases = parse_input.main()
   print('done')
   
