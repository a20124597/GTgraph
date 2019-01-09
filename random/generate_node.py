# -*- coding:utf-8 -*-
__author__ = 'huhao09'
import sys
import codecs
import random
import time


def generate_nodefile(node_file_name,num_node,label_num):
    f_node_wirtee=open(node_file_name,'w')
    for i in xrange(0,num_node):
        node_index=i
        node_label=random.randint(0, label_num-1)
        t_str=str(node_index)+'\t'+str(node_label)+'\n'
        f_node_wirtee.write(t_str)
    f_node_wirtee.close()
if __name__ == "__main__":
    #输入三个参数,nodefile_name,node_num,node_label
    print '参数个数为:', len(sys.argv), '个参数。'
    print '参数列表:', str(sys.argv)
    #node_file="synthetic.v"
    generate_nodefile(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))