from django import forms

# 모델클래스를 ㅑmport해야한다
# froom 폴더명을 적고. 파일명을 적고 import 클래스를 해야한다
# board 에 같은 위치

from board.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board  # model 변수에[ 모델클래스를 연결한다
        fields = (["title", "writer", "contents"],)
        labels = {"title": "제목", "writer": "작성자", "contents": "내용"}
