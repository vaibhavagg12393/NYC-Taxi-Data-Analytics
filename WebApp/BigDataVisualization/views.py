from django.shortcuts import render
from getdata import *
from django.template.defaulttags import register
import json


# Create your views here.

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_ele(list, i):
    return list[int(i)]


def index(request):
    return render(request, 'BigDataVisualization/home.html')


def visualize(request):
    return render(request, 'BigDataVisualization/visualize.html')


def report(request, report_id):
    report_id = int(report_id)
    chart = ""
    result = {"chart": chart}
    if report_id == 1:
        all_data = get_output("Output/MaxTraffic/")
        i = 0
        for data in all_data:
            x = []
            y = []
            for d in data.split("\n"):
                if d == "":
                    continue
                vals = d.split("\t")
                x.append(vals[0])
                y.append(float(vals[1]))
            if i == 0:
                chart_2013 = get_traffic_chart(x, y)
            elif i == 1:
                chart_2014 = get_traffic_chart(x, y)
            else:
                chart_2015 = get_traffic_chart(x, y)
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 2:
        all_data = get_output("Output/RateCode/")
        x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        i = 0
        for data in all_data:
            y1 = []
            y2 = []
            y3 = []
            y4 = []
            y5 = []
            for d in data.split("\n"):
                values = d.split(",")
                if len(values) < 7:
                    continue
                y1.append(float(values[2]))
                y2.append(float(values[3]))
                y3.append(float(values[4]))
                y4.append(float(values[5]))
                y5.append(float(values[6]))
            if i == 0:
                chart_2013 = get_ratecode_chart(x, [y1, y2, y3, y4, y5])
            elif i == 1:
                chart_2014 = get_ratecode_chart(x, [y1, y2, y3, y4, y5])
            else:
                chart_2015 = get_ratecode_chart(x, [y1, y2, y3, y4, y5])
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 3:
        all_data = get_output("Output/NightLife/")
        i = 0
        for data in all_data:
            x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            chart_tmp = "<table class=\'table table-striped\' id=\'output_table\'>" \
                        + "<thead><tr><th>Month/Rank</th> <td>1</td><td>2</td><td>3</td><td>4</td>" \
                        + "<td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr></thead>"
            pk = None
            c = 1
            chart_tmp += "<tr><td>" + str(x[c - 1]) + "</td>"
            for d in data.split("\n"):
                if "\t" not in d:
                    continue
                key, record = d.split("\t")
                if not pk or pk == key.split(",")[0]:
                    chart_tmp += "<td>" + key.split(",")[1] + "," + key.split(",")[2] + "</td>"
                else:
                    c += 1
                    chart_tmp += "</tr> <tr> <td>" + str(x[c - 1]) + "</td><td>" + key.split(",")[1] + "," + \
                                 key.split(",")[2] + "</td>"
                pk = key.split(",")[0]
            chart_tmp += "</tr>"
            chart_tmp += "</table>"
            if i == 0:
                chart_2013 = chart_tmp
            elif i == 1:
                chart_2014 = chart_tmp
            else:
                chart_2015 = chart_tmp
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null",
                  "html": "html"}
    elif report_id == 6:
        all_data = get_output("Output/CreditCashDist/")
        i = 0
        for data in all_data:
            x = []
            y = []
            card = []
            cash = []
            dispute = []
            no_charge = []
            unknown = []
            for d in data.split("\n"):
                if d == "":
                    continue
                vals = d.split("\t")
                x.append(vals[0])
                tmp = []
                values = vals[1].split(",")
                card.append(float(values[0].split(':')[1].strip()))
                cash.append(float(values[1].split(':')[1].strip()))
                dispute.append(float(values[2].split(':')[1].strip()))
                no_charge.append(float(values[3].split(':')[1].strip()))
                unknown.append(float(values[4].split(':')[1].strip()))
            y.append(card)
            y.append(cash)
            y.append(dispute)
            y.append(no_charge)
            y.append(unknown)
            if i == 0:
                chart_2013 = get_credit_cash(x, y)
            elif i == 1:
                chart_2014 = get_credit_cash(x, y)
            else:
                chart_2015 = get_credit_cash(x, y)
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 4:
        all_data = get_output("Output/FareTime/")
        d_time_2013 = {}
        d_dist_2013 = {}
        n_time_2013 = {}
        n_dist_2013 = {}
        time_keys_2013 = []
        dist_keys_2013 = []
        d_time_2014 = {}
        d_dist_2014 = {}
        n_time_2014 = {}
        n_dist_2014 = {}
        time_keys_2014 = []
        dist_keys_2014 = []
        d_time_2015 = {}
        d_dist_2015 = {}
        n_time_2015 = {}
        n_dist_2015 = {}
        time_keys_2015 = []
        dist_keys_2015 = []
        i = 0
        for data in all_data:
            if i == 0:
                for record in data.split("\n"):
                    if len(record.split("\t")) < 2:
                        continue
                    key = record.split("\t")[0]
                    value = record.split("\t")[1]
                    type, time_slot, dist_range = key.split(",")
                    fare, trip_time = map(float, value.split(","))
                    if time_slot not in time_keys_2013:
                        time_keys_2013.append(time_slot)
                    if dist_range not in dist_keys_2013:
                        dist_keys_2013.append(dist_range)
                    if type == "weekend":
                        if not n_time_2013.get(time_slot):
                            n_time_2013[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            n_time_2013[time_slot][0].append(dist_range)
                            n_time_2013[time_slot][1].append(fare)
                            n_time_2013[time_slot][2].append(trip_time)
                        if not n_dist_2013.get(dist_range):
                            n_dist_2013[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            n_dist_2013[dist_range][0].append(time_slot)
                            n_dist_2013[dist_range][1].append(fare)
                            n_dist_2013[dist_range][2].append(trip_time)
                    else:
                        if not d_time_2013.get(time_slot):
                            d_time_2013[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            d_time_2013[time_slot][0].append(dist_range)
                            d_time_2013[time_slot][1].append(fare)
                            d_time_2013[time_slot][2].append(trip_time)
                        if not d_dist_2013.get(dist_range):
                            d_dist_2013[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            d_dist_2013[dist_range][0].append(time_slot)
                            d_dist_2013[dist_range][1].append(fare)
                            d_dist_2013[dist_range][2].append(trip_time)
            elif i == 1:
                for record in data.split("\n"):
                    if len(record.split("\t")) < 2:
                        continue
                    key = record.split("\t")[0]
                    value = record.split("\t")[1]
                    type, time_slot, dist_range = key.split(",")
                    fare, trip_time = map(float, value.split(","))
                    if time_slot not in time_keys_2014:
                        time_keys_2014.append(time_slot)
                    if dist_range not in dist_keys_2014:
                        dist_keys_2014.append(dist_range)
                    if type == "weekend":
                        if not n_time_2014.get(time_slot):
                            n_time_2014[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            n_time_2014[time_slot][0].append(dist_range)
                            n_time_2014[time_slot][1].append(fare)
                            n_time_2014[time_slot][2].append(trip_time)
                        if not n_dist_2014.get(dist_range):
                            n_dist_2014[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            n_dist_2014[dist_range][0].append(time_slot)
                            n_dist_2014[dist_range][1].append(fare)
                            n_dist_2014[dist_range][2].append(trip_time)
                    else:
                        if not d_time_2014.get(time_slot):
                            d_time_2014[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            d_time_2014[time_slot][0].append(dist_range)
                            d_time_2014[time_slot][1].append(fare)
                            d_time_2014[time_slot][2].append(trip_time)
                        if not d_dist_2014.get(dist_range):
                            d_dist_2014[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            d_dist_2014[dist_range][0].append(time_slot)
                            d_dist_2014[dist_range][1].append(fare)
                            d_dist_2014[dist_range][2].append(trip_time)
            else:
                for record in data.split("\n"):
                    if len(record.split("\t")) < 2:
                        continue
                    key = record.split("\t")[0]
                    value = record.split("\t")[1]
                    type, time_slot, dist_range = key.split(",")
                    fare, trip_time = map(float, value.split(","))
                    if time_slot not in time_keys_2015:
                        time_keys_2015.append(time_slot)
                    if dist_range not in dist_keys_2015:
                        dist_keys_2015.append(dist_range)
                    if type == "weekend":
                        if not n_time_2015.get(time_slot):
                            n_time_2015[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            n_time_2015[time_slot][0].append(dist_range)
                            n_time_2015[time_slot][1].append(fare)
                            n_time_2015[time_slot][2].append(trip_time)
                        if not n_dist_2015.get(dist_range):
                            n_dist_2015[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            n_dist_2015[dist_range][0].append(time_slot)
                            n_dist_2015[dist_range][1].append(fare)
                            n_dist_2015[dist_range][2].append(trip_time)
                    else:
                        if not d_time_2015.get(time_slot):
                            d_time_2015[time_slot] = [[dist_range], [fare], [trip_time]]
                        else:
                            d_time_2015[time_slot][0].append(dist_range)
                            d_time_2015[time_slot][1].append(fare)
                            d_time_2015[time_slot][2].append(trip_time)
                        if not d_dist_2015.get(dist_range):
                            d_dist_2015[dist_range] = [[time_slot], [fare], [trip_time]]
                        else:
                            d_dist_2015[dist_range][0].append(time_slot)
                            d_dist_2015[dist_range][1].append(fare)
                            d_dist_2015[dist_range][2].append(trip_time)
            i += 1
        result = {"chart": chart, "d_dist_2013": json.dumps(d_dist_2013), "d_time_2013": json.dumps(d_time_2013),
                  "n_dist_2013": json.dumps(n_dist_2013), "n_time_2013": json.dumps(n_time_2013),
                  "time_keys_2013": time_keys_2013,
                  "dist_keys_2013": dist_keys_2013,
                  "d_dist_2014": json.dumps(d_dist_2014), "d_time_2014": json.dumps(d_time_2014),
                  "n_dist_2014": json.dumps(n_dist_2014), "n_time_2014": json.dumps(n_time_2014),
                  "time_keys_2014": time_keys_2014,
                  "dist_keys_2014": dist_keys_2014,
                  "d_dist_2015": json.dumps(d_dist_2015), "d_time_2015": json.dumps(d_time_2015),
                  "n_dist_2015": json.dumps(n_dist_2015), "n_time_2015": json.dumps(n_time_2015),
                  "time_keys_2015": time_keys_2015,
                  "dist_keys_2015": dist_keys_2015, "check_chart": "FareTime"}
    elif report_id == 5:
        all_data = get_output("Output/CreditCashTime/")
        i = 0
        for data in all_data:
            x = []
            y = []
            night = []
            day = []
            d = data.split("\n")
            vals = d[0].split("\t")
            values = vals[1].split(",")
            day.append(float(values[0].split(':')[1].strip()))
            day.append(float(values[1].split(':')[1].strip()))
            day.append(float(values[2].split(':')[1].strip()))
            day.append(float(values[3].split(':')[1].strip()))
            day.append(float(values[4].split(':')[1].strip()))
            vals = d[1].split("\t")
            values = vals[1].split(",")
            night.append(float(values[0].split(':')[1].strip()))
            night.append(float(values[1].split(':')[1].strip()))
            night.append(float(values[2].split(':')[1].strip()))
            night.append(float(values[3].split(':')[1].strip()))
            night.append(float(values[4].split(':')[1].strip()))
            x = ['Card', 'Cash', 'Dispute', 'No Charge', 'Unknown']
            y.append(day)
            y.append(night)
            if i == 0:
                chart_2013 = get_credit_cash_time(x, y)
            elif i == 1:
                chart_2014 = get_credit_cash_time(x, y)
            else:
                chart_2015 = get_credit_cash_time(x, y)
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 7:
        all_data = get_output("Output/MonthTrips/")
        i = 0
        chart_2013 = ""
        chart_2014 = ""
        chart_2015 = ""
        x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for data in all_data:
            y = []
            d = data.split("\n")
            for j in d:
                if "\t" not in j:
                    continue
                k = j.split("\t")
                y.append(float(k[1]))
            if i == 0:
                chart_2013 = get_month_trip(x, y)
            elif i == 1:
                chart_2014 = get_month_trip(x, y)
            else:
                chart_2015 = get_month_trip(x, y)
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 9:
        all_data = get_output("Output/BoroughTrips/")
        i = 0
        chart_2013 = ""
        chart_2014 = ""
        chart_2015 = ""
        for data in all_data:
            x = []
            y = []
            for d in data.split("\n"):
                if len(d.split("\t")) >= 2:
                    x.append(d.split("\t")[0])
                    y.append(d.split("\t")[1])
            if i == 0:
                chart_2013 = get_borough_trip(x, y)
            elif i == 1:
                chart_2014 = get_borough_trip(x, y)
            else:
                chart_2015 = get_borough_trip(x, y)
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null"}
    elif report_id == 10:
        all_data = get_output("Output/FavTrips/")
        i = 0
        chart_2013 = ""
        chart_2014 = ""
        chart_2015 = ""
        for data in all_data:
            chart_tmp = "<table class=\'table table-striped\' id=\'output_table\'>" \
                        + "<thead><tr><th>Source</th> <th>Destination</th><th>Num Trips</th></tr></thead>"
            for d in data.split("\n"):
                if len(d.split("\t")) < 2:
                    continue
                key, value = d.split("\t")
                chart_tmp += "<tr><td>" + key.split(",")[0] + "</td>" + "<td>" + key.split(",")[1] + "</td>" \
                             + "<td>" + value + "</td>" + "</tr>"
            chart_tmp += "</table>"
            if i == 0:
                chart_2013 = chart_tmp
            elif i == 1:
                chart_2014 = chart_tmp
            else:
                chart_2015 = chart_tmp
            chart_tmp = ""
            i += 1
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null",
                  'html': 'html'}
    elif report_id == 8:
        all_data = get_output("Output/DayTrips/")
        i = 0
        chart_2013 = ""
        chart_2014 = ""
        chart_2015 = ""
        dates_2013 = ['2013-01-01', '2013-02-14', '2013-12-24', '2013-12-25', '2013-12-31', '2013-07-04', '2013-11-28',
                      '2013-11-29', '2013-10-31']
        dates_2014 = ['2014-01-01', '2014-02-14', '2014-12-24', '2014-12-25', '2014-12-31', '2014-07-04', '2014-11-27',
                      '2014-11-28', '2014-10-31']
        dates_2015 = ['2015-01-01', '2015-02-14', '2015-12-24', '2015-12-25', '2015-12-31', '2015-11-26', '2015-11-27',
                      '2015-10-31', '2015-07-04']
        d_2013 = {}
        d_2014 = {}
        d_2015 = {}
        avg_2013 = 0
        avg_2014 = 0
        avg_2015 = 0
        for data in all_data:
            first = True
            x = []
            y = []
            for d in data.split("\n"):
                if first:
                    first = False
                    x.append(d.split("\t")[0])
                    y.append(float(d.split("\t")[1].split(".")[0]))
                if "\t" not in d:
                    continue
                if i == 0:
                    avg_2013 += float(d.split("\t")[1])
                    if d.split("\t")[0] in dates_2013:
                        d_2013[d.split("\t")[0]] = int(d.split("\t")[1])
                elif i == 1:
                    avg_2014 += float(d.split("\t")[1])
                    if d.split("\t")[0] in dates_2014:
                        d_2014[d.split("\t")[0]] = int(d.split("\t")[1])
                else:
                    avg_2015 += float(d.split("\t")[1])
                    if d.split("\t")[0] in dates_2015:
                        d_2015[d.split("\t")[0]] = int(d.split("\t")[1])
            i += 1
        chart_2013 = "<table class='table table-striped' id='output_table'><thead><th>Date</th><th>Day</th><th>Num Trips</th></thead>"
        for key in d_2013.keys():
            chart_2013 += "<tr><td>"+str(key)+"</td><td>"+map_date(key)+"</td><td>"+str(d_2013[key])+"</td></tr>"
        chart_2013 += "<tr><td colspan=2>Average Trips Per day</td><td>"+str(int(avg_2013/365))+"</td></tr>"
        chart_2013 += "</table>"
        chart_2014 = "<table class='table table-striped' id='output_table'><thead><th>Date</th><th>Day</th><th>Num Trips</th></thead>"
        for key in d_2014.keys():
            chart_2014 += "<tr><td>"+str(key)+"</td><td>"+map_date(key)+"</td><td>"+str(d_2014[key])+"</td></tr>"
        chart_2014 += "<tr><td colspan=2>Average Trips Per day</td><td>"+str(int(avg_2014/365))+"</td></tr>"
        chart_2014 += "</table>"
        chart_2015 = "<table class='table table-striped' id='output_table'><thead><th>Date</th><th>Day</th><th>Num Trips</th></thead>"
        for key in d_2015.keys():
            chart_2015 += "<tr><td>"+str(key)+"</td><td>"+map_date(key)+"</td><td>"+str(d_2015[key])+"</td></tr>"
        chart_2015 += "<tr><td colspan=2>Average Trips Per day</td><td>"+str(int(avg_2015/365))+"</td></tr>"
        chart_2015 += "</table>"
        result = {"chart_2013": chart_2013, "chart_2014": chart_2014, "chart_2015": chart_2015, "check_chart": "null",
                  'html': 'html'}
    return render(request, 'BigDataVisualization/report.html', result)


def faretime(request):
    a = []
    for i in range(2012,2031):
        a.append(i)
    d = ["0-3","3-6","6-9","9-12","12-15","15-18","18-21","21-24","24-50"]
    t = ["0-7","10-12","12-17","17-20","20-22","22-24"]
    return render(request, 'BigDataVisualization/predict.html',{"years":a,"dist_range":d,"time_range":t})