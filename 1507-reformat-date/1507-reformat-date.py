class Solution:
    def reformatDate(self, date: str) -> str:
        month = {
            "Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04',
            "May":'05', "Jun":'06', "Jul":'07', "Aug":'08',
            "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'
        }

        data = date.split()
        Day = {"s", "n", "d", "r", "h", "t"}
        result = ""
        Separt = "-"

        for i in range(len(data)-1, -1, -1):
            if i == 2:                     
                result += data[i]
                
            elif i == 1:                   
                result += Separt + month[data[i]]
                
            else:                          
                day = ""
                for ch in data[i]:
                    if ch not in Day:
                        day += ch
                
                day = day.zfill(2)
                result += Separt + day

        return result
