import csv

request = ""

with open('money2-1.csv', 'r') as csvfile:
    i = 0
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        request += "begin;\nINSERT INTO transactions" \
        " (amount, from_bucket, to_bucket, comment, balance_id, created_at, creator_id, creator_type)"\
        " SELECT '{}', 2, 1, '{}', balances.id, extract(epoch from now() at time zone 'utc')::integer, 15, 'users'"\
        " FROM balances" \
        " JOIN users ON users.id = balances.user_id" \
        " WHERE users.phone = '{}';\n" \
        "UPDATE balances" \
        " SET bucket_1 = bucket_1 + '{}', bucket_2 = bucket_2 - '{}'" \
        " FROM users" \
        " WHERE balances.user_id = users.id AND users.phone = '{}';\n" \
        "commit;\n\n".format(row[2],row[5],row[1],row[2],row[2],row[1]);

print(request)
