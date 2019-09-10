import csv
# with open('E:/Downloads/4edb2a71-733b-406d-b207-9c0332aca30e.csv','rt')as f:
#   data = csv.reader(f)
#   with open('C:/Users/nagraju/Desktop/writeData1.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',', quotechar="'", quoting=csv.QUOTE_NONE)
#
#     for row in data:
#         #print(row)
#         writer.writerow(row)

with open('E:/Downloads/4edb2a71-733b-406d-b207-9c0332aca30e.csv','rt') as input, open('C:/Users/nagraju/Desktop/writeData1.csv', 'w', newline='') as output:
    writer = csv.writer(output,delimiter=',', quotechar='', quoting=csv.QUOTE_NONE)
    for row in csv.reader(input):
        if any(field.strip() for field in row):
            writer.writerow(row)
    input.close()
    output.close()