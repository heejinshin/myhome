def dictfetchall(cursor):
    print(cursor.description)
    columns = [col[0].lower() for col in cursor.description]
    # cursor의 description에 각 필드 이름 정보 - 배열
    # columns ['id', 'title', 'contents', 'writer']
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class CommonPage: 
     

if self.curPage >=1: # 앞으로 이동 가능 
    self.isPrev = True 
    self.prev_page self.curPage
else: # 더이상 앞으로 갈 수 없음 
        self.isPrev = False 
        sef.prev_page = self.curPage = 1

if self.curPage <=self.totalPage: # 뒤로 이동 가능 
    self.isNext = True 
    self.next_page = self.curPage + 1
else: # 더이상 뒤로 갈 수 없음 
    self.isNext = False 
    self.next_page = self.curPage

self.page_range = range(self.start, self.end)
