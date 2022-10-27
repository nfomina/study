import json
import csv
from datetime import datetime

with open("exam_results.csv", encoding='UTF-8') as file_in, open("best_scores.json", "w", encoding='UTF-8') as file_out:
    file_data = csv.reader(file_in, delimiter=',')
    headers = next(file_data)
    students = [dict(zip(headers, i)) for i in file_data]
    res = {}
    for student in students:
        if res.get(student['email']):
            if student['score'] > res[student['email']]['best_score']:
                res[student['email']]['best_score'] = student['score']
                res[student['email']]['date_and_time'] = student['date_and_time']
            elif student['score'] == res[student['email']]['best_score']:
                if datetime.strptime(student['date_and_time'],
                                     '%Y-%m-%d %H:%M:%S') >= datetime.strptime(res[student['email']]['date_and_time'],
                                                                               '%Y-%m-%d %H:%M:%S'):
                    res[student['email']]['date_and_time'] = student['date_and_time']
        else:
            res[student['email']] = {'name': student['name'], 'surname': student['surname'],
                                     'best_score': student['score'], 'date_and_time': student['date_and_time']}
    best_scores = []
    for item in sorted(res):
        best_scores.append({"name": res[item]["name"],
                            "surname": res[item]["surname"],
                            "best_score": int(res[item]["best_score"]),
                            "date_and_time": res[item]["date_and_time"],
                            "email": item})
    json.dump(best_scores, file_out)


# short
# import json, csv
#
# with open('exam_results.csv', encoding='utf8') as file:
#     head, *rows = list(csv.reader(file, delimiter=','))
#
# rows.sort(key=lambda x: x[2])  # sort by score
# rows.sort(key=lambda x: x[3])  # sort by time
# rows.sort(key=lambda x: x[4])  # sort by email
#
# data = {}
# for name, surname, score, date_and_time, email in rows:
#     data[email] = {'name': name, 'surname': surname, 'best_score': int(score),
#                    'date_and_time': date_and_time, 'email': email}
#
# with open('best_scores.json', 'w', encoding='utf8') as file:
#     json.dump(list(data.values()), file, indent=3)