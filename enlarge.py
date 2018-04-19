#!/usr/bin/env python2

import os

# repeat n times
n = 10000

src = 'college_towns.txt'
src_fd = open(src,'rb')

dst = '%s_%s' % (n,src)
dst_fd = open(dst,'wb')

for row in src_fd:

    if row.rfind('[edit]') == -1:
        # university row
        for i in range(n):
            dst_fd.write(row)
    else:
        # state row
        dst_fd.write(row)

src_fd.close()
dst_fd.close()