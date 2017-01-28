import csv

def sample_csv_file_with_fixedstep(filedir, filename, step, delimiter = ',', keepheader=True):

    with open(filedir+filename) as input_f:
        reader = csv.reader(input_f, delimiter = delimiter)

        with open(filedir + filename + '_' + str(step) + '.csv', 'wb') as output_f:
            out_writer = csv.writer(output_f, delimiter = delimiter, lineterminator='\r\n')

            if keepheader:
                header = reader.next()
                out_writer.writerow(header)
            else:
                reader.next()

            count = 0
            for i, row in enumerate(reader):
                count = count + 1
                if (count % step) == 0:
                    out_writer.writerow(row)

