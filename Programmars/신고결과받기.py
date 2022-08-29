def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    report_s = {}
    report_o = {}
    for log in report:
        s, o = log.split(' ')
        if s not in report_s.keys():
            report_s[s] = []
        report_s[s].append(o)

        if o not in report_o.keys():
            report_o[o] = 1
        else :
            report_o[o] +=1
    for id in id_list:
        cnt = 0
        if id in report_s.keys():
            for p in report_s[id]:
                if report_o[p] >= k :
                       cnt +=1
        answer.append(cnt) 
    
        
    return answer



def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


# List에 있는 원소들을 key로 Dictionary 초기화할때
# reports = {x : 0 for x in id_list}
# list의 해당 element의 index 뽑는 법 : list.index(element) 