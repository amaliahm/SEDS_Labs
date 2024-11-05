import pytest
import csv

def row_2_list(s):
    return list(s.split())


dataset = []
with open('/home/mina/esi/tp/science de donnees/SEDS_Lab4/unit_test_lab/data/raw/housePrice.csv', 'r') as csvfile:  
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
    input_string = ' '.join(input_row)

    assert all(value != '' for value in input_row), "Missing value found in the row"

