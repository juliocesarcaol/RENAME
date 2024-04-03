import csv

# Function to parse the last column of each row
def parse_identifier(filename):
    parsed_columns = []
    with open(filename, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            identifier = f"{row[-1]}_{row[-3]}"  # Accessing the last element of the row
            parsed_columns.append(identifier)
    return parsed_columns


def find_matching_identifiers_with_values(fasta_file, tsv_identifiers, tsv_file):
    matching_identifiers_with_values = {}
    with open(fasta_file, 'r') as fastafile:
        for line in fastafile:
            if line.startswith('>'):  # Check if it's a header line
                fasta_id = line.strip()[1:]  # Extract the relevant part of the identifier
                for identifier in tsv_identifiers:
                    if fasta_id.startswith(identifier):
                        with open(tsv_file, 'r') as tsvfile:
                            reader = csv.reader(tsvfile, delimiter='\t')
                            for row in reader:
                                if identifier == f"{row[-1]}_{row[-3]}":
                                    new_identifier = f"{row[-6]}_{row[-4]}"
                                    matching_identifiers_with_values[fasta_id] = new_identifier  # Correctly map old identifier to new identifier
                                    break
                        break  # Once a match is found, no need to continue searching
    return matching_identifiers_with_values

def write_new_fasta(fasta_file, matching_identifiers, tsv_file):
    new_fasta_file = fasta_file.replace('.fasta', '_new.fasta')  # New file name
    with open(new_fasta_file, 'w') as new_fasta:
        with open(fasta_file, 'r') as fasta:
            for line in fasta:
                if line.startswith('>'):
                    fasta_id = line.strip()[1:]
                    if fasta_id in matching_identifiers:
                        new_id = matching_identifiers[fasta_id]
                        new_fasta.write(f'>{new_id}\n')  # Write the modified identifier
                    else:
                        new_fasta.write(line)
                else:
                    new_fasta.write(line)


# Path to your TSV file

tsv_file = input("Enter TSV file path: \n")
fasta_file = input("Enter fasta file path: \n")

# Parse the last column of each row
parsed_columns = parse_identifier(tsv_file)

# Print the parsed columns
for column in parsed_columns:
    print(column)

tsv_identifiers = parse_identifier(tsv_file)

# Find matching identifiers in the FASTA file
matching_identifiers = find_matching_identifiers_with_values(fasta_file, tsv_identifiers, tsv_file)

# Print the matching identifiers
print("Matching Identifiers:")
for identifier in matching_identifiers:
    print(identifier)  

# Call the function to write the new FASTA file
write_new_fasta(fasta_file, matching_identifiers, tsv_file)

print("Matching Identifiers:")
for old_identifier, new_identifier in matching_identifiers.items():
    print(f"{old_identifier} -> {new_identifier}")