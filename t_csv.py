import csv

with open('eggs.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # csvwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    # csvwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    for i in range(0, 10):
        csvwriter.writerow(['fds', 'dfds', 'gfd'])