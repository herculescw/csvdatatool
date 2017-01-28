from csvsampling import sample_csv_file_with_fixedstep

#replace your own path
file_dir = ''
filename = 'TWM_HaysTravisWilco_addresses_sorted.csv'

if __name__ == '__main__':
    sample_csv_file_with_fixedstep(filedir=file_dir, filename=filename, step=3)
    sample_csv_file_with_fixedstep(filedir=file_dir, filename=filename, step=6)
    sample_csv_file_with_fixedstep(filedir=file_dir, filename=filename, step=12)