from django.shortcuts import render
from django.http import *
from django.db.models import Q
from .models import KeyValue, Persons, Rankssingle, Ranksaverage

# Create your views here.
current_db = "WCA_export1"


def get_current_db():
    global current_db
    current_db = KeyValue.objects.get(k="current_db")
    return current_db


def set_current_db(db_name):
    global current_db
    current_db = db_name

    result, created = KeyValue.objects.get_or_create(k="current_db")
    result.v = db_name
    result.save()


def changeDB(request):
    db_name = request.GET.get("db")
    set_current_db(db_name)
    ret = {
        'status': 'ok'
    }
    return JsonResponse(ret)


def queryId(request):
    wd_list = request.GET.get('wd').split()  # 关键字空格分割

    q_list = []  # 查询条件
    for wd in wd_list:
        q = Q(id__icontains=wd) | Q(name__icontains=wd)  # id或名字包含关键字
        q_list.append(q)
    results = Persons.objects.using(current_db).filter(*q_list)
    count = results.count()
    data = []
    count_ = 0
    for result in results:
        count_ += 1
        if count_ > 100:
            break
        data.append({
            'id': result.id,
            'subid': result.subid,
            'name': result.name,
            'countryId': result.countryid,
            'gender': result.gender
        })

    ret = {
        'status': 'ok',
        'count': count,
        'data': data
    }
    return JsonResponse(ret)


def ranksAverage(request):
    personId = request.GET.get('personId')
    results = Ranksaverage.objects.using(current_db).filter(personid=personId)
    data = []
    for result in results:
        data.append({
            'eventId': result.eventid,
            'best': result.best,
            'worldRank': result.worldrank,
            'continentRank': result.continentrank,
            'countryRank': result.countryrank
        })
    ret = {
        'status': 'ok',
        'data': data
    }
    return JsonResponse(ret)


def ranksSingle(request):
    personId = request.GET.get('personId')
    results = Rankssingle.objects.using(current_db).filter(personid=personId)
    data = []
    for result in results:
        data.append({
            'eventId': result.eventid,
            'best': result.best,
            'worldRank': result.worldrank,
            'continentRank': result.continentrank,
            'countryRank': result.countryrank
        })
    ret = {
        'status': 'ok',
        'data': data
    }
    return JsonResponse(ret)
