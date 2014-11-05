#!/usr/bin/env python
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from ztransform import ztransform

class qa_ztransform (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
        src_data = [1]*1
	src_data1 = [0]*50
	src_data = list(src_data + src_data1)
	src = gr.vector_source_f(src_data)
	sqr = ztransform()
	sqr.set_parameters("1 0 0","1 -4 4",1)
	dst = gr.vector_sink_f()
	self.tb.connect(src,sqr)
	self.tb.connect(sqr,dst)
	self.tb.run()
	result_data = dst.data()
	print result_data 
	import matplotlib.pyplot as plt
	plt.plot(result_data)
	plt.show()
        # check data


if __name__ == '__main__':
    gr_unittest.main()
