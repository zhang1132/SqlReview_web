# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
from models import InceptionBackupInformation,inc_test
import models


# Create your views here.

def sqlrollback(request):
    sql=request.POST['sqlrollback']
    list=InceptionBackupInformation.objects.all().filter(sql_statement=sql)
    opid=list[0].opid_time
    tablename=list[0].tablename
    #tablename='inc_test'
    if tablename=='inc_test':
        list=inc_test.objects.all().filter(opid_time=opid);
    print(list)
    return HttpResponse(sql)

def rollback(request):
    list=InceptionBackupInformation.objects.all().order_by('time')[0:10]
    context={'list':list}
    return render(request, 'inception/rollback.html',context)


def inception(request):
    return render(request, 'inception/inception.html')


def sqlhangle(request):
    sql2 = request.POST['mysql']
    if sql2.endswith(";"):
        sql1 = '/*--user=root;--password=123zxc;--host=192.168.8.108;--execute=1;--port=3306;*/\
                inception_magic_start;\
                use zhanghui;'
        sql3 = 'inception_magic_commit;'
        sql = sql1 + sql2 + sql3
        try:
            conn = MySQLdb.connect(host='192.168.3.233', user='root', passwd='', db='', port=6669)
            cur = conn.cursor()
            ret = cur.execute(sql)
            result = cur.fetchall()
            num_fields = len(cur.description)
            field_names = [i[0] for i in cur.description]
            print field_names
            for row in result:
                print row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5], "|", row[6], "|", row[
                    7], "|", row[8], "|", row[9], "|", row[10]
            cur.close()
            conn.close()
            result = result[1][4].split("\n")
            print(result)
            context = {"result": result,"sql_review":sql2}
            return render(request, 'inception/inception.html', context)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            return HttpResponse('404')

    else:
        context = {"result": "请以 ；结尾 ！！！" ,"sql_review":sql2}
        return render(request, 'inception/inception.html', context)
