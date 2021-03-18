"""
了解c语言的人，一定会知道struct结构体在c语言中的作用，它定义了一种结构，里面包含不同类型的数据(int,char,bool等等)，
方便对某一结构对象进行处理。而在网络通信当中，大多传递的数据是以二进制流（binary data）存在的。
当传递字符串时，不必担心太多的问题，而当传递诸如int、char之类的基本数据的时候，
就需要有一种机制将某些特定的结构体类型打包成二进制流的字符串然后再网络传输，
而接收端也应该可以通过某种机制进行解包还原出原始的结构体数据。python中的struct模块就提供了这样的机制，
该模块的主要作用就是对python基本类型值与用python字符串格式表示的C struct类型间的转化
（This module performs conversions between Python values and C structs represented as Python strings.）。
stuct模块提供了很简单的几个函数，下面写几个例子。
"""
#基本的pack与unpack
import struct
import binascii

values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)

print('Original values:', values)
print('Format string :', s.format)
print('Uses :', s.size, 'bytes')
print('Packed Value :', binascii.hexlify(packed_data))
print('Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data)
"""
格式符	C语言类型	Python类型	Standard size
x	pad byte(填充字节)	no value	 
c	char	string of length 1	1
b	signed char	integer	1
B	unsigned char	integer	1
?	_Bool	bool	1
h	short	integer	2
H	unsigned short	integer	2
i	int	integer	4
I(大写的i)	unsigned int	integer	4
l(小写的L)	long	integer	4
L	unsigned long	long	4
q	long long	long	8
Q	unsigned long long	long	8
f	float	float	4
d	double	float	8
s	char[]	string	 
p	char[]	string	 
P	void *	long
"""