from django.shortcuts import render
from board.models import Board  # Board모델을 import 하고



# Create your views here.
# 1. ORM방식 - 테이블이 복잡해지면 사용이 불편하다.
def list(request):
    # boardList = Board.objects.all()  #보드 모델 클래스를 만들면 오브젝트를 통해 모델에 있는걸 다들고옴
    boardList = Board.objects.order_by("-id")
    return render(request, "board/board_list.html", {"boardList": boardList})


# 2. 직접 쿼리 실행하기
from django.db import connection

# 디비 연결자를 가져온다. - settings.py에서 지정된 디비 연결자를 가져온다.
from common.CommonUtil import dictfetchall, CommonPage


def list2(request):
    pg = 1
    cursor = connection.cursor()
    # cursor 객체가 디비에 데이터 읽고쓰기를 담당
    # 전체 데이터 건수를 알아야 페이징이 가능하다 
    cursor.execute(sql)
    totalCnt = int(cursor.fetchone()[0])
    commonPage = CommonPage(totalCnt, pg, 10)

    
    sql = """
        select A.id, A.title, A.writer, A.contents
        ,A.wdate
        ,A.hit
        from board_board A
        order by id desc
    """
    

    boardList = dictfetchall(cursor)
    print(boardList)
    # boardList = Board.objects.all()  #보드 모델 클래스를 만들면 오브젝트를 통해 모델에 있는걸 다들고옴
    # boardList = None
    # boardList = Board.objects.order_by('-id')
    return render(request, "board/board_list.html", {"boardList": boardList,
                                                     "commonPage":cp})
