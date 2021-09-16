import csv

with open('Stars/CSV Files/Stars_with_Gravity.csv', 'r') as f:
    reader = list(csv.reader(f))
    reader.pop(0)

    final_star_list = []
    for index, star_data in enumerate(reader):
        final_dic = {
            "Name": star_data[1],
            "Distance": float(star_data[2]),
            "Mass": float(star_data[3]),
            "Radius": float(star_data[4]),
            "Gravity": float(star_data[5])
        }
        final_star_list.append(final_dic)
    print(final_star_list)