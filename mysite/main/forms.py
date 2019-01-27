from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ('이름', '위도', '경도', '메인사진', '서브사진', '소개', '위치', '전화', '인스타',)