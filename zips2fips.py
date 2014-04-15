import dstk
import csv, argparse, re

def get_fips(csv_path):
	#initialize csv file
	with open(csv_path, 'r') as csv_input:
		#strip out directory, if it exists
		loc = re.sub(r'(^.*\/)','',csv_path)
		with open('fips_'+loc,'w') as csv_output:
			writer = csv.writer(csv_output)
			reader = csv.reader(csv_input)

			#initialize DSTK
			d = dstk.DSTK()

			#get location of full_address column
			row = reader.next()
			address_position = row.index('full_address')

			#add columns
			row.append('fips_county')
			row.append('confidence')
			writer.writerow(row)

			print row
			for item in reader:
				#clear out instances of suite, room, office, etc.
				clean_address = re.sub(r'(( SUITE.*?)|( ROOM.*?)|( OFFICE.*?)),',',',item[address_position])
				#find 'full_address' in CSV file
				raw = d.street2coordinates(clean_address)
				#raw = d.street2coordinates(item[address_position])
				print raw
				for r in raw:
					r_dict = raw[r]
					#add 'fips_county' to csv
					try:
						item.append(r_dict['fips_county'])
					except TypeError:
						item.append('')
					#add 'confidence' to csv
					try:
						item.append(str(r_dict['confidence']))
					except TypeError:
						item.append('')
					#fips_file.writerow([r,r_dict['fips_county'],str(r_dict['confidence'])])
				writer.writerow(item)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Convert full address to FIPS code. Eventually: CSV path')
	parser.add_argument('path',help='Enter the full address')
	args = parser.parse_args()

	get_fips(args.path)