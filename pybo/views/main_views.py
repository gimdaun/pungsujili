import logging

from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question

logger = logging.getLogger('pybo')


def main(request):
    logger.info("INFO 레벨로 출력")

    kw = request.GET.get('kw', '')  # 검색어
    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()
    #context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # <------ so 추가
    #return render(request, 'pybo/question_list.html', context)
    return render(request, 'pybo/main.html',{'kw': kw})
