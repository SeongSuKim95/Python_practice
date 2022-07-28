def solution(fees, records):
    answer = []
    record_time = {}
    record_IO = {}
    for i in records:
        time,number,IO = i.split(' ')
        if number not in record_IO.keys():
            record_IO[number] = time
        else:
            # time
            h_I,m_I = map(int,record_IO.pop(number).split(':'))
            h_O,m_O = map(int,time.split(':'))
            IO_time = (h_O - h_I) * 60 + (m_O - m_I)
            if number not in record_time.keys():
                record_time[number] = IO_time
            else:
                record_time[number] += IO_time
    
    for k,v in record_IO.items():
        h_I,m_I = map(int,v.split(':'))
        IO_time = (23 - h_I)* 60 + (59 - m_I)
        if k not in record_time.keys():
                record_time[k] = IO_time
        else:
                record_time[k] += IO_time       
                
    for k,v in sorted(record_time.items(),key = lambda x : int(x[0])):
            if v <= fees[0]:
               answer.append(fees[1])
            else:
               temp = (v- fees[0]) % fees[2]
               if temp == 0 :
                    answer.append(fees[1] + ((v-fees[0])//fees[2])*fees[3])
               else:
                    answer.append(fees[1] + ((v-fees[0])//fees[2]+1)*fees[3])
    return answer