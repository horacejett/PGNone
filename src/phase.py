# -*- coding:utf-8 -*-

class sqlphase():

    # 类初始化，传入变量为str类型
    def __init__(self, v_sql_init):
        self.v_sql_init = v_sql_init

    # 为指定的字符前后加上空格，方便后续处理
    def sqlblank(self):
        self.v_sql_blank = self.v_sql_init
        v_str_list = ['$', "'", '--', '/*', '*/', ',', '(', ')', '<>', '!=', '>=', '<=', '>', '<', '=']
        for v_str in v_str_list:
            self.v_sql_blank = self.v_sql_blank.replace(v_str, ' '+v_str+' ')
        return self.v_sql_blank

    # 按行号分割SQL文本为列表
    def sqlline(self):
        self.v_sql_line = [(0, '-- SQL Head')]
        v_line_list = self.v_sql_blank.strip('\n').split('\n')
        for vid,v_line in enumerate(v_line_list):
            self.v_sql_line.append((vid+1, v_line))
        return self.v_sql_line













aa=sqlphase('''select distinct b.SEQ,a.PROID_STK850 作品ID,A.F003V_STK850 类型
  from stk850 a,stk854 b,stk857 c
  where a.isvalid=1
  and b.isvalid=1
  and c.isvalid=1
  and c.rtime>=CURRENT_DATE-7
  and a.PROID_STK850=b.PROID_STK854
  and a.F003V_STK850 not in ('电视剧','网络剧','动画','综艺节目','网络大电影')
  and c.VSEQ_STK857=b.seq
  ORDER BY 3 desc''')

print(aa,aa.sqlblank())
print(aa.sqlline())